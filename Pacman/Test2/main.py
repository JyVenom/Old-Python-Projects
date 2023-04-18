from random import choice
from turtle import *
from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, -100)
wait = 0
hasGone = False
ghosts = [
    [vector(-180, 140), vector(0, -5)],
    [vector(-180, -180), vector(5, 0)],
    [vector(140, -180), vector(0, 5)],
    [vector(140, 140), vector(-5, 0)],
]
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]


def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


def move():
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    autorun()

    ontimer(move, 30)

def go_to(vp):
    global hasGone

    close_enough = False
    if abs(pacman.x - vp.x) < 5 and abs(pacman.y - vp.y) < 5:
        close_enough = True

    if not hasGone:
        if valid(pacman + vector(-5, 0)):
            aim.x = -5
            aim.y = 0

    if not close_enough and pacman.x < vp.x:
        hasGone = True
        if not close_enough and pacman.y < vp.y:
            if valid(pacman + vector(0, 5)):
                aim.x = 0
                aim.y = 5

        elif not close_enough and pacman.y > vp.y:
            if valid(pacman + vector(0, -5)):
                aim.x = 0
                aim.y = -5

        elif not close_enough and valid(pacman + vector(5, 0)):
            aim.x = 5
            aim.y = 0

    # elif pacman.x > vp.x:
    #     hasGone = True
    #     if pacman.y < vp.y:
    #         if valid(pacman + vector(0, 5)):
    #             aim.x = 0
    #             aim.y = 5
    #
    #     elif pacman.y > vp.y:
    #         if valid(pacman + vector(0, -5)):
    #             aim.x = 0
    #             aim.y = 5
    #
    #     while valid(pacman + vector(-5, 0)):
    #         if pacman.y < vp.y:
    #             if valid(pacman + vector(0, 5)):
    #                 aim.x = 0
    #                 aim.y = 5
    #         elif pacman.y > vp.y:
    #             if valid(pacman + vector(0, -5)):
    #                 aim.x = 0
    #                 aim.y = 5
    #         else:
    #             aim.x = -5
    #             aim.y = 0

def autorun():
    for point in ghosts:
        global wait
        # if abs((pacman - point[0]).x) < 20 and abs((pacman - point[0]).y) < 20:
        #     wait = 0
        #     dif = (pacman - point[0]).x
        #     if valid(pacman + vector(-5, 0)):
        #         if dif < 0:
        #             aim.x = -5
        #             aim.y = 0
        #     elif valid(pacman + vector(0, -5)):
        #         if dif < 0:
        #             aim.x = 0
        #             aim.y = -5
        #     elif valid(pacman + vector(5, 0)):
        #         if dif > 0:
        #             aim.x = 5
        #             aim.y = 0
        #     elif valid(pacman + vector(0, 5)):
        #         if dif > 0:
        #             aim.x = 0
        #             aim.y = 5

        dist = 45

        iswall = False
        if (abs((pacman - point[0]).x) <= dist) and (abs((pacman - point[0]).y) <= dist):
            if pacman.x - point[0].x > 0:
                if not valid(pacman + vector(-5, 0)):
                    iswall = True

        if pacman.x - point[0].x < 0:
            if not valid(pacman + vector(5, 0)):
                iswall = True

        if pacman.y - point[0].y > 0:
            if not valid(pacman + vector(0, -5)):
                iswall = True

        if pacman.y - point[0].y < 0:
            if not valid(pacman + vector(0, 5)):
                iswall = True

        if (abs((pacman - point[0]).x) <= dist) and (abs((pacman - point[0]).y) <= dist) and not iswall:
            wait = 0
            ran = False
            if point[1].y == 0 and point[0].y != pacman.y:
                if not ran:
                    if valid(pacman + vector(-point[1].x, -point[1].y)):
                        if abs(((pacman + vector(point[1].y, point[1].x)) - point[0]).x) > abs(
                                (pacman - point[0]).x) or abs(
                            ((pacman + vector(point[1].y, point[1].x)) - point[0]).y) > abs((pacman - point[0]).y):
                            aim.x = -point[1].x
                            aim.y = -point[1].y
                            ran = True
            if pacman.y == point[0].y:
                if not ran:
                    if valid(pacman + vector(point[1].y, point[1].x)):
                        if abs(((pacman + vector(point[1].y, point[1].x)) - point[0]).x) > abs(
                                (pacman - point[0]).x) or abs(
                            ((pacman + vector(point[1].y, point[1].x)) - point[0]).y) > abs((pacman - point[0]).y):
                            aim.x = point[1].y
                            aim.y = point[1].x
                            ran = True

                if not ran:
                    if valid(pacman + vector(-point[1].y, -point[1].x)):
                        if abs(((pacman + vector(point[1].y, point[1].x)) - point[0]).x) > abs(
                                (pacman - point[0]).x) or abs(
                            ((pacman + vector(point[1].y, point[1].x)) - point[0]).y) > abs((pacman - point[0]).y):
                            aim.x = -point[1].y
                            aim.y = -point[1].x
                            ran = True

                if not ran:
                    if valid(pacman + point[1]):
                        if abs(((pacman + vector(point[1].y, point[1].x)) - point[0]).x) > abs(
                                (pacman - point[0]).x) or abs(
                            ((pacman + vector(point[1].y, point[1].x)) - point[0]).y) > abs((pacman - point[0]).y):
                            aim.x = point[1].x
                            aim.y = point[1].y

            if pacman.y != point[0].y:
                if not ran:
                    if valid(pacman + point[1]):
                        if abs(((pacman + vector(point[1].y, point[1].x)) - point[0]).x) > abs(
                                (pacman - point[0]).x) or abs(
                            ((pacman + vector(point[1].y, point[1].x)) - point[0]).y) > abs((pacman - point[0]).y):
                            aim.x = point[1].x
                            aim.y = point[1].y
                            ran = True

                if not ran:
                    if valid(pacman + vector(point[1].y, point[1].x)):
                        if abs(((pacman + vector(point[1].y, point[1].x)) - point[0]).x) > abs(
                                (pacman - point[0]).x) or abs(
                            ((pacman + vector(point[1].y, point[1].x)) - point[0]).y) > abs((pacman - point[0]).y):
                            aim.x = point[1].y
                            aim.y = point[1].x
                            ran = True

                if not ran:
                    if valid(pacman + vector(-point[1].y, -point[1].x)):
                        if abs(((pacman + vector(point[1].y, point[1].x)) - point[0]).x) > abs(
                                (pacman - point[0]).x) or abs(
                            ((pacman + vector(point[1].y, point[1].x)) - point[0]).y) > abs((pacman - point[0]).y):
                            aim.x = -point[1].y
                            aim.y = -point[1].x

        # elif wait == 128:
        #     if valid(pacman + vector(-5, 0)):
        #         aim.x = -5
        #         aim.y = 0
        #     elif valid(pacman + vector(0, -5)):
        #         aim.x = 0
        #         aim.y = -5
        #     elif valid(pacman + vector(5, 0)):
        #         aim.x = 5
        #         aim.y = 0
        #     elif valid(pacman + vector(0, 5)):
        #         aim.x = 0
        #         aim.y = 5
        #     wait = 0
        #
        # else:
        #     wait += 1
        x = 0
        y = 0
        for point in ghosts:
            x += point[0].x
            y += point[0].y
        else:
            # go_to(vector(-180, 140))
            go_to(vector(x/4, y/4))

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
autorun()
done()
