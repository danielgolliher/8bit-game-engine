"""Generate og-image.png — the social-preview image for 8bit.danielgolliher.com.
Run: python3 og-image-gen.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630

# colors from the midnight theme
BG       = (10, 10, 31)
TILE     = (26, 26, 58)
TILE_DOT = (68, 68, 170)
ACCENT   = (255, 204, 0)
ACCENT2  = (255, 68, 136)
TEXT     = (255, 255, 255)
MUTED    = (181, 181, 214)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Tile grid background — matches the arena look in-game.
TS = 40
for y in range(0, H, TS):
    draw.line([(0, y), (W, y)], fill=TILE, width=2)
for x in range(0, W, TS):
    draw.line([(x, 0), (x, H)], fill=TILE, width=2)
for y in range(TS // 2, H, TS):
    for x in range(TS // 2, W, TS):
        draw.rectangle([x - 1, y - 1, x + 1, y + 1], fill=TILE_DOT)


def draw_sprite(grid, palette, px, py, scale):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c in palette:
                draw.rectangle(
                    [px + x * scale, py + y * scale,
                     px + (x + 1) * scale - 1, py + (y + 1) * scale - 1],
                    fill=palette[c],
                )


KNIGHT = [
    "............",
    "....1111....",
    "...111111...",
    "...122211...",
    "...111111...",
    "..11111111..",
    ".1111111111.",
    ".1322222231.",
    ".1111111111.",
    "..11....11..",
    "..33....33..",
    "..3......33.",
]
KNIGHT_PAL = {"1": (200, 200, 208), "2": (255, 170, 68), "3": (34, 34, 51)}

SLIME = [
    "............",
    "...111111...",
    "..11111111..",
    ".1122222211.",
    ".1122222211.",
    ".1111111111.",
    ".1111111111.",
    ".1111111111.",
    ".1111111111.",
    "..11111111..",
    "...111111...",
    "............",
]
SLIME_PAL = {"1": (85, 204, 85), "2": (170, 255, 170)}

SKELETON = [
    "....1111....",
    "...111111...",
    "...122221...",
    "..11222211..",
    "...122221...",
    "....1111....",
    "..11111111..",
    ".1111111111.",
    "..11111111..",
    "...1....1...",
    "..11....11..",
    ".11......11.",
]
SKELETON_PAL = {"1": (238, 238, 216), "2": (68, 68, 68)}

BAT = [
    "............",
    ".11......11.",
    "111......111",
    ".111....111.",
    "..11111111..",
    "..12222221..",
    "...111111...",
    "....1..1....",
    "............",
    "............",
    "............",
    "............",
]
BAT_PAL = {"1": (85, 51, 119), "2": (34, 17, 51)}

MENLO = "/System/Library/Fonts/Menlo.ttc"
title_font = ImageFont.truetype(MENLO, 96, index=1)   # Bold
tag_font   = ImageFont.truetype(MENLO, 30)
url_font   = ImageFont.truetype(MENLO, 22)

cx = W // 2

# Title with drop shadow.
title = "8-BIT GAME MAKER"
draw.text((cx + 4, 110 + 4), title, font=title_font, fill=(0, 0, 0), anchor="mm")
draw.text((cx, 110), title, font=title_font, fill=ACCENT, anchor="mm")

# Top divider (pixel dashes).
for x in range(120, W - 120, 10):
    draw.rectangle([x, 182, x + 5, 186], fill=ACCENT2)

# Scene row: hero + projectile + enemies.
scale = 14
draw_sprite(KNIGHT, KNIGHT_PAL, 180, 240, scale)
# magical projectile trail between hero and first enemy
for i in range(4):
    px = 370 + i * 26
    py = 318
    s = 10 - i * 2
    draw.rectangle([px, py, px + s, py + s], fill=ACCENT)
draw_sprite(SLIME,    SLIME_PAL,    540, 240, scale)
draw_sprite(SKELETON, SKELETON_PAL, 760, 240, scale)
draw_sprite(BAT,      BAT_PAL,      980, 250, scale)

# Bottom divider.
for x in range(120, W - 120, 10):
    draw.rectangle([x, 452, x + 5, 456], fill=ACCENT2)

# Tagline.
tagline = "Pick a hero. Pick an enemy. Pick a weapon. Make a game."
draw.text((cx, 500), tagline, font=tag_font, fill=TEXT, anchor="mm")

# URL.
url = "8bit.danielgolliher.com"
draw.text((cx, 560), url, font=url_font, fill=ACCENT, anchor="mm")

img.save("og-image.png", "PNG", optimize=True)
print(f"saved og-image.png ({img.size[0]}x{img.size[1]})")
