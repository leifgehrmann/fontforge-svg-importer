from os import path


class SvgImporter:

    def __init__(self):
        self.remove_overlap = True
        self.import_outlines_flags = 'correctdir'
        pass

    def get_glyph_for_svg(self, font, filename):
        char_code = self._get_char_code_from_svg(filename)
        return font.create_char(char_code)

    @staticmethod
    def _get_char_code_from_svg(filename):
        char = path.splitext(path.basename(filename))[0]
        return ord(char)

    def import_outlines_from_svg(self, glyph, filename):
        glyph.importOutlines(filename, self.import_outlines_flags)

        if self.remove_overlap:
            glyph.removeOverlap()
