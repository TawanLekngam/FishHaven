from PySide6.QtGui import QFont


def get_font(font_name: str, font_size: int, bold: bool = False, italic: bool = False) -> QFont:
    font = QFont(font_name)
    font.setPixelSize(font_size)
    font.setBold(bold)
    font.setItalic(italic)
    return font
