import cv2
import os
import json
from deepface import DeepFace

DATASET_DIR = "dataset"
INFO_FILE = "dataset_info.json"

# Charger les informations des utilisateurs
def load_user_info():
    if os.path.exists(INFO_FILE):
        with open(INFO_FILE, "r") as f:
            return json.load(f)
    return {}

# Fonction pour reconnaître le visage en live
def recognize_face():
    cap = cv2.VideoCapture(0)
    user_info = load_user_info()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Sauvegarde temporaire de l'image capturée
        cv2.imwrite("temp.jpg", frame)

        try:
            # Comparer avec toutes les images du dataset
            for filename in os.listdir(DATASET_DIR):
                img_path = os.path.join(DATASET_DIR, filename)
                
                result = DeepFace.verify("temp.jpg", img_path, model_name="Facenet", enforce_detection=False)
                
                if result["verified"]:
                    username = filename.split(".")[0]  # Récupérer le nom depuis le fichier
                    details = user_info.get(username, {})
                    name = details.get("name", username)
                    age = details.get("age", "Unknown")
                    
                    cv2.putText(frame, f"Name: {name}, Age: {age}", (50, 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                    print(f"Recognized: {name}, Age: {age}")
                    break
            else:
                cv2.putText(frame, "Unknown Face", (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        except Exception as e:
            print(f"Error: {e}")

        cv2.imshow("Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_face()
