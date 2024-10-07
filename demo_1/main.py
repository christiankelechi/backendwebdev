import cv2
import torch
import numpy as np
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

# Load the pre-trained COCO model from PyTorch (YOLOv5 or Faster R-CNN)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # YOLOv5s model

# Object Tracking variables
tracker = cv2.legacy.TrackerMOSSE_create()  # Using MOSSE tracker, but you can change this

cap = cv2.VideoCapture(0)  # Use webcam feed


def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break

        # Object Detection using the pre-trained model
        results = model(frame)

        # Convert results to NumPy array for OpenCV visualization
        labels, cord = results.xyxyn[0][:, -1].numpy(), results.xyxyn[0][:, :-1].numpy()

        # Draw bounding boxes for detected objects
        for idx, (label, box) in enumerate(zip(labels, cord)):
            start_point = (int(box[0] * frame.shape[1]), int(box[1] * frame.shape[0]))
            end_point = (int(box[2] * frame.shape[1]), int(box[3] * frame.shape[0]))

            cv2.rectangle(frame, start_point, end_point, (255, 0, 0), 2)
            cv2.putText(frame, model.names[int(label)], (start_point[0], start_point[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            # Initialize tracker with the first detected object
            if idx == 0:
                tracker.init(frame, (start_point[0], start_point[1], end_point[0] - start_point[0], end_point[1] - start_point[1]))

        # Update tracker (this will track the first detected object)
        success, track_box = tracker.update(frame)
        if success:
            p1 = (int(track_box[0]), int(track_box[1]))
            p2 = (int(track_box[0] + track_box[2]), int(track_box[1] + track_box[3]))
            cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)

        # Encode frame to JPEG for streaming
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.get("/video_feed")
def video_feed():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
