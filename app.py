from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(save_path)
    return f"File uploaded successfully: {file.filename}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
