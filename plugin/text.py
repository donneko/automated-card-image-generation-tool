from PIL import ImageFont

def setup(config):
    font = ImageFont.truetype(
        config["font"],
        int(config["size"])
    )

    return {
            "x":int(config["x"]),
            "y":int(config["y"]),
            "color":config["color"],
            "font":font
        }

def print(draw,config,meta):

    draw.text(
        (
            meta["position"][0] + config["x"],
            meta["position"][1] + config["y"]
        ),
        meta["value"],
        font=config["font"],
        fill=config["color"]
    )