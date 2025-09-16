from pico2d import *

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

x=0
y=0
direction = 'right'

while True:
    clear_canvas()
    grass.draw(400, 30)



    character.draw(x+10, y+90)
    update_canvas()
    delay(0.01)

close_canvas()