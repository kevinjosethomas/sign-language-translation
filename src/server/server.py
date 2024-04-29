import cv2
import logging
from flask import Flask, Response
from flask_socketio import SocketIO
from flask_socketio import emit

from store import Store
from recognition import Recognition

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
camera = cv2.VideoCapture(2)
recognition = Recognition()


def recognize():

    while camera.isOpened():

        success, image = camera.read()
        if not success:
            continue

        image, updated = recognition.process(image)

        _, buffer = cv2.imencode(".jpg", image)
        frame = buffer.tobytes()

        if updated:
            socketio.emit("transcription", Store.parsed)

        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def stream():
    return Response(recognize(), mimetype="multipart/x-mixed-replace; boundary=frame")


@socketio.on("connect")
def on_connect():
    print("Connected to client")


if __name__ == "__main__":
    socketio.run(app, debug=False, port=1234)