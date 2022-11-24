# NEOPIXEL kittenbot2

import neopixel, board, time

num_pixels = 4
neo = neopixel.NeoPixel(board.P16, num_pixels, brightness=0.4, auto_write=False)

def pixel(a):
    for b in range(num_pixels):
        if a == b:
            neo[b] = (255,0,0)
        else:
            neo[b] = (0,0,0)
    neo.show()
    time.sleep(0.04)

while True:
    for a in range(num_pixels):
        pixel(a)
    for a in range(num_pixels, 0, -1):
        pixel(a)
