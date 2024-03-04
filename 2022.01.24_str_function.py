#문자열 함수 확인

#print(dir(str))

#함수의 사용법을 알고 싶을 떄
# print(help(str.upper))
#print(help(str.replace))

#1.변환함수
#2.분리함수
#3.정렬함수
#4.문자열 확인함수
#5.판단함수

# 1. 변환함수
#   1)format() : '{} {}.format(1,2)'
#   2)upper(): 
from multiprocessing.pool import ApplyResult


a= 'hi'
print(a.upper() )

#   3)lower
a= 'MY NAME is ryan'
print(a.lower())

#   4)swapcase()
print(a.swapcase())

#   5)caporalize
a='my name is tonny'
print(a.capitalize())

#   6)title
print(a.title())

#   7)strip
a='     he  ll o     '
print(a.strip())
print(a.replace('  ',''));print(a.replace(' ',''))
a='--hello--'
print(a.strip('-'))

#   8)lsrip
a='     he  ll o     '
print('#'+a.lstrip()+'#')

#   9)rstrip
print('#'+a.rstrip()+'#')

#   10)replace
a = '-h-e-ll-o'
print(a.replace('-',''))

#   11)join()
a='hello'
print('-'.join(a))

print('#'*10,'분리함수','#'*10)
#2)분리함수
#   1)partition
a= 'hello my name is ryan'
b= a.rpartition(' ')
print(b)
print(type(b))

#   2)rpartition()
#   3)split
a= 'hello my name is ryan'
b= a.split(' ')
print(b)

jumin='020523-1122111'
a=jumin.split('-')
print(a[0],a[1])

#       split에 인덱스를 줄때
a= 'hello my name is ryan'
b= a.split(' ',2)
print(b)

#   4)rsplit
a= 'hello my name is ryan'
b= a.rsplit(' ',2)
print(b)

#   5)splitlines
a='haha \n hoho \n hihi'
print(a)
print(a.splitlines())

#(연습)
a= 'a_b_c_d_e'
lines='a\nb\nc\nd'
print(a.partition('_'))
print(a.rpartition('_'))
print(a.split('_'))
print(a.rsplit('_',2))
print(lines.splitlines())

#3 정렬함수

a='hello'
print('#'+a.center(20)+"#")
print('#'+a.ljust(20)+'#')
print('#'+a.rjust(20)+'#')

#4 문자열 확인함수 8개
#   1)count()
a= 'apple'
print(a.count('z'))
print(a.count('a'))

#   2)startwith
print(a.startswith('a'),type(a.startswith('a')))
print(a.startswith('z'))

#   3)endswith
print(a.endswith('e'))
print('my name is Ryan'.endswith('Ryan'))

#   4)find()
a= 'apple'
print(a.find('p',2))
print(a.find('z'))

#   5)rfind()

print(a.find('p'),a.rfind('p'))



