import time
import turtle as t
s_width = 800
s_height = 600

t.setup(s_width,s_height)
#기준점
cx,cy = 0,0
#자동차의 큰 사각형
s_x = cx - 300
s_y = 0
t.penup()
t.goto(s_x,s_y)
t.begin_fill()
t.fillcolor('darkblue')
t.down()
t.goto(s_x,s_y-150)
t.goto(s_x+600,s_y-150)
t.goto(s_x+600,0)
t.goto(s_x,s_y)
t.end_fill()

#자동차의 작은 사각형
s_x = cx - 200
s_y = 0
t.penup()
t.goto(s_x,s_y)
t.begin_fill()
t.fillcolor('darkblue')
t.down()
t.goto(s_x,s_y+100)
t.goto(s_x+400,s_y+100)
t.goto(cx+400,0)
t.goto(s_x,s_y)
t.end_fill()

r=70
t.penup()
t.goto(cx-200,-150-r)
t.down()
t.begin_fill()
t.circle(r)
t.end_fill()
t.end

t.mainloop()