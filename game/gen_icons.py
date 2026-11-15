"""Иконки 16x16 для оружия, предметов и артефактов."""
import os
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, 'icons')
os.makedirs(OUT, exist_ok=True)

def new():
    return Image.new('RGBA', (16, 16), (0, 0, 0, 0))

def px(im, x, y, c):
    if c is None:
        return
    if 0 <= x < 16 and 0 <= y < 16:
        im.putpixel((int(x), int(y)), c)

def rect(im, x0, y0, x1, y1, c):
    for y in range(int(y0), int(y1) + 1):
        for x in range(int(x0), int(x1) + 1):
            px(im, x, y, c)

def line(im, x0, y0, x1, y1, c):
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx, sy = (1 if x0 < x1 else -1), (1 if y0 < y1 else -1)
    err = dx - dy
    while True:
        px(im, x0, y0, c)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy; x0 += sx
        if e2 < dx:
            err += dx; y0 += sy

def circle(im, cx, cy, r, c, fill=True):
    for y in range(-r, r + 1):
        for x in range(-r, r + 1):
            d = (x*x + y*y) ** .5
            if (fill and d <= r) or (not fill and abs(d - r) < .7):
                px(im, cx + x, cy + y, c)

def save(im, name):
    im.save(os.path.join(OUT, name + '.png'))

def C(h, a=255):
    h = h.lstrip('#')
    return (int(h[0:2],16), int(h[2:4],16), int(h[4:6],16), a)

GREY = C('#8b98a6'); BLUE = C('#4aa3ff'); PURPLE = C('#b06bff')
GOLD = C('#ffb340'); WHITE = C('#e2e9ef'); DARK = C('#0b0d0f')
RED = C('#e8574a'); GREEN = C('#5fd39b'); CYAN = C('#8ef0ff')

# ---------------- оружие ----------------
def gun(barrel, color, grip=True, scope=False, drum=False, twin=False):
    im = new()
    def one(ox):
        rect(im, ox+2, 7, ox+2+barrel, 9, color)
        rect(im, ox+2, 9, ox+4, 12, DARK if not grip else color)
        px(im, ox+2+barrel, 8, WHITE)
        if scope: rect(im, ox+5, 5, ox+8, 6, color)
        if drum: circle(im, ox+5, 11, 2, color)
    one(1)
    if twin: one(8)
    return im

icons = {}
icons['pistol']   = gun(6, GREY)
icons['dual']     = gun(4, GREY, twin=True)
icons['smg']      = gun(7, C('#9fb0be'), drum=True)
icons['shocker']  = gun(5, CYAN, drum=True)
icons['shotgun']  = gun(10, C('#c9a06a'))
icons['minigun']  = gun(8, C('#b8c4d0'), drum=True)
icons['sniper']   = gun(12, C('#6f8a4a'), scope=True)
icons['rocket']   = gun(8, C('#c0392b'), drum=True)
icons['grenade']  = gun(5, C('#8a6a3a'), drum=True)
icons['plasma']   = gun(6, PURPLE, drum=True)
icons['cryo']     = gun(6, CYAN)
icons['railgun']  = gun(11, BLUE, scope=True)
icons['laser']    = gun(9, GREEN)

# оживляем: у лазера луч
line(icons['laser'], 1, 4, 10, 4, GREEN)
line(icons['railgun'], 2, 3, 12, 3, BLUE)

# ---------------- предметы ----------------
im = new(); circle(im, 8, 8, 6, C('#1a1f24'))
for a in [(0,0),(3,0),(-3,0),(0,3),(0,-3)]:
    px(im, 8+a[0], 8+a[1], GOLD)
icons['rate'] = im

im = new(); line(im, 8, 2, 8, 13, WHITE); line(im, 3, 7, 13, 7, WHITE)
line(im, 5, 4, 11, 4, WHITE); line(im, 5, 10, 11, 10, WHITE)
icons['dmg'] = im

im = new()
rect(im, 5, 2, 8, 10, C('#4a7bd1'))
rect(im, 3, 11, 10, 13, C('#35588f'))
line(im, 3, 13, 5, 13, WHITE)
icons['speed'] = im

im = new()
rect(im, 3, 4, 6, 7, RED); rect(im, 9, 4, 12, 7, RED)
rect(im, 3, 6, 12, 9, RED); rect(im, 5, 9, 10, 10, RED)
rect(im, 6, 11, 9, 11, RED)
icons['hp'] = im

im = new()
line(im, 2, 4, 13, 4, WHITE); line(im, 2, 8, 13, 8, WHITE); line(im, 2, 12, 13, 12, WHITE)
rect(im, 12, 2, 13, 5, BLUE); rect(im, 12, 6, 13, 9, BLUE); rect(im, 12, 10, 13, 13, BLUE)
icons['pierce'] = im

im = new()
for p in [(8,1),(13,8),(8,14),(2,8),(5,4),(11,4),(5,12),(11,12)]:
    rect(im, p[0]-1, p[1]-1, p[0]+1, p[1]+1, GOLD)
icons['crit'] = im

im = new()
rect(im, 4, 3, 11, 6, C('#7fb2d9')); rect(im, 3, 6, 12, 11, C('#5f8fb8'))
rect(im, 4, 11, 11, 13, C('#4a6f90'))
icons['armor'] = im

im = new()
rect(im, 3, 3, 5, 12, RED); rect(im, 10, 3, 12, 12, BLUE)
icons['magnet'] = im

im = new()
rect(im, 6, 3, 9, 12, GREEN); rect(im, 4, 6, 11, 9, GREEN)
icons['regen'] = im

