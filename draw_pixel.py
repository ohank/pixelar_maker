from PIL import Image, ImageColor
from typing import Union

class ImageCreator():
    def __init__(self, size: tuple = (25,25), color: str  = "white") -> None:
        self._height = size[0]
        self._width = size[1]
        self.draw_canvans = Image.new(mode='P', size=size, color=color)

        
    def draw_pixel(self, color: str, position: Union[tuple, list[tuple]]) -> None:
        if isinstance(position, list):
            for pos in position:
                self.draw_canvans.putpixel(pos, ImageColor.getcolor(color, 'P'))
        else:
            self.draw_canvans.putpixel(position, ImageColor.getcolor(color, 'P'))

    def save_image(self, file_name: str = 'simpelPixel.png') -> None:
        self.draw_canvans.save(file_name)
    
    def draw_horizontal_line(self, color: str) -> None:
        self.draw_pixel(color=color, position=
                        list(zip(range(self._width),([0] * self._height))))
