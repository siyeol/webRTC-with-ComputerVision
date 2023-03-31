# WebRTC with Computer Vision


This repository contains the source code for webRTC based video conference platform compatible with Computer Vision Python APIs.

## System Architecture

![workflow](https://user-images.githubusercontent.com/33966473/134840473-2aa66fff-76f6-4e1a-9d4c-94ac5dee86bc.jpg)

## Key Features

- Real-time video chat using WebRTC and Python APIs connected through frame capture, socket.io, and XMLhttpRequests.
- Object detection and pose estimation using Google MediaPipe and a custom Keras model
- Cross-platform support (tested on Chrome, Firefox, and Safari)

## Prerequisites

- Node.js (>= 14.x.x)
- npm (>= 6.x.x)
- Python (>= 3.6)
- Flask
- ngrok (optional)


## How to run
1. run python Flask /flask/server.py
2. move to webRTC folder and "npm install" and "npm start"
3. ngrok http 3012 (and follow the link) /or/ put https://localhost:3012 at Google Chrome
4. check for the http /image200 status code

## Usage

1. Grant permission to access your camera and microphone when prompted.
2. Share the generated URL with another participant to establish a video chat connection.
3. Enjoy real-time object detection and pose estimation during the video chat.

## Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your fork.
4. Create a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Google MediaPipe](https://mediapipe.dev/)
- [Keras](https://keras.io/)
- [WebRTC](https://webrtc.org/)
- [simple-peer](https://github.com/feross/simple-peer)
- [JS-AI - tfObjWebrtc](https://github.com/webrtcHacks/tfObjWebrtc)
- [Multipeer WebRTC](https://github.com/Dirvann/webrtc-video-conference-simple-peer)
