import cv2

def capture_face():
    # Start webcam capture
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()  # Read a frame from the webcam

        if not ret:
            print("Failed to grab frame.")
            break

        # Convert the frame to grayscale (face detection requires it)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Load OpenCV's pre-trained Haar Cascade for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw rectangle around face

        # Display the resulting frame with detected faces
        cv2.imshow("Webcam - Press 'q' to quit", frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Release the webcam
    cv2.destroyAllWindows()  # Close any OpenCV windows

if __name__ == "__main__":
    capture_face()
