from ast import keyword


a = 100
import keyword
#print(keyword.kwlist)
#할당하자-> 대입
b=-3

#140


#142
#bmi:  kg/㎡(몸무게/키**2,단 키는 m)
#몸무게와 키 입력받기
# w= float(input('몸무게를 입력하세요(kg):'))
# h=float(input('키를 입력하세요(cm):'))
# bmi = w/((h/100)**2)
# bmi = round(bmi,1)
#print(bmi)

# if bmi<18.5:
#     print('저체중',bmi)

# elif 18.5<=bmi<23:
#     print('정상',bmi)

# elif 23<=bmi<25:
#     print('과체중',bmi)

# else:
#     print('비만',bmi)

#복합연산자

#논리연산자 사용시 주의사항
#and or 복합적으로 있는 경우
#괄호()를 표시해서 우선순위를 명확하게 해줘야 함

#멤버연산자

print('a' in 'apple')
print('z' not in'apple')

print('A' in ['A','B','C','D'])


#152

print('몫',11711//17)
print('나머지',11711%17)

print(19*4123+15)
a =9999//17
print(a*17)

#157
a= 15.3
b= 12.1

#a**2+b**2==c**2
print((a**2+b**2)**0.5)

#제어문:
'''jumsu=int(input('점수를 입력하세요:'))
if 70>jumsu >=60:
    print('D학점 입니다')
elif 80>jumsu >=70:
    print('C학점 입니다')
elif 90>jumsu >=80:
    print('B학점 입니다')
elif jumsu >=90:
    print('A학점 입니다')
else:
    print('학점을 계산할 수 없습니다.')'''


# jumsu=int(input('점수를 입력하세요:'))
# if jumsu >=90:
#     print('A학점 입니다')
# elif 80>jumsu >=80:
#     print('B학점 입니다')
# elif 90>jumsu >=70:
#     print('C학점 입니다')
# elif jumsu >=60:
#     print('D학점 입니다')
# else:
#     print('학점을 계산할 수 없습니다.')


# pwd = input('비밀번호를 입력하세요:')
# if pwd == '0610':
#     print('문이 열렸습니다.')
# else:
#     print('비밀번호가 일치하지 않습니다.')

age = int(input('나이를 입력해주세요:'))
if age>=15:
    print('영화를 볼 수 있습니다.')
else:
    print('이등급의 영화를 볼 수 없습니다')