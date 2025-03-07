from flask import Flask, Response, render_template, request, jsonify
from threading import Lock
from picamera2 import Picamera2
import logging
import cv2
from ImageProcessing import ImageProcessing
from ParamSetter import ParamSetter

# CONFIGURE LOGGING (Ensures all logs appear correctly)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("VinfinderAppLogger")

# Initialize Flask app
app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)  # Ensure Flask logs at DEBUG level

# Reduce Picamera2 log level to only show warnings and errors (hides debug/info logs)
logging.getLogger("picamera2").setLevel(logging.WARNING)

# Camera setup and threading lock
camera = Picamera2()
lock = Lock()

# Initialize Parameter Handler
param_setter = ParamSetter()

class CameraController:
    """Handles camera operations and CLAHE parameter updates."""

    def __init__(self):
        self.param_setter = param_setter
        logger.info("CameraController initialized.")

    def initialize_camera(self):
        """Configures and starts the camera with the current resolution."""
        logger.info(f"Initializing camera with resolution: {self.param_setter.camera_resolution}")
        camera.stop()
        camera.configure(camera.create_preview_configuration(main={"size": self.param_setter.camera_resolution}))
        camera.start()

    def update_clahe_params(self, data):
        """Updates CLAHE parameters based on the received frontend data."""
        logger.info(f"Received CLAHE parameters: {data}")

        self.param_setter.clahe_for_value = int(data.get('for_value', self.param_setter.DEFAULT_PARAMS["for_value"]))
        self.param_setter.clahe_clip_limit = float(data.get('cliplimit_value', self.param_setter.DEFAULT_PARAMS["cliplimit_value"]))
        self.param_setter.clahe_tile_grid_size = int(data.get('tilegrid_value', self.param_setter.DEFAULT_PARAMS["tilegrid_value"]))

        # Handle resolution change and reinitialize the camera
        resolution_str = data.get('resolution', self.param_setter.DEFAULT_PARAMS["resolution"])
        new_resolution = tuple(map(int, resolution_str.split('x')))
        if new_resolution != self.param_setter.camera_resolution:
            self.param_setter.camera_resolution = new_resolution
            self.initialize_camera()

    def apply_clahe_to_frame(self, frame):
        """Applies CLAHE processing to the frame using the current parameters."""
        return ImageProcessing.apply_clahe(frame, self.param_setter.clahe_for_value, self.param_setter.clahe_clip_limit, self.param_setter.clahe_tile_grid_size)

# Instantiate the Camera Controller
camera_controller = CameraController()

@app.route('/update_clahe_params', methods=['POST'])
def update_clahe_params():
    """Receives and applies new CLAHE parameters."""
    data = request.json
    camera_controller.update_clahe_params(data)
    return jsonify({'success': True})

@app.route('/save_params', methods=['POST'])
def save_params():
    """Saves current CLAHE parameters to a file."""
    param_setter.save_params_to_file()
    return jsonify({'success': True})

@app.route('/load_params', methods=['POST'])
def load_params():
    """Loads saved CLAHE parameters from a file and returns them."""
    param_setter.load_params_from_file()
    return jsonify({
        'for_value': param_setter.clahe_for_value,
        'cliplimit_value': param_setter.clahe_clip_limit,
        'tilegrid_value': param_setter.clahe_tile_grid_size,
        'resolution': f"{param_setter.camera_resolution[0]}x{param_setter.camera_resolution[1]}"
    })

@app.route('/load_default_params', methods=['POST'])
def load_default_params():
    """Loads default CLAHE parameters and applies them."""
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
    """Generates the video stream with real-time CLAHE processing."""
    global camera, lock
    while True:
        with lock:
            frame = camera.capture_array()
            try:
                processed_frame = camera_controller.apply_clahe_to_frame(frame)
            except Exception as e:
                logger.error(f"Error during CLAHE processing: {e}")
                continue  # Skip problematic frames instead of blocking the stream

            # Encode the processed frame as JPEG
            ret, jpeg = cv2.imencode('.jpg', processed_frame)
            if not ret:
                logger.error("Failed to encode frame to JPEG")
                continue  # Skip invalid frames

            # Yield the frame to be sent as part of the video stream
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Returns the video feed with processed frames."""
    return Response(generate_video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Load saved parameters and initialize the camera on server startup
    param_setter.load_params_from_file()
    camera_controller.initialize_camera()
    logger.info("Starting Flask server...")

    # Start Flask with logging and debugging enabled, but prevent double restarts
    app.run(host='0.0.0.0', port=80, debug=True, use_reloader=False)
