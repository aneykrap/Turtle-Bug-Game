#58
from decimal import MIN_ETINY
from pyexpat.errors import XML_ERROR_UNKNOWN_ENCODING
import turtle as t
from unittest.main import MAIN_EXAMPLES

t.title('세로선 그리기 연습')

s_width = 1000
s_height = 600

min_x= -s_width/2
min_y= -s_height/2
max_x= s_width/2
max_y= s_height/2

t.setup(s_width,s_height)

def draw_line(x1,y1,x2,y2,n=0):
    t.penup()
    t.goto(x1,y1)
    t.write(str(n))
    t.pendown()
    t.goto(x2,y2)
    t.penup()

start_x= min_x + 50
start_y = max_y -50


# draw_line(start_x,start_y,start_x,min_y+50)
# draw_line(start_x,start_y,start_x,min_y+50)

for i in range(s_width//100):
    draw_line(start_x+100*i,start_y,start_x+100*i,min_y+50,i+1)
    
t.mainloop()