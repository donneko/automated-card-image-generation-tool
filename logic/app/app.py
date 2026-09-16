from PIL import Image, ImageDraw
from logic.calc.calc import calcCordNumber,calcPageNumber,calcPosition
from logic.service.cord_print import cordPrint
from logic.service.get_json import getConfig,getInputData
from logic.service.save_pages import savePages
from logic.service.setup import setupPrintConfig

def app():
    config = getConfig()
    data = getInputData(config["input"]["data"])

    printDataBook = setupPrintConfig(config["prints"])
    cordNumber = calcCordNumber(config["cards"])
    dataLength = len(data)
    template = Image.open(config["input"]["template"])

    pages = []

    for page in range(calcPageNumber(dataLength,cordNumber)):
        startCard = page * cordNumber

        image = template.copy()
        draw = ImageDraw.Draw(image)

        columns = config["cards"]["columns"]

        for x in range(columns):
            for y in range(config["cards"]["rows"]):
                index = startCard + x * columns + y


                if index >= dataLength:
                    break

                position = calcPosition(x,y,config["cards"])
                cordPrint(draw,printDataBook,data[index],position)

        pages.append(image)


    savePages(pages,config["output"])