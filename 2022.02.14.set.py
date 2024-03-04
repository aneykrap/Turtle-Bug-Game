# 1.형태 {  ,   ,   }
#2. 생성

s1=set([1,2,3])
print(s1)
s2= {4,5,6,7,7,7,6}
print(len(s2),s2)

#특징
#중복된 데이터는 들어가지 않음
#4. 함수
a={1,2,3,4,5}
b={    3,4,5,6,7}
c={1,2}
#1)합집합
#a와 b의 합집합
print(a.union(b))
print(a|b)
print(b.union(a))

#2)교집합 & intersection

print(a & b)
print(a.intersection(b))

print(a&c)
print(a.intersection(c))

#3) 차집합 - 
print(a-b)
print(a.difference(b))

print(b-a)
print(b.difference(a))

#4) 대칭차집합
print(a.symmetric_difference(b))
print(a^b)

#5) 부분집합
print(c.issubset(a))
print(c <=a)
print(c<a)
 

#6)상위집합

print(a.issuperset(c))
print(a>=c)

#7) 서로소 검사 1과 자기가신이외의 공약수를 갖지 않는 수

print('#'*20)
a={1,2,3,4,5}
b={    3,4,5,6,7}
c={1,2}


print(1 in a)

#9)집합 요소 추가하기

a.add(10)
print(a)

#10)집합의 요소를 여러개 추가하고 싶을때

a.update({11,12,13})
print(a)

#11) 집합의 요소값을 삭제하고 싶을때
#해당값이 없으면 에러

a.remove(13)
print(a)
if 20 in a:
    a.remove(20)
#12)최대값을 구하기
print(max(a))

#13)최솟값을 구하기
print(min(a))

print(dir(a))

#
