from PIL import Image, ImageColor

class ImageCreator():
    def __init__(self, size: tuple = (25,25), color: str  = "white") -> None:
        self.draw_canvans = Image.new(mode='P', size=size, color=color)

        
    def draw_pixel(self, color: str, position: tuple[int, int] | list[tuple[int, int]]) -> None:
        if isinstance(position, list[tuple]):
            for pos in position:
                self.draw_canvans.putpixel(pos, ImageColor.getcolor(color, 'P'))
        else:
            self.draw_canvans.putpixel(position, ImageColor.getcolor(color, 'P'))

    def save_image(self, file_name: str = 'simpelPixel.png') -> None:
        self.draw_canvans.save(file_name)
