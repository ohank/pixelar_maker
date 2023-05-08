from PIL import Image, ImageColor
from draw_pixel import ImageCreator

def test_blank_canvans() -> None:

    dut = ImageCreator()
    dut.save_image()

    im = Image.open('simplePixel.png')
    assert im.getcolors() == [(625, 0)]
    assert im.size == (25, 25)


def test_draw_color() -> None:

    dut = ImageCreator()
    dut.draw_pixel(color="red", position=(0,0))
    dut.save_image()


    im = Image.open('simplePixel.png')
    pix = im.load()
    assert im.getcolors() == [(624, 0), (1, 1)]
    assert 1 == pix[0,0]
    assert im.size == (25, 25)