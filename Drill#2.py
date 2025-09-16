from pico2d import *

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

x=400
y=90
angle = 3*math.pi/2
radius = 200
middle_x = 400
middle_y = 300

right=False
up=True
circle_move=False

while True:
    clear_canvas()
    grass.draw(400, 30)
    if circle_move==False:
        if right==False and up==True:
            x += 2
            if x >= 780:
                x = 780
                right=True
            elif x ==400:
                x=400
                circle_move=True

        elif up==True and right==True:
            y += 2
            if y>= 560:
                y = 560
                up=False

        elif right==True and up==False:
            x -= 2
            if x <= 20:
                x = 20
                right=False

        elif right==False and up==False:
            y -= 2
            if y <= 90:
                y = 90
                up=True

    elif circle_move==True:
        x = middle_x + radius * math.cos(angle)
        y = middle_y + radius * math.sin(angle)-10
        angle-=0.03
        if angle<=-math.pi/2:
            angle=3*math.pi/2
            circle_move=False


    character.draw(x, y)
    update_canvas()
    delay(0.01)

close_canvas()
