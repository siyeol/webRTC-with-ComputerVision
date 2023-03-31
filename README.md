# WebRTC with Computer Vision


This repository contains the source code for webRTC based video conference platform compatible with Computer Vision Python APIs.

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
1. run python Flask `/computer_vision/server.py`
2. Move to the `webRTC` folder, install dependencies, and start the development server:
`cd webRTC`
`npm install` 
`npm start`
3. Expose the server using ngrok (optional): `ngrok http 3012`
4. Alternatively, you can use `https://localhost:3012` in Google Chrome.
5. Check for the `http /image 200` status code.

## System Architecture

![workflow](https://user-images.githubusercontent.com/33966473/134840473-2aa66fff-76f6-4e1a-9d4c-94ac5dee86bc.jpg)

## Application Workflow

This project is designed to provide real-time video chat with integrated computer vision capabilities. The key components and their interactions are described below:

- **Browser Execution:** The `webrtc/public/` directory contains the frontend components executed in the browser. The `js/objDetect.js` file plays a crucial role by extracting video frames and sending them to the server for processing.

- **Image Transmission:** The `postFile` function in the `webrtc/public/js/objDetect.js` file sends JPEG images to the Flask server at `http://127.0.0.1:5000/image`.

- **Performance:** The application's performance depends on the hardware. It achieves approximately 70fps on an M1 Apple Silicon and around 15fps on an Intel i5.

- **Server-side Processing:** The Flask server, located in the `/flask/server.py` file, listens for POST method requests. Upon receiving an image, it forwards it to the `object_detection_api.py` file for further processing, including object detection and pose estimation.

- **Result Communication:** After processing the image, the server can send the results back as JSON data to the JavaScript code for display in the browser. Alternatively, the data can be transmitted directly to a teacher using HTTP or Socket.IO.



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
