
"""
app.py
"""

import concurrent.futures
import os
from flask import Flask, request, send_from_directory
from auth import auth  # import auth from auth.py
from flask_cors import CORS

from qtRunner import QtContainer
from loggerUtil import Logger
from config import UPLOAD_FOLDER

app = Flask(
    __name__,
    static_folder="dist",
    static_url_path=""
)
CORS(app)  # allow all origins temporarily

@app.route("/ping")
def ping():
    return "pong"

@app.route('/')
@auth.login_required
def index():
    return send_from_directory(app.static_folder, "index.html")

# Serve React assets (JS, CSS)
@app.route("/assets/<path:path>")
@auth.login_required
def assets(path):
    return send_from_directory(os.path.join(app.static_folder, "assets"), path)

executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

# Shared instances (created once)
logger = Logger()
qtContainer = QtContainer(logger)

@app.route('/upload', methods=['POST'])
@auth.login_required
def upload():
    """Upload images to a designated folder and calls for image processing"""
    if 'images' not in request.files:
        return "No file part", 400
    
    files = request.files.getlist('images')
    if not files:
        return "No selected files", 400

    saved_files = []

    for file in files:
        if file.filename == '':
            continue
        
        save_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(save_path)
        saved_files.append(file.filename)

        logger.logStatus(file.filename, "queued")
        executor.submit(qtContainer.runQtContainer, file.filename)

    return f"Files uploaded and queued: {', '.join(saved_files)}"

if __name__ == "__main__":
    """Run flask app on all LAN interfaces and port 5000"""
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
