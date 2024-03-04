#내장함수
print()
print(1)
print('s')
print('a','b')
print('a','b',123)
print('a','b',1234,sep = '-')
print('a','b',12345,sep = '-', end = '\t')
a =print('Hello')
print(a)

#사용자 함수 만들기 연습(4종)
#인사하는 함수 :
#type1) 매개변수도 없고,리턴값도 없는 함수
def hello():
    print('hello')
hello()

#type2) 매개변수 없고, 리턴값 있는 함수 
def hello2():
    return 'hello'
a = hello2()

print(a)

#type3) 매개변수 있고, 리턴값 없는 함수
def hello3(name):        #name : 지역변수
    print('hello',name) 

hello3('펭수')

#type4) 매개변수 있고, 리턴값 있는 함수
def hello4(name):
    return('hello'+ name)
print(hello4('심사임당'))

#p.35

def hello(nm):
    print(nm,'님 반갑습니다.')
    print('파이썬에서 함수 만들며 놀아 보아요.')

hello('펭수')

def hello_count(nm,cnt):
    for i in range(cnt):
        print(nm,'님 반갑습니다.')
    return str(cnt)+'번 출력했습니다.'

print(hello_count('펭수',3))

#p.36

def triple(x):
    print(x*x*x)
triple(3)

def multiple(x,y):
    print(x*y)
multiple(7,9)

#p.37
def multiply_type1(a,b,c):
    print(a*b*c)
d= multiply_type1(3,4,5)
print(d)

def multiply_type2(a,b,c):
    return(a*b*c)
d = multiply_type2(3,4,5)
print(d)

# 함수 만들기 1
# 반지름을 입력하면 원의 넓이를 리턴하는 함수
# 함수명 : get_circlearea()
# 매개변수 : r (반지름)
# 리턴값 : 3.14*r**2

def get_circlearea(r):
    return(3.14*r**2)

print(get_circlearea(5))


# 함수 만들기 2
# 밑변과 높이를 입력하면 삼각형의 면적을 리턴하는 함수 
# 함수명: get_triarea()
# 매개변수 : len1,len2
# 리턴값 : (밑변*높이)/2

def get_triarea(len1,len2):
    return(len1*len2)/2

print(get_triarea(10,5))

#