from src.calc.calc import calcPosition

def createData(x,y,i,configCards):

    position = calcPosition(x,y,configCards)

    return {
        "position":position,
        "index":i,
        "x":x,
        "y":y
    }