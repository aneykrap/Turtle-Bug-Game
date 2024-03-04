import imp
import random as r
import turtle as t
import time as time

s_width = 800
s_height = 800
gap = 20
t.speed(0)

min_x = -s_width/2 + gap
min_y = -s_height/2 + gap
max_x = s_width/2 - gap
max_y = s_height/2 -gap

speed = 5 #플레이어의 속도
jumsu = 0

t.title('turtle bug')
t.setup(s_width,s_height)

scr = t.Screen()  #스크린 가져오기
scr.tracer(0)     #화면추적금지


def key_left():
    play.left(17)

def key_right():
    play.right(17)


#화면 설정
t.speed(0)
t.bgcolor('black')
t.penup()
t.pencolor('white')
t.pensize(10)
t.goto(min_x,max_y)
t.pendown()
t.goto(max_x,max_y)
t.goto(max_x,min_y)
t.goto(min_x,min_y)
t.goto(min_x,max_y)
t.penup()
t.hideturtle()

#플레이어 만들기

play = t.Turtle()
play.shape('turtle')
play.color('lightblue')
play.up()


t.onkeypress(key_left,'Left')
t.onkeypress(key_right,'Right')
t.listen()

# Bugs 만들기

b_cnt = 30
b_color = ['red','yellow','white','orange','cyan','grey'] #색깔주의 확인필요
b_shape = [ 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
b_size = [0.5,0.6,0.7,0.8,0.9,1]
bugs = []

for i in range(b_cnt):
    b = t.Turtle()  # 객체생성
    b.color(b_color[r.randint(0,5)])
    b.shape(b_shape[r.randint(0,5)])
    b.shapesize(b_size[r.randint(0,5)])
    b.setheading(r.randint(0,360))
    b.up()
    b.speed(2)
    b_x = r.randint(min_x,max_x)
    b_y = r.randint(min_y,max_y)
    b.goto(b_x,b_y)
    bugs.append(b)

while True :
    scr.update()
    time.sleep(0.1)
    #1 플레이어 움직
    play.forward(speed)
    p_x,p_y = play.pos()
    #print(p_x,p_y)
    #테두리 밖으로 벗어나면 플레이어 방향 변경
    if p_x < min_x or p_x > max_x or p_y < min_y or p_y >max_y :
            if p_x < min_x : play.setx(min_x)
            if p_x > max_x : play.setx(max_x)
            if p_y < min_y : play.sety(min_y)
            if p_y > max_y : play.sety(max_y)
            play.right(180)
 
    #2 벌레 움직
    for i in range(b_cnt):
        bugs[i].forward(r.randint(3,10))
        b_x,b_y = bugs[i].pos()
        #print(p_x,p_y)
        #테두리 밖으로 벗어나면 플레이어 방향 변경
        if b_x < min_x or b_x > max_x or b_y < min_y or b_y > max_y :
            if b_x < min_x : bugs[i].setx(min_x)
            if b_x > max_x : bugs[i].setx(max_x)
            if b_y < min_y : bugs[i].sety(min_y)
            if b_y > max_y : bugs[i].sety(max_y)

            bugs[i].right(180)




        # 플레이어와 만났는지 체크하기
        # 만났으면 speed +=1 , 점수 쓰기 , 벌레 옮기기
        dist = bugs[i].distance(play.pos())
        if dist < 20 : #만났다
            speed +=1
            jumsu +=1
            bugs[i].write(str(jumsu))
            bugs[i].color(b_color[r.randint(0,5)])
            bugs[i].shape(b_shape[r.randint(0,5)])
            bugs[i].shapesize(b_size[r.randint(0,5)])
            bugs[i].setheading(r.randint(0,360))
            bugs[i].up()
            bugs_x = r.randint(min_x,max_x)
            bugs_y = r.randint(min_y,max_y)
            bugs[i].goto(bugs_x,bugs_y)

t.mainloop()