# fontforge-svg-importer

> **This is still Work In Progress.** You'll notice that the code does not do
anything yet.

A tool to easily import SVGs into an existing FontForge file.

The tool will be capable of running post processing commands such as:

* Merge overlapping polygons

## Installing

1. Install FontForge CLI

## Command-Line Usage

```
fontforge -lang=py -script import.py svg_file ... sfd_file
```

## Python Version

FontForge will use the default python interpreter on launch. Because of this,
the script is written in Python 2.7, which is the default on the Mac.
Contributions to support Python 3.x are welcome.
