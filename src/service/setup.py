import importlib

def setup(scripts):
    dataBook = {}

    for script in scripts:

        module = importlib.import_module(script["script"])

        printData = module.setup(script["config"])
        printData["__module_print__"] = module.print

        dataBook[script["key"]] = printData

    return dataBook