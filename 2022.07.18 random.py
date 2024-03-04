#random 라이브러리
import random as r

for i in range(10):
    print(r.randint(1,6)) #1부터 6까지 정수 중에 1개 뽑기

for i in range(10):
    print(r.random()) # 0부터1사이 실수

lst=[1,2,3]
r.shuffle(lst) #리스트를 섞는다
print(lst)

lst = ['토끼반','호라이반','사자반']
print(r.choice(lst))
print(lst[r.randint(0,2)])

# import turtle as t

# for i in range(100):
#     t.goto(r.randint(-200,200),r.randint(-200,200))
# print('완료')

#up down 문제

n = r.randint(1,50)
a=0
#a = int(input('입력해주세요:'))

while a != n:
    a = int(input('입력해주세요:'))
    if a > n :
        print('down')
    elif a < n :
        print('up')
 
print('정답!!')
