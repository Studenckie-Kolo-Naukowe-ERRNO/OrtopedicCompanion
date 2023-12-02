from PoseEstimation import *
from Client.Client import *

import cv2
import warnings
import numpy as np
import cv2

class VideoCaptureApp:
    def __init__(self):
        # Create a window
        cv2.namedWindow("Video Capture with Trackbars")
        self.pointer = 0
        # Create trackbars
        cv2.createTrackbar("Val", "Video Capture with Trackbars", 0, 15, self.event_ptr)
            # first value is blue, BGR format!
        self.colors = [(255,0,0), (0,255,0), (0,0,255)]
    def event_ptr(self, value):
        self.pointer = value

    def update(self, frame, array):
        # Get trackbar values
        self.pointer = cv2.getTrackbarPos("Val", "Video Capture with Trackbars")
        
        # draw
        for i in range(0, 16):
            center = (int(array[i][0]), int(array[i][1]))

            print(center)
            cv2.circle(frame, center, 4, self.colors[0], 2)
        
        cv2.imshow("Video Capture with Trackbars", frame)

        key = cv2.waitKey(10)
        if key == 27:  # ESC key
            self.vid.release()
            cv2.destroyAllWindows()
SEPERATOR = '|'

EMPTY_ARRY = numpy.array([[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]])
EMPTY_ARRY_STR = "1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0|1.0"


def convertData(arr: np.array) -> str:
    result = ""
    try:
        rows, cols = arr.shape
    except:
        return "1.0|1.0|"

    for i in range(rows):
        for j in range(cols):
            result += str(arr[i, j]) + SEPERATOR
    return result


def main():
    print("Script started.")
    app = VideoCaptureApp()


    est = PoseEstimator()
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera, you can change it based on your camera index

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            warnings.warn("Error: Could not read frame.")
            break
        

        data = est.getTrackedPose(frame)
        if data is not EMPTY_ARRY:
            print(convertData(data))
            app.update(frame, data)

if __name__ == "__main__":
    main()

