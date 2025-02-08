import cv2
import numpy as np
from deepface import DeepFace

def load_model():
    """Load the face recognition model."""
    print("Loading face recognition model...")
    return DeepFace.build_model("Facenet")  # Facenet pour les embeddings faciaux

def preprocess_image(image):
    """Convert image to grayscale and resize if needed."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.resize(gray, (160, 160))  # Taille standard pour Facenet
