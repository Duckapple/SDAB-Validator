def validate(folder, files):
    try:
        for fileName in files:
            if fileName.lower().endswith(".html"):
                file = open(fileName, "r")
                for line in file.readlines():
                    # Step 1: check for <link>
                    hasLink = "<link" in line and ("fonts.google" in line or "font" in line)
                    # Step 2: check for @import
                    hasAtImport = "@import" in line and "fonts.google" in line
                    # Step 3: check for @font-face
                    hasFontFace = "@font-face" in line
                    if hasLink or hasAtImport or hasFontFace:
                        return "A font is imported via Google Fonts or similar\n"
            elif fileName.lower().endswith(".css"):
                file = open(fileName, "r")
                for line in file.readlines():
                    # Step 2: check for @import
                    hasAtImport = "@import" in line and "fonts.google" in line
                    # Step 3: check for @font-face
                    hasFontFace = "@font-face" in line
                    if hasAtImport or hasFontFace:
                        return "A font is imported in CSS via Google Fonts or similar\n"
        return "No font is imported\n"
    except Exception as _:
        return "Something went wrong in checking this assignment for font import\n"
    finally:
        file.close()
