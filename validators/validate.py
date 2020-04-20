from tidylib import tidy_document
def validate(folder, files):
    for fileName in files:
        if fileName.lower().endswith(".html"):
            try:
                file = open(fileName, "r")
                filetext = "".join([s for s in file.readlines()])
                _, errors = tidy_document(filetext, options={"numeric-entities":1})
                if len(errors) == 0:
                    return "HTML was successfully validated with no errors\n"
                return "HTML was validated, with following errors:\n  - " + errors.replace("\n", "\n  - ").strip("  - ")
            except Exception as _:
                return "An error occured while validating html file\n"
            finally:
                file.close()