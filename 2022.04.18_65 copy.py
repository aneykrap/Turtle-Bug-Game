import turtle as t
import random as r
from unittest.main import MAIN_EXAMPLES

t.title('turtle race')

s_width = 800
s_height = 600

min_x= -s_width/2
min_y= -s_height/2
max_x= s_width/2
max_y= s_height/2

start_x= min_x + 30
start_y = max_y -50

t.setup(s_width,s_height)
t.speed(0)
t.hideturtle()

#############################################
# 함수명 :draw_line
#(x1,y1)->(x2,y2)까지 선분그리기 함수
# n : 숫자(화면에 n을 씀)
#############################################

def draw_line(x1,y1,x2,y2,pen_color='white',pen_size=5):
    t.penup()
    t.pensize(pen_size)
    t.goto(x1,y1)
    t.pencolor(pen_color)
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

# 선수별 트랙그리기
draw_polygon(min_x+30,max_y-50,\
             min_x+30,min_y+50,\
             max_x-30,min_y+50,\
             max_x-30,max_y-50,
             'darkblue')

for i in range(s_height//100-2):
    draw_line(min_x+30,start_y-(100*(i+1)),max_x-30,start_y-(100*(i+1)))

#출발선과 도착선 그리기

draw_line(min_x+50,max_y-50,min_x+50,min_y+50,'white',2)
draw_line(max_x-50,max_y-50,max_x-50,min_y+50,'white',2)


# 선수 등장 시키기

p_color = ['white','yellow','pink','cyan','orange'] #거북이 색
players = []  #거북이 선수가 담길 리스트


for i in range(len(p_color)):
    p = t.Turtle()
    p.penup()
    p.color(p_color[i]) #색상 정의 
    p.shape('turtle')
    p.goto(min_x+40,max_y-100-100*i)
    players.append(p)

# 선수 달리기 시작
goal_line = max_x-50
goal_tag = False
while True :
    for p in players:
        d = r.randint(1,10)
        p.forward(d)

        if p.xcor() > goal_line:
            goal_tag = True
            p.shapesize(10)

    if goal_tag :
        break


t.mainloop()