--Hurdle4--
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    if front_is_clear():
        move()
--Maze--
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
