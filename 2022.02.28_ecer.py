#180

# mon = input('개월수를 입력하세요:     ')
# mon = int(mon)


# if mon<=1:
#     print('결핵 예방접종을 하세요')
# if mon<=2:
#     print('B형 간염예방접종을 하세요')
# #2<= mon and <=6
# if 2<=mon<=6:
#     print('파상풍 예방접종을 하세요')
# if 2<=mon<=15:
#     print('페렴구균 예방접종을 하세요')

#182

# running1 = float(input('100m기록을 입력하세요(초):  '))
# running2 = float(input('1000m기록을 입력하세요(초):  '))
# up=int(input('윗몸일으키기 기록을 입력하세요(회): '))
# press= float(input('좌우 압력 기록을 입력하세요(kg): '))
# pp= int(input('팔굽혀펴기 기록을 입력하세요(회): '))

# #and 로 잡아줬어야 함

# if 0<running1<=13.6 and 0<running2<=237 and 51<=up and 56<=press and 46<=pp:
#     print('합격가능성이 매우 높습니다.')
# else:
#     print('합격가능성이 낮습니다. ')

#공무원 시험 
# kor = int(input('국어점수:  '))
# eng = int(input('영어점수:  '))
# his = int(input('한국사점수:  '))

# if kor<40 or eng<40 or his<40:
#     print('과락')
# else:
#     print('과락아님')
#     if (kor+eng+his)/3>=60:
#         print('합격')
#     else:
#         print('불합격')

#리스트 자료형을 이용하는 방법

# jumsu= []
# jumsu.append(int(input('국어점수:  ')))
# jumsu.append(int(input('영어점수:  ')))
# jumsu.append(int(input('한국사점수:  ')))


# if jumsu[0]>=40 and jumsu[1]>=40 and jumsu[2]>=40:
#     avg= sum(jumsu)/len(jumsu)
#     print('평균:',avg)
#     if avg >= 60:
#         print('합격')
# else:
#     print('과락')


#자동 판매기
#주문하시려면 엔터키를 눌러주세요==>입력
#사용자: 엔터키를 친다.
#1.사이다(700) 2.콜라(800) 3.물(1200)
#주문하려는 품목의 번호를 입력해주세요.==>입력
#1
#돈을 입력해주세요 ==>입력
#1000
#넣은 돈보다 제품가격이 높으면 : 주문할 수 없습니다.금액부족
#그렇지 않으면
#   제품을 제공:사이다가 나왔습니다.
#   거스름돈을 거슬러 줍니다. 

order = input('주문하시려면 엔터키를 입력해주세요')
print('1.사이다(700) 2.콜라(800) 3.물(1200)')
menu = input('주문하려는 품목 번호를 입력해주세요')
mm= int(input('돈을 입력해주세요:    '))

if mm <700:
    print('주문할 수 없습니다,금액부족')
elif 700<=mm<800:
    if menu =='1':
        print('사이다가 나왔습니다.\n'+'거스름 돈:',(mm-700))
    if menu=='2':
        print('금액부족')
    if menu=='3':
        print('금액부족')
elif 700<=mm<1200:
    if menu=='1':
        print('사이다가 나왔습니다.\n'+'거스름 돈:',(mm-700))
    if menu=='2':
        print('콜라가 나왔습니다.\n'+'거스름 돈:',(mm-800))
    if menu=='3':
        print('금액부족')
elif mm>=1200:
    if menu=='1':
        print('사이다가 나왔습니다.\n'+'거스름 돈:',(mm-700))
    if menu=='2':
        print('콜라가 나왔습니다.\n'+'거스름 돈:',(mm-800))
    if menu=='3':
        print('물이 나왔습니다.\n'+'거스름돈 :',(mm-1200))


