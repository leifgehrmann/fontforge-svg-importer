import sys
from fontforge_svg_importer import Font, SvgImporter

input_sfd_filename = sys.argv[1]
output_sfd_filename = sys.argv[2]
svg_filenames = sys.argv[3:]

font = Font.open_sfd(input_sfd_filename)
importer = SvgImporter()

glyph_count = 0
for svg_filename in svg_filenames:
    glyph = importer.get_glyph_for_svg(font, svg_filename)
    importer.import_outlines_from_svg(glyph, svg_filename)
    glyph_count += 1

font.save_sfd(output_sfd_filename)

print("")
print("Successfully imported %d glyphs: '%s'" % (glyph_count, output_sfd_filename))
print("")
