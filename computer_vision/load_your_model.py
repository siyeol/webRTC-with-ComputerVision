from keras.models import load_model
import cv2
import numpy as np

class YourKerasModel:
    def __init__(self):
        self.model = load_model('sample_model.h5')

    def prediction(self, frame):
        frame = cv2.resize(frame, (299, 299))
        frame = np.expand_dims(frame, axis=0)
        frame = frame / 255

        predictions = self.model.predict(frame)

        # return most probable Engagement Label
        return np.argmax(predictions[1][0])