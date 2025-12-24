
"""
loggerUtil.py
"""

import json
import os
import threading

from config import UPLOAD_FOLDER


class Logger:
    """
    Thread-safe logging for file upload status tracking (queued, processing, done)
    """
    def __init__(self, status_file="processingStatus.json"):
        self.status_file = os.path.join(UPLOAD_FOLDER, "processingStatus.json")
        self.lock = threading.Lock()
        if not os.path.exists(self.status_file):
            with open(self.status_file, "w") as file:
                json.dump({}, file)

    def logStatus(self, filename, status):
        """
        Record file upload status
        """
        with self.lock:  # prevent race conditions
            with open(self.status_file, "r") as file:
                    data = json.load(file)

            data[filename] = status

            with open(self.status_file, "w") as file:
                json.dump(data, file, indent=2)