FROM debian:trixie-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    qt6-base-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY qtBackend/ .

RUN cmake -S . -B build \
    && cmake --build build

CMD ["./build/qtprocessor"]
