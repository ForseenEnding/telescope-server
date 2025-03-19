from flask import Response
import cv2

class Camera:
    def __init__(self):
        self.video_source = 0  # Default camera
        self.vid = cv2.VideoCapture(self.video_source)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
            
    def get_images(self):
        return ""

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                ret, jpeg = cv2.imencode('.jpg', frame)
                return jpeg.tobytes()
        return None

    def capture_image(self, filename):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                cv2.imwrite(filename, frame)
                return True
        return False

    def set_camera_property(self, prop_id, value):
        if self.vid.isOpened():
            self.vid.set(prop_id, value)

    def get_camera_property(self, prop_id):
        if self.vid.isOpened():
            return self.vid.get(prop_id)
        return None