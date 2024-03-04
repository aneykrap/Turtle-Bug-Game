a='hello python'

#1 
print(a[:5])
print(a[:-7])
#2
# print(a[6:])

# b='python'
# print(b[::2])

# c='홀짝홀짝홀짝홀짝'
# print(c[1::2])

#문자열 포매팅 

'''name = input('이름을 입력하세요:')
print(name+"님 어서오세요")
print(name,'님 어서오세요')
print('%s님 어서오세요'%name)


degree = -11.5
print('오늘의 아침 최저기온은 %f도 였습니다.'%degree)
print('오늘의 아침 최저기온은 %.1f도 였습니다.'%degree)

age = 20
print('내 나이는 %d 살 입니다.'%age)

# int 
age = input('당신의 나이는 몇 살입니까')
print(type(age))
print('당신의 나이는 %s 살 이군요.'%age)
print('3년후 당신의 나이는 %d 살 이군요.'%(int(age) +3))'''

# #자리수 포맷팅
# name= '펭수는 남극에서 왔습니다.'
# print('%s'%name)
# print('*%s*'%name)
# print('*%10s*'%name)

# print('*%10.1f*'%3.14)
# print('*%-10.1f*'%3.14)


# #포매팅을 2개이상
# name = '홍길동'
# age = 20
# friend1 = '이황'
# friend2 = '이이'

# print('%s는 %d살 입니다. 그의 베스트 프렌드는 %s와 %s입니다. '%(name,age,friend1,friend2))
# # print('%s는 %d살 입니다. 그의 베스트 프렌드는 %s와 %s입니다. '%(name,age,friend1))

yyyy = 2022
mm = 1
dd = 17

# #1 
print('오늘은 ' + str(yyyy)+ "년 " + str(mm) +'월 '+str(dd)+"일 입니다.")

# #2
# print('오늘은 %d년 %d월 %d일 입니다.'%(yyyy,mm,dd))

# print(round(3.141592,3))
# print(int(3.5))

# #1
# # print('%.3f'%1.23456789)
# # print('%0.3f'%1.23456789)
# # print('%10.3f'%1.23456789)

# # print('50년 후에 내가 살아 있을 확률은 %.1f%%입니다.'%99.999999)

# # per = input('당신이 성공할 확률은?')
# # print('당신이 성공할 확률은 %s입니다'%per)

# # per = float(per)
# # print('당신이 성공할 확률은 %.1f%%입니다'%per)

# #format() 함수

# print('내 이름은 {}이야'.format('김삼순'))
# print('내 절친은 {1}과 {0}야'.format('현빈','원빈'))
# print('내 절친은 {}과 {}야'.format('현빈','원빈'))

# name = '홍길동'
# age = 20

# print('내 이름은 {}이고, 내 나이는 {}살 입니다'.format(name,age))

# print('내 이름은 {name}입니다. 내 나이는 {age}살 입니다.'.format(name='홍길동',age = '20'))
# print('내 이름은 {name}입니다. 내 나이는 {age}살 입니다.'.format(age = '20',name='홍길동'))

# # 정렬방식 비교
# print('*{}*'.format('hello'))
# print('*{0:<10}*'.format('hello'))
# print('*{0:>10}*'.format('hello'))
# print('*{0:-^10}*'.format('hello'))
# print('*{0:^10}*'.format('hello'))
# print('*{0:#^10}*'.format('hello'))

# str1 = '2022년 1월 17일'
# num = 10
#오늘은 2022년 1월 17일입니다. 나는 올해 10개의 꿈을 이룰 것입니다. 
#print(   .format(str1,num))
#print(%s,%d)
#print( ++)


# #1
# print('오늘은 {}입니다. 나는 올해 {}개의 꿈을 이룰 것입니다.'.format(str1,num,))

# #2
# print('오늘은 %s입니다. 나는 올해 %d개의 꿈을 이룰 것입니다.'%(str1,num))

# #3
# print('오늘은' +str1+ '입니다.' '나는 올해 ' +str(num)+'개의 꿈을 이룰 것입니다.')

# 주민등록번호 규칙
# 판별
#생년월일 - 
# # 뒤에 첫번째 자리 : 2000년 이전 성별 1 남 2 여
#                      2000년 이후 성별 3 남 4 여 
#                      5,7 외국인 남자
#                      6,8 외국인 여자 
# 성별 뒤의 5자리 = 본적 + 일련번호
# 가장 마지막 = 검증용 카드

jumin = input('주민번호 입력:')
tot = int(jumin[0])*2 \
+int(jumin[1])*3\
+int(jumin[2])*4\
+int(jumin[3])*5\
+int(jumin[4])*6\
+int(jumin[5])*7\
+int(jumin[6])*8\
+int(jumin[7])*9\
+int(jumin[8])*2\
+int(jumin[9])*3\
+int(jumin[10])*4\
+int(jumin[11])*5

#print('총합:',tot)
#print('총합을 11로 나눈 나머지:',tot % 11)
#print('검증코드',11 - (tot % 11))

print(int(jumin[12]) == 11 - (tot % 11))
