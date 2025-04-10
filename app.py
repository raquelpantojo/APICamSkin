# app.py

from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
from process_video import process_video  # Importe a função process_video
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

@app.route("/", methods=['POST'])
def detect():
    try:
        if request.method != "POST":
            return "Invalid method", 405

        if 'video' not in request.files:
            return "No video file found in request", 400

        video = request.files['video']
        if video.filename == '':
            return "No selected file", 400

        video_path = os.path.join(uploads_dir, secure_filename(video.filename))
        video.save(video_path)
        print(f"Received file: {video.filename} saved at {video_path}")

        if video.filename.endswith(('.mp4', '.avi', '.wmv')):
            pycrtvalue, pycrtincert = process_video(video_path)  # Chama process_video com video_path como argumento
            if pycrtvalue is not None and pycrtincert is not None:
                processed_data = {'pCRT': pycrtvalue, 'incerteza': pycrtincert}
            else:
                processed_data = {'pCRT': 0.0, 'incerteza': 0.0}
        else:
            processed_data = {'pCRT': 0.0, 'incerteza': 0.0}

        print(f"Processed data: {processed_data}")

        return jsonify(processed_data)
    
    except Exception as e:
        print(f"Exception: {e}")
        return "Internal Server Error", 500
    
@app.route('/return-files', methods=['GET'])
def return_file():
    obj = request.args.get('obj')
    loc = os.path.join("runs/detect", obj)
    print(loc)
    try:
        return send_file(os.path.join("runs/detect", obj), attachment_filename=obj)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
     app.run()