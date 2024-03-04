# 밤하늘의 별이 반짝반짝 빛나는 화면
# import turtle as t
# import random as r
# import time



'''
#1970.1.1 0시 0분 0초 부터 경과한 시간 (초)
print(time.time())

#time.sleep(3)  # x초 동안 멈춤
print(time.time())
for i in range(10):
    n = r.randint(1,100)  #int 정수임 #1~~100 ,100포함
     # n = r.random()        #소수점
    print(n)
'''


'''
# 별 정의
color = ['yellow','pink','orange','cyan','lightblue']  #별색상
line = [10,20,30,40,50]   #별크기

width = 800              #가로크기
height = 600             #세로크기
line_width=[1,2,3,4,5]   #별의 선두께


min_x = -width/2
max_x = width/2
min_y = -height/2
max_y = height/2

t.bgcolor('darkblue')
for i in range(100):
#별의 좌표
    x = r.randint(min_x,max_x)
    y = r.randint(min_y,max_y)
    n = r.randint(0,4)

    star_line = line[n]
    star_color = color[r.randint(0,4)]


    t.speed(0)
    t.hideturtle()#커서 숨기기


    t.penup()
    t.goto(x,y)
    t.color(star_color)
    t.pendown()
    t.pensize(star_line[n])


    for i in range(5):
        t.forward(star_line)
        t.right(144)

t.mainloop()

'''


import turtle as t


t.shape('turtle')
t.goto(0,0)
t.pensize(1)
t.color('red')
t.forward(100)
t.pensize(5)
t.color('blue')
t.forward(100)
t.pensize(10)
t.color('yellow')
t.forward(100)


t.mainloop()



