import cv2
import logging
from tracker import EyeTracker
from detection import DrowsyDetector

# Setup logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def main():
    cap = cv2.VideoCapture(0)
    tracker = EyeTracker()
    detector = DrowsyDetector()

    logging.info("Session started")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        left_eye, right_eye = tracker.get_landmark(frame)
        if left_eye and right_eye:
            tracker.draw_eyes(frame, left_eye, right_eye)

            left_ear = tracker.eye_aspect_ratio(left_eye)
            right_ear = tracker.eye_aspect_ratio(right_eye)
            ear = (left_ear + right_ear) / 2.0

            sleepy = detector.update(ear)
            if sleepy:
                logging.warning("Drowsiness detected!")

        cv2.imshow("Drowsy Alert", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    logging.info("Session ended")

if __name__ == "__main__":
    main()
