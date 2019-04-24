# fontforge-svg-importer

![Illustration of what fontforge-svg-importer does](illustration.png)

A tool to easily import SVGs into an existing FontForge file.

## Installing

1. Install FontForge CLI
    * On Mac OS, install [Brew], then run `brew install fontforge`
    
[Brew]: https://brew.sh/

## Command-Line Usage

```
./fontforge-svg-importer sfd_input_filename sfd_output_filename svg_file ...
```

## Python Version

FontForge will use the default python interpreter on launch. Because of this,
the script is written in Python 2.7, which is the default on the Mac.
Contributions to support Python 3.x are welcome.
