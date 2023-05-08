from PIL import Image, ImageColor

class ImageCreator():
    def __init__(self, size: tuple = (25,25), color: str  = "white") -> None:
        self.draw_canvans = Image.new(mode='P', size=size, color=color)

        
    def draw_pixel(self, color: str, position: tuple) -> None:
        self.draw_canvans.putpixel(position, ImageColor.getcolor(color, 'P'))

    def save_image(self) -> None:
        self.draw_canvans.save('simplePixel.png')

