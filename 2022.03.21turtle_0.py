import turtle as t

t.title('도형그리기')  #윈도우 창 제목 설정
t.setup(500,500)       #윈도우 창 크기 설정
t.speed(3)              #1(가장 느림)~ 10(가장빠름),0(가장 빠름)
#t.penup()              #펜 띄우기
#t.goto()               #그 특정 점으로 이동
t.penup()

t.shape('turtle') #커서의 모양 바꾸기
t.goto(-200,100)
t.pendown()
t.color('blue')
t.pensize(3) #밑에 영향을 다 받음

#사각형 #파란색


for i in range(4): #리턴값[0,1,2,3]
    t.forward(100) #현재 바라보고 있는 방향으로 이동
    t.left(90)     #현재 바라보고 있는 방향에서 왼쪽으로 회전


# 1사분면으로 이동
t.penup()
t.goto(100,100)
t.pendown()
t.shape('circle')
t.color('lightblue')
for i in range(3): 
    t.forward(110) 
    t.left(120) 


#3사분면으로 이동 
t.penup()
t.goto(-150,-100)
t.shape('square')
t.color('lime')
t.pensize(2) 
t.pendown()
t.circle(50)



t.mainloop() # 멈춰있게 함
