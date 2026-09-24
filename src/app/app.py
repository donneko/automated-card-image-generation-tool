from PIL import Image, ImageDraw
from src.calc.calc import calcCordNumber,calcPageNumber,calcPosition
from src.service.cord_print import cordPrint
from src.service.get_json import getConfig,getInputData
from src.service.save_pages import savePages
from src.service.setup import setup
from src.service.create_data import createData

def app():
    config = getConfig()
    data = getInputData(config["input"]["data"])

    dataBook = setup(config["scripts"])
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

                meta = createData(x,y,index,config["cards"])
                cordPrint(draw,dataBook,data[index],meta)

        pages.append(image)


    savePages(pages,config["output"])