# SDAB-Validator
This is a validator for the third assignment in the Systematic Design of User Interfaces course on ITU. 

It is very extensible, having the validators in separate python source files, 
so these validators can be edited or added on a whim.

## Capabilities
 - Check whether certain source file types are available
 - Check whether web-font are used
 - Check for use of :pseudo-classes in CSS
 - Check for reset.css
 - Validate HTML
 - Check for viewport meta-data
 - Import from LearnIT assignment zip file (just put in root directory of project and run `app.py`)
 - Export to markdown, with a .zipped bundle

## Usage
There are two ways to use the validator; with a .zip-file or with a directory of inputs.

The .zip-file should be of a format such that unzipping it results in a structure like the following:
```
└── zip-file
    ├── <User>
    │   └── Files to check related to user
    ...
```

The "Download all submissions" grading action on Moodle outputs a zip-file and therefore fits this structure.

When extracted by the program, the output should be like this (and this is the format you should follow if you do not have a zip-file:

```
├── input
│   ├── <User>
│   │   └── Files to check related to user
```

Output will be put in the folder `out` in the root of the project. A zip-file of the bundled validations is present, along with a directory `files` where the individual markdown files are present.
