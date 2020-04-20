def validate(folder, files):
    for fileName in files:
        if fileName.lower().endswith(".html"):
            file = open(fileName, "r")
            for line in file.readlines():
                hasLink = "<link" in line and "stylesheet" in line
                isReset = "reset" in line.lower() or "normalize" in line.lower()
                if hasLink and isReset:
                    return "Reset.css is referrenced in html\n"
        elif fileName.lower().endswith(".css"):
            if "reset" in fileName.lower() or "normalize" in fileName.lower():
                return "Reset.css or nomalize.css is included as a file\n"
    return "No reset.css is imported\n"
