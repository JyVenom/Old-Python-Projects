# EXAMPLE FOR A PLATFORM GAME USING THE TURTLE
#
# This is a simple platform (jump 'n' run) game with a Super Mario 
# figurine. Use the arrow keys to control the figure and jump from
# platform to platform.
#
# Apr-18-2014
#
# (c) 2014, Tobias Kohn
# http://jython.tobiaskohn.ch/
#
from turtle import *
from time import sleep

# Change these values to adapt to your screen
SCREEN_LEFT = -400
SCREEN_RIGHT = -SCREEN_LEFT
SCREEN_TOP = 300
SCREEN_BOTTOM = -SCREEN_TOP

# Here you can design your level!
# Each platform comprises three numbers: x_left, x_right, height(y)
PLATFORMS = [(-280, -200, 36),
             (-150, 30, 45),
             (60, 165, 60),
             (-200, -44, 100),
             (6, 288, 120),
             (50, 90, 150),
             (-100, 30, 180),
             (-250, -190, 210),
             (-80, 250, 270),
             (-350, -150, 320),
             (280, 350, 330),
             (-120, -10, 360)]
# Specify the coordinates and radius of the goal to reach
GOAL = (50, 400, 30)

# Change these values to influence (key) control
KEYSPEED = 6
MAXSPEED = 15
JUMPSPEED = 12
JUMPFACTOR = 1.5
GRAVITY = -1.25
DAMPING = 0.75
JUMPDAMPING = 0.95
LOOPDELAY = 0.1

# Do not change these!
LEFT = -1
RIGHT = 1
GROUNDLEVEL = SCREEN_BOTTOM + 36

BREAK = False   # Used to terminate the program
MARIO_HEIGHT = 7
MARIO_WIDTH = 8

# The position and speed of Mario itself
pos_x = SCREEN_LEFT + 10
pos_y = GROUNDLEVEL
speed_x = 0
speed_y = 0
direction = 0   # Currently not used

def bound(x, min_x, max_x):
    """Return the x-value, bounded to the given min and max."""
    return min(max(x, min_x), max_x)

def update():
    """Update the turtle's position."""
    global pos_x, pos_y, speed_x, speed_y
    # Update the current speed (y)
    gl = getGroundLevel(pos_x, pos_y)
    if gl < pos_y or speed_y > 0:
        speed_y = bound(speed_y + GRAVITY, -MAXSPEED, MAXSPEED)
    else:
        speed_y = 0
    # Update the current speed (x)
    if speed_x != 0:
        if speed_y == 0:
            speed_x = bound(speed_x * DAMPING, -MAXSPEED, MAXSPEED)
        else:
            speed_x = bound(speed_x * JUMPDAMPING, -MAXSPEED, MAXSPEED)
        if -0.5 < speed_x < 0.5:
            speed_x = 0
    # Update the position
    if speed_x != 0 or speed_y != 0:
        pos_x = bound(pos_x + speed_x, SCREEN_LEFT, SCREEN_RIGHT)
        pos_y = bound(pos_y + speed_y, gl, SCREEN_TOP)
        setPos(pos_x, pos_y + MARIO_HEIGHT)

def setSpeed(speedX=None, speedY=None):
    """Set the character's speed and direction.
       Use 'None' to keep the current speed."""
    global speed_x, speed_y, direction
    if speedX != None:
        speed_x = speedX
    if speedY != None:
        speed_y = speedY
    if speed_x >= 0:
        d = RIGHT
    else:
        d = LEFT

def getGroundLevel(x, y):
    """Return the ground-level for the given coordinate."""
    result = GROUNDLEVEL
    mw = MARIO_WIDTH // 2
    for x_left, x_right, height in PLATFORMS:
        if x_left-mw <= x <= x_right+mw:
            gl = GROUNDLEVEL + height
            if y >= gl and gl > result:
                result = gl
    return result

def goalReached():
    """Check if the goal has been reached."""
    goal_x, goal_y, radius = GOAL
    delta_x = (pos_x - goal_x) ** 2
    delta_y = (pos_y - (goal_y+GROUNDLEVEL)) ** 2
    return ((delta_x + delta_y) <= (radius ** 2))

def fillRectangle(x1, y1, x2, y2):
    """Draw a filled rectangle using the current pencolor."""
    setPos(x1, y1)
    fillToPoint()
    for p in [(x1, y2), (x2, y2), (x2, y1), (x1, y1)]:
        moveTo(p)
    fillOff()

def paintPlatforms():
    """Paint all the platforms Mario can stand on."""
    penWidth(6)
    setPenColor(makeColor("chocolate"))
    for x_left, x_right, height in PLATFORMS:
        y = GROUNDLEVEL + height - 3
        setPos(x_left, y)
        moveTo(x_right, y)

def paintGoal():
    """Paint the goal to reach."""
    goal_x, goal_y, radius = GOAL
    setPenColor(makeColor("gold"))
    setPos(goal_x, goal_y + GROUNDLEVEL)
    dot(radius)
    setPenColor("black")
    dot(radius * 3 // 4)

def paintScene():
    """Paint the entire scene/background."""
    clear(makeColor("sky blue"))
    setPenColor(makeColor("forest green"))
    fillRectangle(SCREEN_LEFT, GROUNDLEVEL, SCREEN_RIGHT, SCREEN_BOTTOM)
    paintPlatforms()
    paintGoal()
    penUp()

def onKeyPressed(code):
    """React to a pressed key."""
    global speed_x, speed_y, BREAK
    if code == 37:   # LEFT
        if speed_y == 0:
            speed_x += LEFT * KEYSPEED
    elif code == 38: # UP
        if speed_y == 0:
            speed_y = max(JUMPSPEED, JUMPFACTOR * abs(speed_x))
    elif code == 39: # RIGHT
        if speed_y == 0:
            speed_x += RIGHT * KEYSPEED
    elif code == 27:
        BREAK = True

### MAIN ###

# Setup:
makeTurtle("sprites/mario.png", keyPressed=onKeyPressed)
hideTurtle()
paintScene()
moveTo(pos_x, pos_y + MARIO_HEIGHT)
setSpeed(None, None)
showTurtle()
heading(0)

#Run loop:
while 1 :
    sleep(LOOPDELAY)
    if BREAK or isDisposed():
        break
    update()
    if goalReached():
        msgDlg("Congratulations! You won!")
        break

# Close the window:
dispose()

### END PROGRAM ###
