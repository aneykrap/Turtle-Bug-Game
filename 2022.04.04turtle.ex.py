import time
import turtle as t


s_width = 800
s_height = 800
t.speed(0)
t.setup(s_width,s_height)
t.penup()
t.goto(-s_width/4,0)
t.pendown()
t.color('blue')
t.begin_fill()
#직사각형1

t.forward(s_width/2) 
t.left(90)  
t.forward(s_width/8)
t.left(90)
t.forward(s_width/2) 
t.left(90)  
t.forward(s_width/8)
t.left(90)

t.end_fill()

#직사각형2
t.penup()
t.goto(-s_width/2,0)
t.pendown()
t.color('blue')
t.begin_fill()
t.forward(s_width) 
t.right(90)  
t.forward(s_width/4)
t.right(90)
t.forward(s_width) 
t.right(90)  
t.forward(s_width/4)
t.right(90)
t.end_fill()

t.penup()
t.goto(-s_width/4,-s_height/4)
t.pendown()
t.color('black')
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(s_width/4,-s_height/4)
t.pendown()
t.color('black')
t.begin_fill()
t.circle(50)
t.end_fill()

t.mainloop()