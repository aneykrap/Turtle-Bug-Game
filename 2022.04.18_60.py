#60
from decimal import MIN_ETINY
from pyexpat.errors import XML_ERROR_UNKNOWN_ENCODING
import turtle as t
from unittest.main import MAIN_EXAMPLES

t.title('가로선 그리기 연습')

s_width = 800
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
     draw_line(start_x,start_y-100*i,max_x-50,start_y-100*i,i+1)

#밑에서부터 올라가기
#for i in range(s_height//100):
#    draw_line(min_x+50,min_y+50+100*i,max_x-50,min_y+50+100*i,i+1)

#오른쪽에서 왼쪽으로 
#for i in range(s_height//100):
#    draw_line(max_x-50,start_y-100*i,min_x+50,start_y-100*i,i+1)

t.mainloop()