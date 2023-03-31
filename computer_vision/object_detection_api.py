import numpy as np

import cv2
import json

# TODO: load your third party Module
from load_third_party_module import sample_mediapipe_module

# TODO: load your model
from load_your_model import YourKerasModel


class ObjectDetection(object):
    def __init__(self):
        self.name="webrtcHacks TensorFlow Object Detection REST API"

    def toJSON(self):
        return json.dumps(self.__dict__)

    def get_objects(image):
        sample_model = YourKerasModel()

        (im_width, im_height) = image.size
        image_np = np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)
        rgbFrame = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)

        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        sample_prediction = sample_model.prediction(image_np)

        EAR, headArea, handLM, poseLM = sample_mediapipe_module(rgbFrame, rgbFrame, rgbFrame)

        # print(f'EAR:{EAR} / headArea:{headArea}')

        if not isinstance(sample_prediction, int) :
            Dout=sample_prediction.item()
        else:
            Dout=sample_prediction

        if not isinstance(EAR, int):
            Eout=EAR.item()
        else:
            Eout=EAR

        outputJson = json.dumps({"predict":Dout, "EAR":Eout, "headarea":headArea})

        return outputJson
