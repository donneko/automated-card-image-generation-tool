
def saveSomePage(pages,setting):

    pagesLength = len(pages)
    digits = len(str(pagesLength))

    for i in range(pagesLength):

        fileNumber = "" if pagesLength < 1 else f"_{str(i).zfill(digits)}"

        page = pages[i]
        page.save(
            f"{setting["path"]}{fileNumber}.{setting["format"].lower()}",
            setting["format"],
            resolution=setting["dpi"]
        )

def saveOnePage(pages,setting):

    pages[0].save(
        f"{setting["path"]}.{setting["format"].lower()}",
        setting["format"],
        save_all=True,
        append_images=pages[1:],
        resolution=setting["dpi"]
    )

def savePages(pages,outputConfig):

    setting = {
        "path":f"{outputConfig["directory"]}/{outputConfig["name_template"]}",
        "format":outputConfig["format"],
        "dpi":outputConfig["dpi"]
    }

    if outputConfig["save_one_page"].lower() == "true":
        saveOnePage(pages,setting)
    else:
        saveSomePage(pages,setting)
