import math
import numpy

from ultralytics import YOLO
import torch

import os
import warnings

MODEL_PATH = "yolov8m-pose.pt"

EMPTY_ARRY = numpy.array([[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]])


class PoseEstimator:
    def __init__(self, src=0):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        if self.device == 'cpu':
            warnings.warn("The model will be using the *CPU*, instead of the CUDA.")

        # check if model is downloaded
        if os.path.exists(MODEL_PATH):
            # @TODO
            self.model = YOLO(MODEL_PATH)
        else:
            self.model = YOLO(MODEL_PATH)

        self.model.to(self.device)

        self.conv = 0.3
        self.source = src

        # The left side is the start position
        self.trackedPose = [0, 0]

    def __estimateAllPoses(self, frame: numpy.ndarray) -> list:
        return self.model(source=frame, show=False, conf=self.conv, save=False)

    def getTrackedPose(self, frame: numpy.ndarray) -> numpy.ndarray:
        result = self.__estimateAllPoses(frame)
        index = 0
        minDistance = 10000

        for res in result:
            # tensor to ndarray
            persons = res.keypoints.xy.cpu().numpy()

            try:
                persons[index][0]
            except:
                # nothing was detected
                return EMPTY_ARRY

            # if there is only one person detected, just return it
            if len(persons) <= 1:
                self.trackedPose = persons[index][0]
                return persons[0]

            for i, person in enumerate(persons):
                distance = math.dist(self.trackedPose, person[0])
                if distance > minDistance:
                    minDistance = distance
                    index = i

            self.trackedPose = persons[index][0]
            # if there is more than one person, return the closest one to the firstly detected
            return persons[index]

