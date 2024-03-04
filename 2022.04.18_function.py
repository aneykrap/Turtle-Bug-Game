#53

import turtle as t

def key_up():
    t.setheading(90)
    t.forward(10)

def key_down():
    t.setheading(270)
    t.forward(10)

def key_left():
    t.setheading(180)
    t.forward(10)

def key_right():
    t.setheading(0)
    t.forward(10)

def clear():
    t.clear()

def set_red():
    t.color('red')

def set_green():
    t.color('green')

def set_blue():
    t.color('blue')



t.shape('turtle')
t.onkeypress(key_up,'Up')
t.onkeypress(key_down,'Down')
t.onkeypress(key_left,'Left')
t.onkeypress(key_right,'Right')

t.onkeypress(clear,'space')
t.onkeypress(set_red,'r')
t.onkeypress(set_blue,'b')
t.onkeypress(set_green,'g')

t.listen()


t.mainloop()