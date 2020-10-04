import pyxel
import math

pyxel.init(200, 200)

ballx = 100
bally = 0
angle = math.radians(30)
vx = math.cos(angle)
vy = math.sin(angle)
padx = 100


def update():
    global ballx, bally, angle, vx, vy, padx
    ballx += vx
    bally += vy
    if ballx >= 200 or ballx <= 0:
        vx *= -1
    padx = pyxel.mouse_x


def draw():
    global ballx, bally, angle, vx, vy, padx
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx - 20, 195, 40, 5, 14)


pyxel.run(update, draw)
