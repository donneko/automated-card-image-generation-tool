from logic.service.draw_print import drawPrint

def cordPrint(draw,printDataBook,data,position):
    for key, value in data.items():

        if not (key in printDataBook):
            print(f"key: {key} が存在しません。")
            break

        printData = printDataBook[key]

        drawPrint(draw,{
            "font":printData["font"],
            "position":(
                position[0] + printData["x"],
                position[1] + printData["y"]
                ),
            "text":value,
            "color":printData["color"]
        })




