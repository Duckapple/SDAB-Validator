import os
def validate(folder, files):
    result = ""
    for typeName in ["html", "css", "js"]:
        found = False
        dotType = "." + typeName
        for file in files:
            if file.lower().endswith(dotType):
                found = True
        if not found:
            result += "Does not contain any file of type " + typeName + "\n"
    if len(result) == 0:
        return "There is at least one HTML, JS and CSS file\n"
    else:
        return result