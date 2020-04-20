def validate(folder, files):
    for fileName in files:
        if fileName.lower().endswith(".html"):
            try:
                file = open(fileName, "r")
                for line in file.readlines():
                    hasMeta = "<meta" in line and "viewport" in line
                    if hasMeta:
                        return "Meta-data for viewport exists in html\n"
            except Exception as _:
                return "HTML file could not be read; Might have meta-data\n"
            finally:
                file.close()
    return "No meta-data found\n"