# 😴 Drowsy Alert

Drowsy Alert adalah program sederhana untuk mendeteksi kantuk melalui kamera dengan memantau mata.  
Program ini menggunakan **MediaPipe FaceMesh** untuk melacak wajah, menghitung **Eye Aspect Ratio (EAR)**, dan menyalakan alarm jika mata terpejam terlalu lama.

##
Customize alarmnya dengan ganti alarm.wav dengan suara apapun yang kamu inginkan

## 🚀 Cara Menjalankan

1. Clone / download project ini  
2. Buat virtual environment dan install dependensi:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```
3. Untuk jalankan run:
   ```
   python3 main.py
   ```
   
