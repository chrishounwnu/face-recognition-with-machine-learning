import cv2
import os
import numpy as np
from deepface import DeepFace

def detect_and_align_face(image_path, save_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error loading image: {image_path}")
        return False
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) == 0:
        print(f"No face detected in {image_path}")
        return False
    
    for (x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        face = cv2.resize(face, (160, 160))  # Resize for model compatibility
        cv2.imwrite(save_path, face)
        print(f"Processed image saved as {save_path}")
        return True
    
    return False

def process_dataset(dataset_folder, processed_folder):
    if not os.path.exists(processed_folder):
        os.makedirs(processed_folder)
    
    for filename in os.listdir(dataset_folder):
        img_path = os.path.join(dataset_folder, filename)
        save_path = os.path.join(processed_folder, filename)
        detect_and_align_face(img_path, save_path)

if __name__ == "__main__":
    detect_and_align_face("captured.jpg", "processed.jpg")
    process_dataset("dataset/", "processed_dataset/")
