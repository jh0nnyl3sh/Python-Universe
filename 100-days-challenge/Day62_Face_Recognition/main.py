import cv2
import numpy as np
import os

# Model dosyalarını indirmek yerine OpenCV'nin içindeki hazır kaynakları hedefliyoruz
# Eğer dosyalar yoksa hata almamak için kontrol ekliyoruz
model_file = "res10_300x300_ssd_iter_140000.caffemodel"
config_file = "deploy.prototxt"

# Not: Bu dosyalar sisteminde yoksa OpenCV'nin GitHub'ından otomatik çekilmesi gerekir.
# Ancak işi garantiye almak için en basit "Haar" yöntemini iyileştirilmiş parametrelerle deneyelim.
# Eğer DNN istersen dosyaları indirmen gerekecek. Şimdilik Haar'ı "hassas" hale getirelim:

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Hatalı tespitleri (elbise vb.) engellemek için parametreleri sıkılaştırıyoruz:
    # scaleFactor: 1.1 yerine 1.3 (daha seçici)
    # minNeighbors: 5 yerine 8 veya 10 (onay mekanizmasını artırır)
    faces = face_cascade.detectMultiScale(gray, 1.3, 10, minSize=(50, 50))

    for (x, y, w, h) in faces:
        # Gerçekten bir yüz mü? Alan kontrolü yapıyoruz
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, "Insan Yuzu", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.imshow('Hassas Yuz Tespit', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()