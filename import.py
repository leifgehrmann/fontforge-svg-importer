import sys
import fontforge

font_filename = sys.argv[:-1]
font = fontforge.open(font_filename)

# select all imported charatcers, thhen apply a "remove overlap" call
imported_charatcers = []
font.selection.

font.save(font_filename)

print("Hello World")
print("The arguments are: " , str(sys.argv))
print(sys.version_info)
