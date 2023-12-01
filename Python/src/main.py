from PoseEstimation import *
from Client.Client import *

import cv2
import warnings
import numpy as np

SEPERATOR = '|'


def convertData(arr: np.array) -> str:
    result = ""
    try:
        rows, cols = arr.shape
    except:
        return "1.0|1.0"

    for i in range(rows):
        for j in range(cols):
            result += str(arr[i, j]) + SEPERATOR
    return result


def main():
    print("Script started.")

    est = PoseEstimator()
    cli = ClientServer()
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera, you can change it based on your camera index

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            warnings.warn("Error: Could not read frame.")
            break

        data = est.getTrackedPose(frame)
        if data is not numpy.array([1.0, 1.0]):
            print(convertData(data))
            cli.sendData(convertData(data))


if __name__ == "__main__":
    main()

