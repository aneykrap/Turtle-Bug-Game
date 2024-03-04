import turtle as t
import time 
import random as r
# from playsound import playsound

s_width = 800
s_height= 800
speed = 4 #초기속도 설정
play = False
jumsu = 0 #초기점수 설정

min_x=-s_width/2
min_y=-s_height/2
max_x=s_width/2
max_y=s_height/2

bgm = False # 배경음악 동작 여부

def k_right():
    if snake_head.heading()!=180:
        snake_head.setheading(0)
   
def k_left():
    if snake_head.heading()!=0:
        snake_head.setheading(180)
    
def k_up():
    if snake_head.heading()!=270:
        snake_head.setheading(90)
    
def k_down():
    if snake_head.heading()!=90:
        snake_head.setheading(270)
def start():
    global play
    if not play:
        play = True

t.title('Turtle snake')
t.setup(s_width,s_height)

#s.update()
#스크린 추적 
s=t.Screen()
s.tracer(0)

t.bgcolor('black')

#뱀머리 만들기
snake_head = t.Turtle()
snake_head.color('lightblue')
snake_head.shape('square')
snake_head.shapesize(1)
snake_head.up()

#뱀 몸통 정의
snake_body = []


#먹이 만들기
f_color=['lightyellow','white','lightgreen','lightpink','purple']
f_shape=['arrow', 'turtle', 'circle', 'triangle', 'classic' ]
food = t.Turtle()
food.color(f_color[r.randint(0,4)])
food.shape(f_shape[r.randint(0,4)])
food.shapesize(0.8)
food.up()
f_x = r.randint(min_x+50,max_x-50)
f_y = r.randint(min_y+50,max_y-50)
food.goto(f_x,f_y)

t.onkeypress(k_right,'Right')
t.onkeypress(k_left,'Left')
t.onkeypress(k_up,'Up')
t.onkeypress(k_down,'Down')
t.onkeypress(start,'space')


s.update()
# t.listen()

# print('시작음 before',time.time())
# playsound('start.wav',True)
# print('시작음 after',time.time())
s.update() 


while True:
    if play:
        # if not bgm:
        #     bgm_star_tm = time.time()
        #     playsound('bgm2.wav',False)
        #     bgm = True
        # else:
            
        #     gap_time=time.time() - bgm_star_tm 
        #     if gap_time > 8.3:
    
        #         bgm = False


        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_head.forward(speed)
        # 만약 머리&먹이가 닿으면 jumsu+1,쓰기
        dist =snake_head.distance(food.pos())
        if dist<=18:
            # playsound('coin.wav',False)
            speed +=0.7
            jumsu+=1
            food.up()
            food.write(str(jumsu))
            food.color(f_color[r.randint(0,4)])
            food.shape(f_shape[r.randint(0,4)])
            food_x = r.randint(min_x+50,max_x-50)
            food_y = r.randint(min_y+50,max_y-50)
            food.goto(food_x,food_y)

            #뱀의 몸통 늘리기:
            body = t.Turtle()
            body.color('lightblue')
            body.shape('square')
            body.up()
            snake_body.append(body)

        #첫번째 몸통 =>snake_head
        if len(snake_body)>0:
            snake_body[0].goto(x,y)
        #나머지 몸통 =>자기앞에 있는 몸통
        for i in range(len(snake_body)-1,0,-1):
        #for i in range(2,len(snake_body)):
            b_x= snake_body[i-1].xcor()
            b_y= snake_body[i-1].ycor()
            snake_body[i].goto(b_x,b_y)
            snake_body[i]

        #게임오버 처리
        #1) 머리가 테두리에 닿았을 때   
        s_x = snake_head.xcor()
        s_y = snake_head.ycor()
        if s_x <min_x or s_x> max_x or s_y <min_y or s_y> max_y or s_y <min_y or s_y> max_y:
            snake_head.goto(0,0)
            snake_head.write('Game Over',False,'center',('',30,'bold'))
            time.sleep(2)
            play = False
            break
        
        #2) 머리가 몸통에 닿았을때에도 게임오버
        for i in range(1,len(snake_body)-1):
            #머리와 i번째 몸통과의 거리를 잰다(distance)
            # 20 이내 이면 머리와 몸통이 닿았다
            dist = snake_head.distance(snake_body[i].pos())
            if dist < 5:
                #print('머리 몸통 터치')
                snake_body.clear()
                snake_head.goto(0,0)
                snake_head.write('Game Over',False,'center',('',30,'bold'))
                time.sleep(2)
                play = False
                break    






    s.update()
    time.sleep(0.1)

t.mainloop()
