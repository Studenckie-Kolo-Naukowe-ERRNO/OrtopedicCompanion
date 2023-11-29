from ultralytics import YOLO
import torch
import warnings
import math
import numpy

class PoseEstimator:
    def __init__(self, src=0):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        if self.device == 'cpu':
            warnings.warn("The model will be using the *CPU*, instead of the CUDA.")

        # check if file exists @TODO
        self.model = YOLO('yolov8m-pose.pt')
        self.model.to(self.device)

        self.conv = 0.3
        self.source = src

        # what is the start position, left or right?
        self.trackedPose = [0, 0]

    def __estimateAllPoses(self) -> list:
        return self.model(source=self.source, show=False, conf=self.conv, save=False)

    def getTrackedPose(self) -> numpy.ndarray:
        result = self.__estimateAllPoses()
        index = 0
        minDistance = 10000

        for res in result:
            # tensor to ndarray
            persons = res.keypoints.xy.cpu().numpy()

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

