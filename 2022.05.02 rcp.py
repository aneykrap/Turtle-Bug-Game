# 가위바위보
import turtle as t
import random as r
#세로로 길쭉

s_width = 600
s_height = 800
gap = 20
com = ''
user = ''


#함수선언
#그림 나오기

def scissors(x,y):
    global user
    user = '가위'
    user_player.shape('가위-scissors.gif')
    complay()   
    set_last()
    
def rock(x,y):
    global user
    user = '바위'
    user_player.shape('바위-rock.gif')
    complay()
    set_last()

def paper(x,y):
    global user
    user = '보'
    user_player.shape('보-paper.gif')
    complay()
    set_last()


def complay():
    global com
    n = r.randint(1,3)
    if n == 1:
        com = '가위'
        com_player.shape('가위-scissors.gif')
    elif n ==2 :
        com = '바위'
        com_player.shape('바위-rock.gif')
    else: 
        com = '보'
        com_player.shape('보-paper.gif')

#승부겨루기 

def set_last():
    r_str=''
    print(1,user,com,r_str)
    if user=='가위':
        if com=='가위':
            r_str='무승부'
        elif com=='바위':
            r_str='패'
        elif com== '보':
            r_str='승'

    elif user=='바위':
        if com=='가위':
            r_str='승'
        elif com=='바위':
            r_str='무승부'
        elif com== '보':
            r_str='패'

    elif user=='보':
        if com=='가위':
            r_str='패'
        elif com=='바위':
            r_str='승'
        elif com== '보':
            r_str='무승부'
    print(2,user,com,r_str)
    pen.clear()
    pen.write(r_str,False,'center',('',20,'bold'))

    
    







t.title('가위바위보 게임')
t.bgcolor('lightyellow')
t.setup(s_width,s_height)

#사용할 이미지 리소스 불러오기
#가위-scissors.gif  바위-rock.gif  보-paper.gif

screen = t.Screen()
screen.addshape('보-paper.gif')
screen.addshape('바위-rock.gif')
screen.addshape('가위-scissors.gif' )


t.speed(0)
#제목 사각형 그리기
t.fillcolor('darkblue')
t.begin_fill()

t.penup()
t.goto(-s_width/2+20,s_height/2-20)
t.pendown()
t.goto(s_width/2-20,s_height/2-20)
t.goto(s_width/2-20,s_height/2-20-100)
t.goto(-s_width/2+20,s_height/2-20-100)
t.goto(-s_width/2+20,s_height/2-20)
t.penup()

t.end_fill()


# 사각형 안에 제목쓰기 : 가위바위보 게임

t.color('lightyellow')
t.up()
t.goto(0,s_height/2-105)
t.write('가위바위보 게임',False,'center',('',40,'bold'))

# 컴퓨터랑 이용자 글자쓰기


t.color('black')
t.up()
t.goto(-s_width/4,s_height/2-200)
t.write('컴퓨터',False,'center',('',20,'bold'))


t.color('black')
t.up()
t.goto(s_width/4,s_height/2-200)
t.write('플레이어',False,'center',('',20,'bold'))

t.hideturtle() # 커서숨기기

# 객체
# 승부=pen 컴퓨터 = com_player 플레이어 = user_player

pen = t.Turtle()  #승부표시
pen.up()
pen.goto(0,s_height/2-250)
pen.ht()

com_player = t.Turtle()
com_player.up()
com_player.goto(-s_width/4,-s_height/2+464/2)

user_player = t.Turtle()
user_player.up()
user_player.goto(s_width/4,-s_height/2+464/2)

t.onscreenclick( scissors ,1) # 1 => 마우스 왼
t.onscreenclick( rock ,2) 
t.onscreenclick( paper ,3)
t.listen()



t.mainloop()