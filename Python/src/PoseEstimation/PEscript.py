from PoseEstimation import *
import sys


if __name__ == "__main__":
    _src = sys.argv[1]
    pe = PoseEstimator(src=_src)

    print(pe.getTrackedPose())

