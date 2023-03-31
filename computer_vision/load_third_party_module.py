import mediapipe as mp
import numpy as np
import cv2

class PoseDetector:
    def __init__(self, mode = False, upBody = False, smooth=True, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)

    def findPose(self, img, draw=False):
        self.results = self.pose.process(img)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS

    def getPosition(self, img, draw=False):
        lmList= []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmList

class HandDetector():
    def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        
    def findHands(self, img, draw = True):
        self.results = self.hands.process(img)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def getPosition(self, img, handNo = 0, draw = True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)
        return lmlist


class FaceMeshDetector:
    def __init__(self, static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_face_mesh = mp.solutions.face_mesh
        self.DRAWING_SPEC = self.mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
        self.face_mesh = self.mp_face_mesh.FaceMesh(static_image_mode, max_num_faces, min_detection_confidence, min_tracking_confidence)
        self.LEFT_EYE_INDICES = [466, 388, 387, 386, 385, 384, 398, 249, 390, 373, 374, 380, 381, 382, 263, 362]
        self.RIGHT_EYE_INDICES = [246, 161, 160, 159, 158, 157, 173, 7, 163, 144, 145, 153, 154, 155, 33, 133]

    def calculate_single_ear(self, eye_landmarks_np):
        upper_mean = np.mean(eye_landmarks_np[0:7], axis=0)
        lower_mean = np.mean(eye_landmarks_np[7:14], axis=0)
        return self.euclidean_distance(upper_mean, lower_mean) / self.euclidean_distance(eye_landmarks_np[14], eye_landmarks_np[15])

    def euclidean_distance(self, x, y):
        return np.linalg.norm(x - y)

    def landmarks_to_np(self, landmarks):
        landmarks = [[landmark.x, landmark.y] for landmark in landmarks]
        return np.array(landmarks)

    def find_face_mesh(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(imgRGB)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                if draw:
                    self.mp_drawing.draw_landmarks(img, face_landmarks, self.mp_face_mesh.FACEMESH_CONTOURS, landmark_drawing_spec=self.DRAWING_SPEC)

        return img, results.multi_face_landmarks

    def get_ear_and_area(self, img, face_landmarks):
        if face_landmarks is None:
            return -1, -1

        left_eye_landmarks_np = self.landmarks_to_np([face_landmarks.landmark[i] for i in self.LEFT_EYE_INDICES])
        left_ear = self.calculate_single_ear(left_eye_landmarks_np)

        right_eye_landmarks_np = self.landmarks_to_np([face_landmarks.landmark[i] for i in self.RIGHT_EYE_INDICES])
        right_ear = self.calculate_single_ear(right_eye_landmarks_np)

        h, w, c = img.shape
        cx_min, cy_min = w, h
        cx_max, cy_max = 0, 0

        for _, lm in enumerate(face_landmarks.landmark):
            cx, cy = int(lm.x * w), int(lm.y * h)
            cx_min, cy_min = min(cx, cx_min), min(cy, cy_min)
            cx_max, cy_max = max(cx, cx_max), max(cy, cy_max)

        ear = (left_ear + right_ear) / 2
        area = int((cx_max - cx_min) * (cy_max - cy_min))
        
        return ear, area


def sample_mediapipe_module(rgb, oriImg, TPImg):
    face_mesh_detector = FaceMeshDetector()
    poseDetector = PoseDetector()
    handDetector = HandDetector()

    ret_EAR = -1
    ret_Area = -1
    ret_hand = [[], []]
    ret_pose = None

    rgb.flags.writeable = False
    
    handDetector.findHands(oriImg, False)
    poseDetector.findPose(oriImg, False)
    
    _, face_landmarks = face_mesh_detector.find_face_mesh(rgb, draw=False)

    rgb.flags.writeable = True
    if face_landmarks:
        ret_EAR, ret_Area = face_mesh_detector.get_ear_and_area(rgb, face_landmarks[0])
    
    ret_pose = poseDetector.getPosition(TPImg)
    try:
        ret_hand[0] = handDetector.getPosition(TPImg, 0, draw=False)
    except:
        ret_hand[0] = []
        
    try:
        ret_hand[1] = handDetector.getPosition(TPImg, 1, draw=False)
    except:
        ret_hand[1] = []

    return ret_EAR, ret_Area, ret_hand, ret_pose
