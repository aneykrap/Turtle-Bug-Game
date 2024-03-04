# 내장함수
# 외장함수
#help(__builtins__)

#리스트관련 함수를 보고싶을때
#print(help(list))

#144쪽
#1)abs()
# print(abs(4)== abs(-4))

#2)eval()
# a=eval('1+1')
# print(a)

# print(eval("'a'+'b'"))
# print(eval("'1'+'0'"))

#3)divmod(분자,분모):몫과 나머지 구하기 => (몫,나머지)
#몫://
#나머지:%
import re


print(divmod(10,3),type(divmod(10,3)))
print(10//3,10%3)

#4)int() str() list() tuple() set() dict()
# 괄호안의 값을 각각 int,list,tuple로 자료형 변경

#5)hex() : 괄호안의 값을 16진수로 변경하는 함수
#0o숫자
#0x숫자(또는 a-f): 16진수 0~9,a~f
print(hex(15))

#다음 10진수를 16진수로 변경하세요
#1. 10 0xa
#2. 127 0x7f
#3. 54 0x36
print(hex(10))
print(hex(127))
print(hex(54))

#6)dir()
# print(dir([]))
# print(dir(''))

#7)chr(): 아스키코드값을 넣으면 문자로 리턴
print(chr(80))

#8)ord() : 문자=>아스키코드
print(ord('A'))

#9) all(): 괄호안의 값이 모두 참인지 검사
print(all([True,True,True,True])) #True
print(all([True,True,True,False])) #False

#자료형 배울때
#숫자: 0 ==> False, 0 이외의 값은 ==> True

#10) len()

#11) max()
print(max([1,4,3,5,10]))
print(max(1,50,25,33))

#12) min()
print(min([1,4,3,5,10]))
print(min(1,50,25,33))

#13) sorted()
a=[10,9,11,7,6,5]
print(sorted(a,reverse=True))
print(a)

#14) enumerate() : 리턴값이 튜플형태, (인덱스,자료값)
lst =['사과','당근','오징어','꼴뚜기']
for i in range(len(lst)):
    print(lst[i])

for i in lst:
    print(i)

for (i,s) in enumerate(lst):
    print(i,s)

#15) filter()
# 

def num(a):
    return type(a)==int

print(num(1))
print(num('a'))

print(list(filter(num,[1,'a'])))
#<filter object at 0x0000016D494E7F40> 

#15-2)

def func(x):
    if x>0:
        return True
    else:
        return False

a=[-5,-3,-1,1,3,5]

print(list(filter(func,a)))
#print((filter(func,a)))

#16) range()
# 3가지 형태
#range(n): range(0,n) : 0,1,2,3,4,......n-1
#range(n1,n2) : m1,n1+1..........n2-1
#range(n1,n2,n3) : n1, n1+n3, n1+n3+n3

print(range(5))
print(list(range(5)))
print(list(range(1,5)))
print(list(range(1,10,2)))

#17) zip() : 짝꿍 만들어서 리턴
print(zip([1,2,3],['a','b','c'])) #<zip object at 0x0000028BC72A0D40>
print(list(zip([1,2,3],['a','b','c'])))

#18) map()
# map(함수명,값)
def nn(a):
    return a*a

print(nn(4))
print(list(map(nn,[1,2,3,4,5,6,7,8,9,10])))

#실습1
'''
def cal(a):
    if a == int:
        return chr(abs(a))
    elif a == str:
        return print(ord(a))
cal('w')
'''

def cal():
    a = eval(input('수식입력: '))
    a = abs(a)
    a = round(a,0)
    a= int(a)

    if 90>=a>=65 or 122>=a>=97:
        print(chr(a))
    else: 
        print(str(a))

cal()

#실습2

def simul(a):
    a=list(map(str,a))
    print('자료 요소 참 여부:',all(a))
    print('자료 길이:',len(a))
    print('자료 중 최댓값:',max(a))
    print('정렬 시 자료 순서:',sorted(a))
    print('자료 번호:',list(enumerate(a)))

simul([1,3,5,'A','b'])



