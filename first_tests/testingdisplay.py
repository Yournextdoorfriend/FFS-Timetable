import board, digitalio, adafruit_mpr121, busio, time, displayio, rgbmatrix, framebufferio
import adafruit_imageload, terminalio, random
import adafruit_display_text.label


displayio.release_displays()
matrix = rgbmatrix.RGBMatrix(
    width=64, bit_depth=2,
    rgb_pins=[board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5],
    addr_pins=[board.GP6, board.GP7, board.GP8, board.GP9],
    clock_pin=board.GP10, latch_pin=board.GP12, output_enable_pin=board.GP13)
display = framebufferio.FramebufferDisplay(matrix)


i2c = busio.I2C(board.GP17, board.GP16)
touch_pad = adafruit_mpr121.MPR121(i2c)


def scroll(line):
    line.x = line.x - 1
    line_width = line.bounding_box[2]
    if line.x < -line_width:
        line.x = display.width


def reverse_scroll(line):
    line.x = line.x + 1
    line_width = line.bounding_box[2]
    if line.x >= display.width:
        line.x = -line_width


def dsum(l): #Gets the sum of the dummy list, if 0 then the display is black
    nreturn = 0
    for i in l:
        nreturn = nreturn + i
    return nreturn


SCALE = 1
b1 = displayio.Bitmap(display.width//SCALE, display.height//SCALE, 2)
b2 = displayio.Bitmap(display.width//SCALE, display.height//SCALE, 2)
palette = displayio.Palette(2)
tg1 = displayio.TileGrid(b1, pixel_shader=palette)
tg2 = displayio.TileGrid(b2, pixel_shader=palette)
g1 = displayio.Group(scale=SCALE)
g1.append(tg1)
display.show(g1)
g2 = displayio.Group(scale=SCALE)
g2.append(tg2)


#A list of bmp filenames I used
x = time.time()
dummy = [0, 0, 0, 0, 0]
firsttimeconway = True
newpress = True
lastindex = 0 #Used as a counter in the slideshow below
while True: #Because the Pico is a simpler board, you need to hold down on the cap touch sensors until your input is registered
    y = time.time()
    matrix.brightness = dsum(dummy)
    
    scrollert = time.time()
    line1 = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=0xff0000,
        text="CircuitPython")
    line1.x = display.width
    line1.y = 8
    line2 = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=0x0080ff,
        text="On RP Pico")
    line2.x = display.width
    line2.y = 24
    g = displayio.Group()
    g.append(line1)
    g.append(line2)
    display.show(g)
    while time.time() < scrollert + 5:
        scroll(line1)
        reverse_scroll(line2)
        display.refresh(minimum_frames_per_second=0)