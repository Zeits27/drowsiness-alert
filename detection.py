import pygame

EAR_THRESHOLD = 0.15
CONSEC_FRAMES = 20   

class DrowsyDetector:
    def __init__(self):
        self.counter = 0
        self.state = "open"
        pygame.mixer.init()
        pygame.mixer.music.load("assets/alarm.wav")

    def update(self, ear):
        print(f"EAR={ear:.3f} | Counter={self.counter} | State={self.state}")  # 👈 debug info

        if ear < EAR_THRESHOLD:
            self.counter += 1

            # Detect state change (open -> closed)
            if self.counter >= 1.5 and self.state != "closed":
                self.state = "closed"
                print("Eyes CLOSED")

            # Trigger drowsiness alarm
            if self.counter >= CONSEC_FRAMES:
                self.play_alert()
                return True

        else:
            if self.state != "open":
                self.state = "open"
                print("Eyes OPEN")

            self.counter = 0
            self.stop_alert()

        return False

    def play_alert(self):
        if not pygame.mixer.music.get_busy():
            print("🚨 Alarm Playing 🚨")
            pygame.mixer.music.play(-1)  # loop until stopped

    def stop_alert(self):
        if pygame.mixer.music.get_busy():
            print("✅ Alarm Stopped")
        pygame.mixer.music.stop()
