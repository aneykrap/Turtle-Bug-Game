#딕셔너리
a={'길동':70,'길동':90}
print(a)

#키값은 리스트 형태 안됨
#연습
a={1:'사과',2:'배',3:'포도'}
print(a)

print(a.items())

print(a.keys())

print(type(a.keys()))

print(a.values())

#키값이 존재하는 확인 // in, not in

print(1 in a)
print(1 in a.keys())

print('포도' in a.values())

#삭제

del a[1]
a.clear()
print(a)

#del a
#print(id(a))

c= {'이름':'홍길동','나이':16,'아버지':'김판서'}
print(c.get('이름'))
print(c.get('아버지'))
print(c.get('키'))
#못찾으면none

c['아버지']='홍상직'
print(c)

#연습문제

a= {'강감찬':'귀주대첩','을지문덕':'살수대첩','세종대왕':'집현전'}
a['서희'] = '강동6주'
print(a)

a['세종대왕']='한글'
print(a)

print('을지문덕'in a)

del a['을지문덕']
print(a)

b = {'서울':'세종대왕','파주':'윤관','성남':'이집'}
print(b.get('성남'))
del b['성남']
b['남양주']='정약용'
print(b.values())
#118쪽 2번

dic={'서울':'세종대왕','파주':'윤관','성남':'이집'}
print(dic.pop('성남'))
print(dic)
