from flask import Flask, Response
from threading import Lock
from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2

app = Flask('_name_')
camera = PiCamera()
lock = Lock()

# Initalizing the camera on server startup
def initialize_camera():
    camera.resolution = (640, 480)
    camera.framerate = 30
    # camera.start_preview() # Camera preview

def apply_clahe(frame_img):
    # Image processing - CLAHE
        lab_img = cv2.cvtColor(frame_img, cv2.COLOR_BGR2LAB)
        l_channel, a_channel, b_channel = cv2.split(lab_img)

        for i in range(3):
            clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8+i*4,8+i*4))
            l_channel = clahe.apply(l_channel)

        lab_img = cv2.merge((l_channel,a_channel,b_channel))
        median_lab_img = cv2.medianBlur(lab_img, 3)
        median_bgr_img = cv2.cvtColor(median_lab_img, cv2.COLOR_LAB2BGR)

        return median_bgr_img

# Video stream generating function
def generate_video_stream():
    global camera
    global lock

    with lock:
        raw_capture = PiRGBArray(camera, size=(640, 480))
        for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
            # Capturing the current frame
            frame_img = frame.array
            
            # Image processing - CLAHE
            processed_frame = apply_clahe(frame_img)

            # Saving the video stream
            ret, jpeg = cv2.imencode('.jpg', processed_frame)

            # Sending the frame as a response to the client's request
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

            # Clearing the buffer
            raw_capture.truncate(0)


# Endpoint for the video stream
@app.route('/')
def video_feed():
    return Response(generate_video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Initialize the camera on server startup
    initialize_camera()

    # Run Flask server
    app.run(host='0.0.0.0', port=5000)
