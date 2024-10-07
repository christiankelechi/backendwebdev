import cv2
import requests

cap = cv2.VideoCapture(0)  # Use the default camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Encode frame to send to the backend API
    _, buffer = cv2.imencode('.jpg', frame)
    
    # Send image to backend for processing
    response = requests.post("http://127.0.0.1:8000/detect_humans/", files={"file": buffer.tobytes()})

    if response.status_code == 200:
        data = response.json()
        # Overlay bounding boxes on the frame
        for detection in data['detections']:
            x, y, w, h = detection['bbox']
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Human Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Display the processed frame
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()