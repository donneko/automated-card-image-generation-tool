def savePages(pages,outputConfig):


    pages[0].save(
        f"{outputConfig["directory"]}/out-image.{outputConfig["format"]}",
        outputConfig["format"],
        save_all=True,
        append_images=pages[1:],
        resolution=300
    )