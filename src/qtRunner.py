
"""
qtRunner.py
"""

import subprocess
import os

from config import UPLOAD_FOLDER

class QtContainer:
    """
    Provide functionality to run Qt 6 image processing container in the background.
    """
    def __init__(self, logger):
        self.logger = logger
        self.containerBaseCmd = [
            "docker", "run", "--rm",
            "-v", f"{os.path.abspath(UPLOAD_FOLDER)}:/app/uploads",
            "123dockerlab/qt-processor:arm64",
            "/app/build/qtprocessor"
        ]

    def runQtContainer(self, filepath):
        """
        Process image using Qt 6 Docker container.
        """
        print(f"Starting Qt container for {filepath}")
        self.logger.logStatus(filepath, "processing")

        containerCmd = self.containerBaseCmd + [f"/app/uploads/{filepath}"]

        try:
            subprocess.run(containerCmd)
        except subprocess.CalledProcessError as e:
            print(f"Error processing {filepath}: {e}")
            self.logger.logStatus(filepath, "error")
        else:
            print(f"Finished Qt container for {filepath}")
            self.logger.logStatus(filepath, "done") 
















