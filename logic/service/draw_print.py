def drawPrint(draw,printData):
    draw.text(
        printData["position"],
        printData["text"],
        font=printData["font"],
        fill=printData["color"]
    )

