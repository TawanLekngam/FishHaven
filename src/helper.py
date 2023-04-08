from pygame import Surface
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QSize, Qt


def surface_to_pixmap(surface: Surface) -> QPixmap:
    new_surface = surface.copy()
    size = QSize(100, 100)
    image = QImage(new_surface.get_buffer(), new_surface.get_width(),
                   new_surface.get_height(), QImage.Format_RGB32)
    pixmap = QPixmap.fromImage(image)
    pixmap = pixmap.scaled(size, Qt.KeepAspectRatio,
                           Qt.SmoothTransformation)
    return pixmap
