from PoseEstimation import *
from Client.Client import *
from Client.DataConversion import *

import cv2
import warnings
import numpy as np

SEPERATOR = '|'

EMPTY_ARRY = numpy.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]])


def empty() -> numpy.ndarray:
    em = numpy.array([[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0],[1.0,1.0]])
    em *= -1
    return em


def limbsDetected(arr: numpy.ndarray) -> bool:
    LEFT_ARM_ID, RIGHT_ARM_ID = 10, 9
    LEFT_LEG_ID, RIGHT_LEG_ID = 15, 16

    return not (arr[LEFT_ARM_ID][0] == 0 or arr[RIGHT_ARM_ID][0] == 0 or arr[LEFT_LEG_ID][0] == 0 or arr[RIGHT_ARM_ID][0] == 0)


def main():
    print(empty())
    print("Script started.")

    est = PoseEstimator()
    cli = ClientServer()
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera, you can change it based on your camera index
    print("Script started video capture.")
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            warnings.warn("Error: Could not read frame.")
            break

        data = est.getTrackedPose(frame)
        if data is not EMPTY_ARRY:
            if limbsDetected(data):
                cli.sendData(convertData(data))
            else:
                cli.sendData(convertData(empty()))
        else:
            cli.sendData(convertData(empty()))


if __name__ == "__main__":
    main()

