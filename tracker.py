import cv2
import mediapipe as mp
import math

LEFT_EYE = [33, 133, 159, 145, 153, 154, 155]
RIGHT_EYE = [362, 263, 386, 374, 380, 381, 382]

class EyeTracker:
    def __init__(self):
        mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
    def get_landmark(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)
        h, w, _ = frame.shape
        if not results.multi_face_landmarks:
            return None, None
        face_landmarks = results.multi_face_landmarks[0]
        left_eye = [(int(face_landmarks.landmark[idx].x * w), int(face_landmarks.landmark[idx].y * h)) for idx in LEFT_EYE]
        right_eye = [(int(face_landmarks.landmark[idx].x * w), int(face_landmarks.landmark.landmark[idx].y * h)) for idx in RIGHT_EYE]
        return left_eye, right_eye
    def draw_eyes(self, frame, left_eye, right_eye):
        for (x, y) in left_eye + right_eye:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)  
    # bagian EAR
    def euclidean_distance(self, p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    
    def eye_aspect_ratio(self, eye):
        A = self.euclidean_distance(eye[1], eye[5])
        B = self.euclidean_distance(eye[2], eye[4])
        C = self.euclidean_distance(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear