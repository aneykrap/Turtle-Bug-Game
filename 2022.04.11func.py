#2022.04.11 functiom
# 함수 : 사용자 정의 함수

# import keyword
# print(keyword.kwlist)
'''
'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
  'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield' 
 '''

# 함수 정의 방법
# 매개변수가 있는지 없는지 :2
# 리턴값이 있는지 없는지 

# import imp


# def hello(name):
#     print('hello',name)
# hello('Ryan')

# def print_list(*lst):
#     for l in lst:
#         print(l)

# print_list(1,2,3,4)
# print_list() 
# print_list(1)

#p 39
# 컴퓨터 내장함수 
# def sum():
#     a=2
#     b=3
#     print(a+b)
# sum()

# # sum()
# sum()
# def sum():
#     a=2
#     b=3
#     print(a+b)
#40
#인자값 : 이름,나이 ,주소
# 결과 : 리터갑없은



# def inter_person(nm,age,addr):
#     print('안녕하세요 내 이름은 {}이고 나는 {}살이고 {}에 삽니다. ')
# inter_person('홍길동','20','전라남도 장성국ㄴ')



# def introduce(name,age,addr):
#     print('안녕하세요 |n 내 이름은 {}이고, 나이는{}살이고 |n {}에 삽니다')

# import turtle as t 
# for i in range(3):
#     t.forward(100)
#     t.left(120)


# #도형 그리는 함수

# def draw_polygon(n):
#     for i in range(n):
#         t.forward(100)
#         t.left(390/n)


#도형함수 2

# def draw_polygon2(n,d):
#     for i in range(n):
#         t.forward(d)
#         t.left(360/n)

# # 도형함수 3

# def draw_polygon3(n,d=100,c='black',w=1):
#     t.pencolor(c)
#     t.pensize(w)
#     for i in range(n):
#         t.forward(d)
#         t.left(360/n)

# draw_polygon3(3)
# draw_polygon3(4,d=200,c='red')
       
#42 #출력

# def get_calc(a,b,c):
#     print((a+b)*c)
# get_calc(1,2,3)

# #42 # 리텁
# def get_calc2(a,b,c):
#     return((a+b)*c)
# d = get_calc2(1,2,3)
# print(d)

# #43
# #문제3
# def calc(n1,n2):
#     return(n1*n2)
# w = calc(5,4)
# print(w)

#문제5
'''
a= input('한변의 길이를 입력해주세요')
def triangle(a):
    for i in range(3):
        t.forward(a)
        t.left(120)

triangle(int(a))

#문제 6

def tri_d(w,h):
    return(w*h/2)
s = tri_d(5,4)
print(s)
'''

#47

def sayhello(name,place='미국'):
    print('{}님 안녕하세요.{}에 오신것을 환영합니다'.format(name,place))
    return name

sayhello('홍길동')
sayhello('홍길동','대만')

#49
#BMI

'''
저체중	20 미만
정상	20 - 24
과체중	25 - 29
비만	30 이상
'''
# def print_bmi(cm,kg,name='익명'):
#     m=cm/100 
#     bmi =round(kg/m**2,1)

#     msg=''
#     if bmi<20:msg='저체중'
#     elif 20<=bmi<25: msg='정상'
#     elif 25<=bmi<30: msg='과체중'
#     else: msg='비만'



#     print('BMI:',bmi,msg)

# print_bmi(170,50,'홍길동')

# 50
#문제3

def distance(x=0,y=0):
    if x==0 and y==0:
        x= float(input('x좌표를 입력하세요:'))
        y= float(input('y좌표를 입력하세요:'))
    d=(x**2+y**2)**0.5
    return round(d,1)

print(distance())














#t.mainloop()