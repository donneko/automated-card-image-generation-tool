import math

def calcCordNumber(configCards):
    cordNumber = configCards["columns"] * configCards["rows"]
    return cordNumber

def calcPageNumber(dataLength,cordNumber):

    tmpTh = dataLength / cordNumber
    return math.ceil(tmpTh)

def calcPosition(x,y,configCards):

    widthGap = configCards["width"] + configCards["gap_x"]
    heightGap = configCards["height"] + configCards["gap_y"]

    return (
    configCards["start_x"] + widthGap * x,
    configCards["start_y"] + heightGap * y
    )

