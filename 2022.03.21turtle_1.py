#p.7
import turtle as t

t.title('도형그리기')  #윈도우 창 제목 설정
t.setup(500,500)       #윈도우 창 크기 설정
t.speed(0)              #1(가장 느림)~ 10(가장빠름),0(가장 빠름)
#t.penup()              #펜 띄우기
#t.goto()               #그 특정 점으로 이동
t.penup()
t.goto(-100,0)
t.pendown()

for i in range(4): #리턴값[0,1,2,3]
    t.forward(100) #현재 바라보고 있는 방향으로 이동
    t.left(90)     #현재 바라보고 있는 방향에서 왼쪽으로 회전

t.penup()
t.goto(200,0)
t.pendown()

for i in range(3): 
    t.forward(150) 
    t.left(120)   



#p.8
t.penup()
t.goto(-100,-200)
t.pendown()

for i in range(4): 
    t.forward(100) 
    t.left(90)   

t.penup()
t.goto(20,-200)
t.pendown()

for i in range(4): 
    t.forward(100) 
    t.left(90)   

#p.10
# t.penup()
# t.goto(300,-200)
# t.pendown()

#왼쪽으로 1도씩
# for i in range(360):
#     t.forward(1)
#     t.left(1)
#circle 쓰기


t.penup()
t.goto(400,-200)
t.pendown()
t.circle(50)


#p11
t.penup()
t.goto(-100,-300)
t.pendown()
t.speed(0)

for i in range(100):
    t.forward(i*2)
    t.left(90)


# t.penup()
# t.goto(0,-300)
# t.pendown()
# t.speed(1)

# for i in range(100):
#     t.forward(i)
#     t.left(90)




# t.penup()
# t.goto(100,-300)
# t.pendown()
# t.speed(10)

# for i in range(100):
#     t.forward(i)
#     t.left(90)



#p12
t.penup()
t.goto(300,-300)
t.pendown()
t.speed(0)
t.color('lime')
t.pensize(1)

for i in range(100):
    t.forward(100)
    t.left(89)   #79도로 했을 겹치는게 많음


#p13

t.penup()
t.goto(200,200)
t.pendown()
t.shape('turtle')
t.color('skyblue')
t.pensize(5)
t.speed(10)

for i in range(5):
    t.forward(100)
    t.left(145)

















t.mainloop()