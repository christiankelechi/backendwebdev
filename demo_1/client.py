import cv2
import asyncio
import requests
import aiohttp
import numpy as np

async def fetch_processed_frame(session):
    async with session.get('http://localhost:8001/video_feed') as response:
        return await response.content.read()

async def send_frame(session, frame):
    _, buffer = cv2.imencode('.jpg', frame)
    frame_bytes = buffer.tobytes()
    async with session.post('http://localhost:8001/upload_frame', files={"file": frame_bytes}) as response:
        return await response.json()

async def main():
    # Set up video capture from the webcams
    cap1 = cv2.VideoCapture(0)  # Raw video feed (left)
    cap2 = cv2.VideoCapture(1)  # Processed video feed (right)

    async with aiohttp.ClientSession() as session:
        while True:
            success1, frame1 = cap1.read()  # Capture from the first webcam
            success2, frame2 = cap2.read()  # Capture from the second webcam

            if not success1 or not success2:
                break

            # Send frame1 to the FastAPI server
            send_task = asyncio.create_task(send_frame(session, frame1))

            # Fetch the processed frame from the FastAPI server
            processed_frame = await fetch_processed_frame(session)

            # Decode the processed frame
            np_arr = np.frombuffer(processed_frame, np.uint8)
            frame2 = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            # Wait for the send_frame task to complete
            response = await send_task
            print(response)  # Print the server response

            # Create a combined frame
            combined_frame = cv2.hconcat([frame1, frame2])  # Horizontal concatenation of the two frames

            # Show the combined frames
            cv2.imshow('Webcam Stream - Raw and Processed', combined_frame)

            # Exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the captures and close windows
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    asyncio.run(main())