im = new()
rect(im, 4, 5, 11, 12, RED); rect(im, 6, 2, 9, 5, RED)
px(im, 6, 7, DARK); px(im, 9, 7, DARK)
icons['vamp'] = im

im = new()
for i in range(4):
    line(im, 3+i, 2, 8+i, 13, CYAN)
    line(im, 12-i, 2, 7-i, 13, CYAN)
icons['slow'] = im

im = new()
circle(im, 8, 8, 5, C('#7ec24a'))
px(im, 6, 6, DARK); px(im, 10, 6, DARK)
rect(im, 6, 10, 9, 10, DARK)
icons['poison'] = im

im = new()
rect(im, 2, 6, 13, 9, GOLD); px(im, 14, 8, WHITE); px(im, 1, 8, WHITE)
icons['multi'] = im

im = new()
for i in range(5):
    line(im, 3, 13-i*3, 13, 3+i, C('#b06bff'))
icons['thorns'] = im

im = new()
circle(im, 8, 8, 3, WHITE); line(im, 8, 2, 8, 5, GREY); line(im, 8, 11, 8, 14, GREY)
icons['knock'] = im

im = new()
circle(im, 8, 8, 6, None, fill=False)
for p in [(8,2),(14,8),(8,14),(2,8)]:
    circle(im, p[0], p[1], 1, GREEN)
icons['orb'] = im

im = new()
rect(im, 7, 2, 9, 13, C('#7fb2d9')); rect(im, 5, 4, 11, 10, C('#5f8fb8'))
icons['shield'] = im

im = new()
line(im, 3, 13, 12, 3, WHITE); line(im, 3, 3, 12, 13, WHITE)
line(im, 2, 12, 12, 12, BLUE)
icons['ricochet'] = im

im = new()
circle(im, 8, 8, 5, None, fill=False)
circle(im, 8, 8, 2, RED)
line(im, 8, 8, 13, 3, GOLD)
icons['homing'] = im

im = new()
circle(im, 8, 9, 5, GOLD)
for p in [(8,2),(4,4),(12,4),(3,8),(13,8)]:
    px(im, p[0], p[1], C('#fff3c4'))
icons['boom'] = im

im = new()
rect(im, 3, 6, 12, 10, RED); rect(im, 5, 9, 10, 11, C('#8a2b20'))
px(im, 13, 8, WHITE)
icons['bigshot'] = im

# ---------------- артефакты ----------------
im = new()
rect(im, 3, 4, 6, 7, C('#ff6b5a')); rect(im, 9, 4, 12, 7, C('#ff6b5a'))
rect(im, 3, 6, 12, 9, C('#c0392b')); rect(im, 5, 9, 10, 10, C('#c0392b'))
px(im, 4, 5, C('#ffd0c0'))
icons['a_heart'] = im

im = new()
rect(im, 7, 1, 8, 11, WHITE); rect(im, 5, 11, 10, 12, GOLD)
line(im, 4, 9, 11, 9, GREY)
icons['a_blade'] = im

im = new()
circle(im, 8, 8, 6, None, fill=False)
line(im, 8, 8, 8, 4, GOLD); line(im, 8, 8, 11, 9, GOLD)
icons['a_clock'] = im

im = new()
rect(im, 3, 3, 5, 12, RED); rect(im, 10, 3, 12, 12, BLUE)
line(im, 3, 6, 5, 6, WHITE)
icons['a_mag'] = im

im = new()
rect(im, 6, 2, 9, 13, WHITE); rect(im, 4, 4, 11, 11, BLUE)
icons['a_shield'] = im

im = new()
circle(im, 8, 10, 5, GOLD)
line(im, 8, 1, 8, 6, C('#ffe9a0')); line(im, 6, 3, 6, 6, C('#ffe9a0'))
icons['a_flame'] = im

im = new()
for i in range(4):
    line(im, 3, 13-i*3, 12, 2+i, PURPLE)
icons['a_prism'] = im

im = new()
circle(im, 8, 8, 5, WHITE); circle(im, 8, 8, 2, DARK); px(im, 8, 8, RED)
icons['a_eye'] = im

im = new()
rect(im, 4, 3, 10, 10, C('#c9a06a')); rect(im, 3, 10, 12, 12, C('#8a6a3a'))
icons['a_boots'] = im

im = new()
rect(im, 3, 4, 6, 7, RED); rect(im, 9, 4, 12, 7, RED)
rect(im, 4, 7, 12, 10, RED); rect(im, 6, 10, 10, 12, C('#8a2b20'))
icons['a_vamp'] = im

im = new()
circle(im, 8, 8, 6, None, fill=False)
for p in [(8,1),(15,8),(8,15),(1,8),(8,8)]:
    circle(im, p[0], p[1], 1, GOLD)
icons['a_orbs'] = im

im = new()
circle(im, 8, 9, 5, C('#7ec24a'))
circle(im, 6, 6, 1, DARK); circle(im, 10, 6, 1, DARK)
icons['a_poison'] = im

for name, im in icons.items():
    save(im, name)

# общий лист для проверки
names = sorted(icons)
cell = 16 * 3
cols = 10
rows = (len(names) + cols - 1) // cols
sheet = Image.new('RGBA', (cols * (cell + 6), rows * (cell + 6)), (12, 14, 16, 255))
for i, n in enumerate(names):
    big = icons[n].resize((cell, cell), Image.NEAREST)
    sheet.alpha_composite(big, (6 + (i % cols) * (cell + 6), 6 + (i // cols) * (cell + 6)))
sheet.save(os.path.join(BASE, 'иконки-обзор.png'))
print('иконок:', len(icons))
