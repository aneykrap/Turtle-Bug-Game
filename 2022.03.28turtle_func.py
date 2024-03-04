#
import time
import turtle as t
s_width = 800
s_height = 800
t.title('복습하기') 

# t.setup(s_width,s_height)
# t.write('삼각형을 그렸다가 지웠음')

#time.sleep()

# t.begin_fill()
# t.fillcolor('red')
# for i in range(4):
#     t.forward(100)
#     t.left(90)
# t.end_fill()

# 맨 꼭대기에 사각형 그리고 제목을 쓰는 연습
min_y = s_height/20-120  #280
max_y = s_height/20 -20   #380
min_x = -s_width/2 +20   #-380
max_x = s_width/2 -20    #380

# t.begin_fill()
# t.fillcolor('darkblue')
# t.penup()
# t.goto(min_x,max_y)
# t.pendown()
# t.goto(min_x,min_y)
# t.goto(max_x,min_y)
# t.goto(max_x,max_y)
# t.goto(min_x,max_y)
# t.end_fill()

#큰 글자 쓰기
'''
t.color('yellow')
t.penup()
t.goto(0,min_y + 5)
t.pendown()
t.write('도형연습',False, align= 'center',font=('Arial',30,'bold'))

##time.sleep(1)

t.reset()
#큰 원 그리기
# t.speed(4)
# t.pensize(5)
# t.color('red','blue')
# t.begin_fill()
# t.circle(100)

# t.end_fill()


# t.pendown()
# t.forward(50)
# t.penup()


#사각형 그리기
#  time 

# t.speed(4)
# t.pensize(5)
# t.color('black','pink')
# t.begin_fill()

# for i in range(4):
#     t.forward(200)
#     t.left(90) 

# t.end_fill()
# t.penup()
# t.goto(0,-100)
# t.write('speed는 4 , pensize 5 , color는 black&pink')


#큰원 그리기

t.goto(0,50)

t.begin_fill()
t.color('red','blue')
t.circle(50)
t.end_fill()
t.goto(0,-50)
t.write('circle')
t.clear()

time.sleep(1)

#사각형 그리기
#  time 

t.speed(4)
t.pensize(5)
t.color('black','pink')
t.begin_fill()

for i in range(4):
    t.forward(200)
    t.left(90) 

t.end_fill()
t.penup()
t.goto(0,-100)
t.write('speed는 4 , pensize 5 , color는 black&pink')
t.clear()

'''
'''
#오륜기 그리기
t.speed(0)
t.pensize(10)
t.color('blue')
t.circle(50)

t.penup()
t.goto(50,-50)
t.pendown()
t.color('yellow')
t.circle(50)

t.penup()
t.goto(100,0)
t.pendown()
t.color('black')
t.circle(50)

t.penup()
t.goto(150,-50)
t.pendown()
t.color('green')
t.circle(50)

t.penup()
t.goto(200,0)
t.pendown()
t.color('red')
t.circle(50)
t.clear()
t.speed(0)


#반복문으로 만들기
clist=['blue','yellow','black','green','red']
x = -100
y = 0
r = 50

t.penup() #약어 t.up  t.pu
t.goto(x,y)
t.pensize(7)
for i in range(len(clist)):
    t.up()
    if i % 2==0:
        t.goto(x+r*i,y)
    else:
        t.goto(x+r*i,y-r)
    
    t.color(clist[i])
    t.down()
    t.circle(r)

t.reset

'''
'''
t.pensize(1)
clist2 = ['purple','blue','yellow','white']
t.bgcolor('black')
t.speed(0)
for i in range(200):
    for j in clist2:
        t.pencolor(j)
        t.forward(i)
        t.left(89)


t.reset()

n = 50
t.color('green')
for i in range(n):
    t.circle(80)
    t.left(360/n)

t.reset()
'''
#t.bgcolor('yellow')

#페이지30
t.shapesize(5)
t.shape('turtle')
#좌표이동 및 확인에 대한 함수
#t.forward() t.back()
#t.goto(x,y) , setpos(x,y)
t.setx(-300)
t.sety(-200)


print(t.xcor())
print(t.ycor())

t.setpos(0,0)


d = t.distance(-300,0)
print(d)

ang = t.heading()
print(ang)
t.left(90)
print(t.heading()) #현재 거북이가 바라보는 각도

t.setheading(270)

ang = t.towards(-200,-200)
print(ang)

t.mainloop()