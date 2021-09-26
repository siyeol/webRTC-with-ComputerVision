# IMPORTS

import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import six.moves.urllib as urllib
import tarfile
import tensorflow as tf
import json
from keras.models import load_model


# if tf.__version__ != '1.4.0':
#   raise ImportError('Please upgrade your tensorflow installation to v1.4.0!')

# ENV SETUP  ### CWH: remove matplot display and manually add paths to references
model = load_model('Xception_on_DAiSEE_fc.h5')

# added to put object in JSON
class Object(object):
    def __init__(self):
        self.name="webrtcHacks TensorFlow Object Detection REST API"

    def toJSON(self):
        return json.dumps(self.__dict__)

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

def get_objects(image, threshold=0.5):
    # print(type(image))
    image = image.resize((299,299))
    image_np = load_image_into_numpy_array(image)
    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)

    predictions = model.predict(image_np_expanded)

    print("예측 : ", predictions[1][0][0], predictions[1][0][1])

    outputJson = json.dumps([1,2,3])
    return outputJson
