# Quick benchmark of clearing a displayio Bitmap using for loops

# See https://github.com/adafruit/circuitpython/issues/2688

import time
import board, displayio

WIDTH = 240
HEIGHT = 240

display = board.DISPLAY

# eight colours is 3 bits per pixel when packed
bitmap = displayio.Bitmap(WIDTH, HEIGHT, 8)

palette = displayio.Palette(8)
palette[0] = 0x000000
palette[1] = 0xff0000
palette[2] = 0x00ff00
palette[3] = 0x0000ff

tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
group = displayio.Group()
group.append(tile_grid)

display.auto_refresh=False
display.show(group)

def refresh_screen(disp):
    while True:
        refreshed = False
        try:
            refreshed = disp.refresh(minimum_frames_per_second=0)
        except Exception:
            pass
        if refreshed:
            break

def fillscreen1(bmp, col_idx):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            bmp[x, y] = col_idx

def fillscreen2(bmp, col_idx):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            bmp[x, y] = col_idx

def fillscreen3(bmp, col_idx):
    for idx in range(WIDTH * HEIGHT):
        bmp[idx] = col_idx

# "Big" Python has a timeit library but not present on CircuitPython
# so it's time for some for loops
for func in (fillscreen1, fillscreen2, fillscreen3):
    for _ in range(2):
        for colour_idx in (0, 0, 0, 1, 2, 3):
            t1 = time.monotonic_ns()
            func(bitmap, colour_idx)
            refresh_screen(display)
            t2 = time.monotonic_ns()
            func_name = str(func).split(" ")[1]
            print(func_name,
                  colour_idx,
                  "{:.3f}s".format((t2 - t1) / 1e9))
            time.sleep(0.5)

