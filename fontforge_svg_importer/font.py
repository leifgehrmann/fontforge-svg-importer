import fontforge


class Font:

    def __init__(self, fontforge_font):
        self.font = fontforge_font
        pass

    @classmethod
    def open_sfd(cls, filename):
        return Font(fontforge.open(filename))

    def save_sfd(self, filename):
        self.font.save(filename)

    def create_char(self, char_code):
        return self.font.createChar(char_code)
