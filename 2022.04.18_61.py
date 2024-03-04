import turtle as t
from unittest.main import MAIN_EXAMPLES

t.title('면 그리기')

s_width = 800
s_height = 600

min_x= -s_width/2
min_y= -s_height/2
max_x= s_width/2
max_y= s_height/2

t.setup(s_width,s_height)

#############################################
# 함수명 :draw_line
#(x1,y1)->(x2,y2)까지 선분그리기 함수
# n : 숫자(화면에 n을 씀)
#############################################

def draw_line(x1,y1,x2,y2,n=0):
    t.penup()
    t.goto(x1,y1)
    t.write(str(n))
    t.pendown()
    t.goto(x2,y2)
    t.penup()

#사각형을 그리는 함수

def draw_polygon(x1,y1,x2,y2,x3,y3,x4,y4,color='white'):
    t.penup()
    t.goto(x1,y1)
    t.begin_fill()
    t.fillcolor(color)
    t.pendown()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x4,y4)
    t.goto(x1,y1)
    t.end_fill()

draw_polygon(min_x+50,max_y-50,\
             min_x+50,min_y+50,\
             max_x-50,min_y+50,\
             max_x-50,max_y-50,
             'darkblue')




t.mainloop()