from PIL import ImageFont

def setupPrintConfig(prints):
    printDataBook = {}

    for printConfig in prints:


        font = ImageFont.truetype(
            printConfig["font"],
            int(printConfig["size"])
        )


        printDataBook[printConfig["key"]] = {
            "x":int(printConfig["x"]),
            "y":int(printConfig["y"]),
            "color":printConfig["color"],
            "font":font
        }

    return printDataBook