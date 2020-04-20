def validate(folder, files):
    pseudoClasses = []
    for fileName in files:
        if fileName.lower().endswith(".css"):
            try:
                file = open(fileName, "r")
                for line in file.readlines():
                    for type in [":hover",":focus",":visited",":active",":not",":root",":checked"]:
                        if type in line and type not in pseudoClasses:
                            pseudoClasses.append(type)
            except Exception as _:
                return "CSS file could not be read; Might be using pseudo-classes\n"
            finally:
                file.close()
    if len(pseudoClasses) == 0:
        return "No pseudo classes used\n"
    else:
        return "Pseudo-classes used: " + ", ".join(pseudoClasses) + "\n"
