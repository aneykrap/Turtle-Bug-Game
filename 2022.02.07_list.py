#리스트의 활용
#1 리스트의 형태
a= [1,2,3,'a','b']
print(a,type(a))
#2 생성하는 법
a= [1,2,3]
b= list()
c= list('apple')
print(c)

print(list(range(1,5)))

#3 리스트인지 확인하는 방법

c= [1,2,3]
print(type(c))

#4 인덱싱
a=['a','b','c','d','e']
print(a[2])

#5 슬라이싱

print(a[2:])

#6 리스트 요소값의 수정
a[-1]= 'F'
print(a)

#7 n 중 리스트
a= [0,1,2,3,4,5]
a= [0,1,2,[31,32,33,['a','b','c']],4,5]
print(len(a))

print(a[3][2])
print(a[3][3][0])
print(a[3][3][-1])


#문제

a= ['월','화','수','목','금','토',\
['오징어게임','지금우리학교는','마이네임',['김남길','진선규']]]

#리스트a의 길이는
print(len(a))
#오징어게임 인덱싱
print(a[6][0])
#진선규 인덱싱
print(a[6][3][1])
print(a[-1][-1][-1])
#목금토 슬라이싱
print(a[3:6])

# 태양계
solar= ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']

#지구형
print(solar[1:5])
#목성형
print(solar[5:])

##################################################################################
#리스트의 함수
#요소를 추가하는 함수3개
#1 1개의 요소 추가
a=[1,2,3,4]
a.append(4)
print(a)

#2 1개의 요소를 i 번째에 추가(새치기)
a.insert(0,5)
print(a)

#3 n의 요소를 추가할때
a.extend(['6','7'])
print(a)

#리스트의 요소 삭제함수
del a[0]
print(a)

#pop
print(a.pop())
print(a)


print(a.pop(0))
print(a)

#리스트에서 자주 사용하는 함수
#1)index
a=[1,1,1,2,2,2,2,3,3,3,3,3,4,5,6,7,8,9]
print(a.index(9))

#count()

print(a.count(1))
print(a.count(2))

#sort

a=['Z','a','4','3','2','#','땅콩','하늘','세종대왕']
#a.sort()
#print(a)

#reverse()
a.reverse()
print(a)

#리스트 연산자
c=['a','b']+[1,2]
print(c)
print(c*2)
