from PoseEstimation import *
from Client import *
import cv2
import warnings
import numpy as np

SEPERATOR = '|'


def convertData(arr: np.array) -> str:
    result = ""
    rows, cols = arr.shape

    for i in range(rows):
        for j in range(cols):
            result += str(arr[i, j]) + SEPERATOR
    return result


if __name__ == "__main__":
    est = PoseEstimator()
    client = ClientServer()
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera, you can change it based on your camera index

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            warnings.warn("Error: Could not read frame.")
            break

        data = est.getTrackedPose(frame)
        if data is not np.array([1, 1]):
            #print(convertData(data))
            client.sendData(convertData(data))


    # brute force kill the process mommy
