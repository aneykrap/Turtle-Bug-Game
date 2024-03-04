import turtle as t
import random as r 
import time 

# 윈도우 설정
t.title('Turtle Run')
t.bgcolor('orange')

#변수 설정 = 전역변수

s_width = 600
s_height = 800
t.setup(s_width,s_height)

playing = False #게임진행 상태태그
score = 0



#거북이 기본설정
t.speed(0)
t.up()
t.shape('turtle')
t.color('blue')
# t.goto(0,0)



#글자쓰는 함수 

pen = t.Turtle()
pen.up()
pen.hideturtle() # 글자쓰는 객체 지우기


#먹이 객체 

feed = t.Turtle()
feed.shape('circle')
feed.up()
feed.speed(0)
feed.goto(0,-200)
feed.color('green')

#악당  객체 

ts = t.Turtle()
ts.shape('turtle')
ts.up()
ts.speed(0)
ts.goto(0,200)
ts.color('red')


#플레이어 거북이 이벤트
#함수 순서 1)전역변수 2) 사용자 함수 정의

def key_up():
    t.setheading(90)

def key_down():
    t.setheading(270)

def key_left():
    t.setheading(180)

def key_right():
    t.setheading(0)


#space 바 눌렀을때 

def game_start():
    global playing
    print('게임시작되었다!!!!')
    if not playing:
        pen.clear()
        playing = True 
        play()
    

def play():
    global playing,score
    
    t.forward(10)  # 현재 바라보고 있는 방향으로 10만큼

    # 플레이어 거북이와 먹이와의 거리가 25 이내 == 먹음
    # 거북이가 움직이므로 측정위치
    # 거리 측정은 distance
    #1 먹이 좌표구하기 position ==튜플 형태로
    pos = feed.position()

    #2 플레이어 거북이,먹이 거리 구하기
    dist = t.distance(pos)
    if dist < 25:
        score +=1
        f_x = r.randint(-s_width/2 +50, s_width/2-50)
        f_y = r.randint(-s_height/2 +50, s_height/2-50)
        feed.write(str(score))
        feed.goto(f_x,f_y)

    # 악당 거북이가 플레이어 따라다니기
    n =r.randint(1,5)
    if n==1 :
        # 1 악.거 기준에서 플.거 각도 구하기
        ang = ts.towards(t.pos())
        # 2 악.거 머리방향 설정
        ts.seth(ang)
    # 3 악.거 직진
    if score > 10:
        ts.forward(10)
    else :
        ts.forward(score+5)

    if t.distance(ts.pos()) <25:
        message('Game Over','score'+str(score))
        time.sleep(3)

        score =0
        playing = False
        t.goto(0,0)
        t.seth(0)
        ts.goto(0,200)
        ts.seth(0)
        feed.goto(0,-200)
        pen.clear()
        message('Turtle Run','space를 눌러주세요 ')

    

    if playing :
        t.ontimer(play,100) #1000 == 1초 #호출되는 함수 () 없음
    

#화면에 텍스트 쓰는 함수
#m1,m2 는 문자열이다

def message(m1,m2):
    pen.clear() #기존 글자 지우기
    pen.goto(0,100)
    # pen.write(m1)  # 사이즈 10 ,중심점 = 좌 하단 
    pen.write(m1,False,'center',('',30,'bold'))
    pen.color('white')
    pen.goto(0,-100)
    pen.write(m2,False,'center',('',20,'bold'))
    


message('Turtle Run','space를 눌러주세요')

# 방향키 
t.onkeypress(key_up,'Up')
t.onkeypress(key_down,'Down')
t.onkeypress(key_left,'Left')
t.onkeypress(key_right,'Right')


t.onkeypress(game_start,'space')










t.listen()

t.mainloop()