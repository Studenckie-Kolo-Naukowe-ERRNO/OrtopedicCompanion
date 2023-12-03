import numpy

SEPERATOR = '|'

EMPTY_ARRY = numpy.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]])


def convertData(arr: numpy.array) -> str:
    result = ""
    try:
        rows, cols = arr.shape
    except:
        return convertData(EMPTY_ARRY)

    for i in range(rows):
        for j in range(cols):
            result += str(arr[i, j]) + SEPERATOR
    return result
