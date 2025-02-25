from flask import Flask, Response, render_template, request, jsonify
from threading import Lock
from picamera2 import Picamera2
import logging
import cv2
from ImageProcessing import ImageProcessing
from ParamSetter import ParamSetter

# Flask app initialization
app = Flask(__name__)

# Camera and threading lock
camera = Picamera2()
lock = Lock()

# Initialize ParamSetter
param_setter = ParamSetter()

class CameraController:
    def __init__(self):
        self.param_setter = param_setter

    def initialize_camera(self):
        """Initialize the camera with the current resolution."""
        logging.debug(f"Initializing camera with resolution: {self.param_setter.camera_resolution}")
        camera.stop()
        camera.configure(camera.create_preview_configuration(main={"size": self.param_setter.camera_resolution}))
        camera.start()

    def update_clahe_params(self, data):
        """Update CLAHE parameters based on the data received from the frontend."""
        self.param_setter.clahe_for_value = int(data.get('for_value', self.param_setter.DEFAULT_PARAMS["for_value"]))
        self.param_setter.clahe_clip_limit = float(data.get('cliplimit_value', self.param_setter.DEFAULT_PARAMS["cliplimit_value"]))
        self.param_setter.clahe_tile_grid_size = int(data.get('tilegrid_value', self.param_setter.DEFAULT_PARAMS["tilegrid_value"]))

        resolution_str = data.get('resolution', self.param_setter.DEFAULT_PARAMS["resolution"])
        new_resolution = tuple(map(int, resolution_str.split('x')))
        if new_resolution != self.param_setter.camera_resolution:
            self.param_setter.camera_resolution = new_resolution
            self.initialize_camera()

    def apply_clahe_to_frame(self, frame):
        """Apply CLAHE to the frame using the parameters."""
        return ImageProcessing.apply_clahe(frame, self.param_setter.clahe_for_value, self.param_setter.clahe_clip_limit, self.param_setter.clahe_tile_grid_size)

# Instantiate the CameraController
camera_controller = CameraController()

@app.route('/update_clahe_params', methods=['POST'])
def update_clahe_params():
    data = request.json
    logging.debug(f"Received parameters: {data}")
    camera_controller.update_clahe_params(data)
    return jsonify({'success': True})

@app.route('/save_params', methods=['POST'])
def save_params():
    param_setter.save_params_to_file()
    return jsonify({'success': True})

@app.route('/load_params', methods=['POST'])
def load_params():
    param_setter.load_params_from_file()
    return jsonify({
        'for_value': param_setter.clahe_for_value,
        'cliplimit_value': param_setter.clahe_clip_limit,
        'tilegrid_value': param_setter.clahe_tile_grid_size,
        'resolution': f"{param_setter.camera_resolution[0]}x{param_setter.camera_resolution[1]}"
    })

@app.route('/load_default_params', methods=['POST'])
def load_default_params():
    param_setter.DEFAULT_PARAMS = param_setter.load_default_params_from_file()
    param_setter.clahe_for_value = param_setter.DEFAULT_PARAMS["for_value"]
    param_setter.clahe_clip_limit = param_setter.DEFAULT_PARAMS["cliplimit_value"]
    param_setter.clahe_tile_grid_size = param_setter.DEFAULT_PARAMS["tilegrid_value"]
    param_setter.camera_resolution = tuple(map(int, param_setter.DEFAULT_PARAMS["resolution"].split('x')))
    return jsonify({
        'for_value': param_setter.clahe_for_value,
        'cliplimit_value': param_setter.clahe_clip_limit,
        'tilegrid_value': param_setter.clahe_tile_grid_size,
        'resolution': f"{param_setter.camera_resolution[0]}x{param_setter.camera_resolution[1]}"
    })

def generate_video_stream():
    """Generate the video stream with CLAHE processing."""
    global camera, lock
    while True:
        with lock:
            frame = camera.capture_array()
            try:
                processed_frame = camera_controller.apply_clahe_to_frame(frame)
            except Exception as e:
                logging.error(f"Error during CLAHE processing: {e}")
                continue

            ret, jpeg = cv2.imencode('.jpg', processed_frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Load saved parameters and initialize camera at server start
    param_setter.load_params_from_file()
    camera_controller.initialize_camera()
    app.run(host='0.0.0.0', port=5000)
