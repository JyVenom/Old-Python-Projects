from turtle import *
import time
from random import *
from tkinter import *

speed(0)
def mj(x, y):
    return x, y

def crtanje2(x, y):
    global pon
    global m
    global klik
    global tocnih
    pon += 1
    klik += 1
    for i in range(20):
        if x >= unutar[i][0] and x <= unutar[i][0]+100 and y <= unutar[i][1]+100 and y >= unutar[i][1]:
            pu()
            goto(unutar[i][0]+50, unutar[i][1]+25)
            pd()
            rj = l.index(i)
            rj2 = l.index(i)
            if rj % 2 != 0:
                rj -= 1
            crtanje(rj, boja[rj//2])
            m[1-pon%2] = rj2
            break
    if pon % 2 == 0 and pon != 0 and m[0] != -101 and m[1] != -100 and abs(m[0]-m[1]) != 1 or abs(m[0]-m[1]) == 1 and min(m[0], m[1]) % 2 != 0:
        tracer(True)
        time.sleep(1)
        tracer(False)
        pu()
        goto(unutar[l[m[0]]][0]+1, unutar[l[m[0]]][1]+1)
        pd()
        pencolor('white')
        fillcolor('white')
        begin_fill()
        for i in range(4):
             fd(98)
             lt(90)
        end_fill()
        pu()
        goto(unutar[l[m[1]]][0]+1, unutar[l[m[1]]][1]+1)
        pd()
        pencolor('white')
        fillcolor('white')
        begin_fill()
        for i in range(4):
            fd(98)
            lt(90)
        end_fill()
    if abs(m[0]-m[1]) == 1 and min(m[0], m[1]) % 2 == 0:
        tocnih += 1
    if pon % 2 == 0:
        m = [-101, -100]
    pencolor('black')
    if tocnih == 10:
        import sys; sys.exit('\n----------------------\nSolved in {} steps!\n----------------------'.format(pon//2))
    return


def tablica():
    hideturtle()
    pu()
    goto(-250, 100)
    pd()
    for i in range(20):
        if i % 5 == 0 and i != 0:
            bk(500)
            rt(90)
            fd(100)
            lt(90)
        kvadrat()
        fd(100)

def kvadrat():
    for i in range(4):
        fd(100)
        lt(90)

def pravokutnik():
    pu()
    bk(25)
    lt(90)
    fd(12.5)
    rt(90)
    pd()
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(50)
        else:
            fd(25)
        lt(90)

def zvijezda():
    pu()
    lt(90)
    fd(37.5)
    lt(90)
    fd(25)
    rt(180)
    pd()
    begin_fill()
    for i in range(5):
        fd(50)
        rt(144)

def paralelogram():
    pu()
    lt(90)
    fd(12.5)
    rt(90)
    pd()
    for i in range(4):
        if i % 2 == 0:
            fd(25)
            lt(140)
        else:
            fd(25)
            lt(40)

def trapez():
    pu()
    lt(90)
    fd(12.5)
    rt(90)
    bk(17.5)
    pd()
    begin_fill()
    fd(50)
    lt(140)
    fd(25)
    lt(40)
    fd(25)
    lt(40)
    fd(25)
    lt(140)
    fd(25)

def polukrug():
    pu()
    fd(25)
    lt(90)
    fd(12.5)
    pd()
    begin_fill()
    circle(25, extent = 180)
    lt(90)
    fd(50)

def crtanje(br, boja):
    fillcolor(boja)
    if br == 0:
        begin_fill()
        circle(25, steps = 4)
    elif br == 2:
        begin_fill()
        circle(25)
    elif br == 4:
        begin_fill()
        circle(25, steps = 3)
    elif br == 6:
        pravokutnik()
    elif br == 8:
        pu()
        bk(20)
        lt(90)
        fd(12.5)
        rt(90)
        pd()
        rt(45)
        begin_fill()
        circle(25, steps = 4)
        lt(45)
    elif br == 10:
        pu()
        bk(20)
        lt(90)
        fd(20)
        rt(90)
        pd()
        begin_fill()
        for i in range(5):
            circle(5)
            pu()
            fd(10)
            pd()
    elif br == 12:
        zvijezda()
    elif br == 14:
        begin_fill()
        paralelogram()
    elif br == 16:
        trapez()
    else:
        polukrug()
    end_fill()

tracer(False)
l = sample(range(0, 20), 20)
tablica()
colormode(255)
boja = []
for i in range(0, 20, 2):
    boja.append((randint(0, 255), randint(0, 255), randint(0, 255)))
    for j in range(i, i+2):
        pu()
        goto(-200+((l[j]%5)*100), 125-((l[j]//5)*100))
        pd()
        crtanje(i, boja[i//2])
tracer(True)
time.sleep(10)
reset()
tracer(False)
tablica()
unutar = [(-250, 100), (-150, 100), (-50, 100), (50, 100), (150, 100), (-250, 0), (-150, 0), (-50, 0), (50, 0), (150, 0), (-250, -100), (-150, -100), (-50, -100), (50, -100), (150, -100), (-250, -200), (-150, -200), (-50, -200), (50, -200), (150, -200)]
tocno = 0
tracer(True)
tracer(False)
pon = 0
tocnih = 0
m = [-101, -100]
klik = 0
poz = onscreenclick(crtanje2)
mainloop()
