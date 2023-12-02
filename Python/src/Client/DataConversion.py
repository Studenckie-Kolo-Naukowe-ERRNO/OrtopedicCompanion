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
