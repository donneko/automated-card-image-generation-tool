
def cordPrint(draw,dataBook,data,meta):
    for key, value in data.items():
        meta["value"] = value

        if not (key in dataBook):
            print(f"key: {key} が存在しません。")
            break

        printData = dataBook[key]
        printData["__module_print__"](draw,printData,meta)





