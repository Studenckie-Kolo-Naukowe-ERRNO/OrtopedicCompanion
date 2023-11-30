import sys

import Client
import PoseEstimation


def main():
    client = Client()
    estimator = PoseEstimation(0)


if __name__ == "__main__":
    main()
    sys.exit(1)
