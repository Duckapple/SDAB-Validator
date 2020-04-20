#!/usr/bin/env python3
import os, glob, zipfile, patoolib
from shutil import rmtree
from validators import filetypes, fontimport, validate, viewport, pseudo, resetcss

validators = [
    filetypes,
    fontimport,
    resetcss,
    pseudo,
    viewport,
    validate,
]

# Setup input 
if not (os.path.isdir("./input") and os.path.exists("./input")):
    for file in glob.iglob("./*.zip"):
        zip_ref = zipfile.ZipFile(file, "r")
        zip_ref.extractall("./input")
        zip_ref.close()
for type in ["zip","rar"]:
    for file in glob.iglob("./input/**/*.{}".format(type)):
        directory = "/".join(file.split("/")[:-1]) + "/"
        patoolib.extract_archive(file, outdir=directory)
        os.remove(file)
for dir in glob.iglob("./input/**/__MACOSX"):
    rmtree(dir, ignore_errors=True)

# Create output folder
if not os.path.isdir("./out/files"):
    os.makedirs("./out/files")

# Validate and save validation
for folder in glob.iglob("./input/*"):
    result = ""
    files = []
    for location, _, filelist in os.walk(folder):
        for file in filelist:
            files.append(os.path.join(location, file))
    for validator in validators:
        result += validator.validate(folder, files)
    file = open("./out/files/" + folder.split("/")[-1] + ".md", "w")
    file.write(result)
    file.close()

# Make output zip
with zipfile.ZipFile("./out/result.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    for file in glob.iglob("./out/files/*.md"):
        zipf.write(file)