# Image Server

## Overview
This small hobby project allows uploading images from a (phone) browser and processing them in background Qt 6 container on Raspberry Pi or other platforms.

## Requirements
- Python 3
- Flask
- Docker
- Qt processor Docker image (ARM64)

## Qt Processor Docker Image (Build & Deploy)
Build the image containing the Qt processor

### Build for platform same as build host
```bash
docker build -t qt-processor .
```

### Build for another platform
- Register ARM emulators with the kernel.
```bash
docker run --privileged --rm tonistiigi/binfmt --install all
```
- Build image for intended platform (eg: linux/arm64)
```bash
docker buildx build --platform linux/arm64 -t qt-processor:arm64 --load .
```
Either copy the image (with `docker save` and `docker load`) or `Docker push` the image to Docker registry and `Docker pull` it on the target host.

## Getting Started
```bash
# Clone repo
git clone <repo_url>
cd image-server/src

# Run Flask (development)
python3 app.py

# Access web UI at:
http://<server-ip>:5000/