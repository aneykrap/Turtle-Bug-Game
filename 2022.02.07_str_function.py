#판단함수
from operator import truediv


num='123'
n2 = '½'
n3 ='3²'
fake = 'hundred'
hangle = '한글'
#1) isdigit
print('*'*5,'isdigit()','*'*5)
print(num,' isdigit :',num.isdigit())
print(num,' isdigit :',n2.isdigit())

#2 isalnum
print('*'*5,'isalnum()','*'*5)
print(num,' isalnum :',num.isalnum())
print(num,' isalnum :',n2.isalnum())
print(num,' isalnum :',n3.isalnum())
print(num,' isalnum :',hangle.isalnum())
print(num,' isalnum :',fake.isalnum())

#3 isalpha 
print('*'*5,'isalpha ()','*'*5)
print(num,' isalpha  :',num.isalpha())
print(num,' isalpha  :',n2.isalpha ())
print(num,' isalpha  :',n3.isalpha ())
print(num,'isalpha  :',hangle.isalpha ())
print(num,' isalpha :',fake.isalpha ())

#4 isdecimal
print('*'*5,'isdecimal ()','*'*5)
print(num,' isalpha  :',num.isdecimal())
print(num,' isalpha  :',n2.isdecimal ())
print(num,' isalpha  :',n3.isdecimal ())
print(num,'isalpha  :',hangle.isdecimal ())
print(num,' isalpha :',fake.isdecimal ())

#5 isidentifier
print('*'*5,'isidentifier()','*'*5)
print(num,' isalpha  :',num.isidentifier())
print(n2,' isalpha  :',n2.isidentifier ())
print(n3,' isalpha  :',n3.isidentifier())
print(hangle,'isalpha  :',hangle.isidentifier ())
print(fake,' isalpha :',fake.isidentifier ())



a= 'True'
b= 'apple'
c = '##.@'
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())


#6 islower
a = 'apple'
b = 'APPLE'

print(a,' islower: ',a.islower())
print(b,' islower: ',b.islower())


#7 isupper
a= 'APPLE'
b = 'apple'
print(a,' isupper: ',a.isupper())
print(b,' isupper: ',b.isupper())

#8 istitle
a= 'My name is Ryan'
b= 'My Nmae Is Ryan'
print(a, 'istitle:',a.istitle())
print(b, 'istitle:',b.istitle())

#9 isspace
a= '    '
b='     apple    '
print(a, 'isspace:',a.isspace())
print(b, 'isspace:',b.isspace())

#10 isnumeric
print('*'*5,'isnumeric()','*'*5)
print(num,' isalpha  :',num.isnumeric())
print(n2,' isalpha  :',n2.isnumeric ())
print(n3,' isalpha  :',n3.isnumeric())
print(hangle,'isalpha  :',hangle.isnumeric ())
print(fake,' isalpha :',fake.isnumeric ())
