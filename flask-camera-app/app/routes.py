from flask import Blueprint, render_template, request, redirect, url_for
from .camera import Camera

app = Blueprint('app', __name__)
camera = Camera()

@app.route('/')
def index():
    images = camera.get_images()
    return render_template('index.html', images="")

@app.route('/capture', methods=['GET'])
def capture():
    camera.capture_image()
    return redirect(url_for('app.index'))

@app.route('/transfer', methods=['GET'])
def transfer():
    image_id = request.form.get('image_id')
#   camera.transfer_image(image_id)
    return redirect(url_for('app.index'))

@app.route('/control', methods=['GET'])
def control():
    action = request.form.get('action')
    if action == 'start':
        camera.start()
    elif action == 'stop':
        camera.stop()
    return redirect(url_for('app.index'))