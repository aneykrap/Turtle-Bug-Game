#with

#1) 기본형
f=open('2022.06.13 test.txt','w')
f.write('test')
f.close()

#2) with문
with open('2022.06.13 test2.txt','w') as f:
    f.write('test2')

#예제
#2022.06.13 test2.txt 을 'a' 모드로 연 다음에 아래와 같은 두 줄 추가
# '파이썬으로 문자열으로 추가했습니다'
#'한글이 잘 보입니다'
#with문 사용

with open('2022.06.13 test2.txt','a',encoding='utf-8') as f:
    f.write('\n파이썬으로 문자열으로 추가했습니다')
    f.write('\n한글이 잘 보입니다')

#try-except

try:
    f=open('2022.06.13 test3.txt','r')
    f.write('test1')
except:
    print('에러발생')
finally:
    f.close()

#with 문 

try:
    with open('2022.06.13 test3.txt','r') as f:
        f.write('test1')
except:
    print('에러발생')
finally:
    pass























