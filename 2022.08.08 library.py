#174
#라이브러리

#파이썬 내장함수 예) print() int() str()
#사용자가 정의해서 만드는 함수
#***.py => 모듈
#파이썬이 설치될때에는 없었음. 새롭게 제공
#새로 설치 :pip install 라이브러리명
# import 라이브러리 이름

# math 
'''
import imp
import math

print(math.pi)
a = math.factorial(10)
print(a)
print(dir(math))

#175
print(math.pi*(10/2)**2)

#인터넷과 관련된 라이브러리
#웹 브라우저
import webbrowser
a= webbrowser.open('https://www.naver.com')
print(a) #True
'''
'''
import urllib.request
a=urllib.request.urlopen('https://www.naver.com')
print(a,type(a)) #<http.client.HTTPResponse object at 0x000001E6C82041F0>
#<class 'http.client.HTTPResponse'>
print(a.status) #200 정상 , 404페이지를 찾을 수 없음
print(a.read())
'''

#웹 크롤링==> 인터넷에서 내가 원하는 정보만 게더링 하는 방법
#코로나 3년 사이에,대학교 대학원에서 교재 개발

# 178 datetime : 날짜와 시간정보를 제공하는 라이브러리
# time 라이브러리 : 1970,1,1 0시 0분 0초 경과된 초를 리턴
# 
import datetime
import imp

print('오늘의 날짜는:',datetime.date.today())
d=datetime.date.today()
print(type(d.year),type(d.month),type(d.day))

print(d.ctime())

#178
print('*'*10)
print(datetime.time(7))
print(datetime.time(7,0))
a = datetime.time(12,30,55)

print(a)

print(a.hour,a.minute,a.second)

print(a.isoformat())
print(a.strftime('%H시 %M 분 %S 초 입니다.'))

#178

import time

print(time.time()) #1659957868.6740317 #1659957884.9788628

start_tm = time.time()
while True :
    gap_time = time.time()-start_tm
    print(gap_time)
    time.sleep(0.5)
    if gap_time >3:
        break


#179

# print(time.time())
# print(time.localtime(time.time()))
# a= time.localtime()
# print(time.strftime('%Y %m %d %c',a))

# d= datetime.datetime(2000,8,15)
# print(d - datetime.timedelta(days = 30))

# for i in range(10):
#     print(i)
#     time.sleep(1)


#180
#문제1

d= datetime.date.today()
print(d+datetime.timedelta(days=1000))

#문제2

for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print('발사')