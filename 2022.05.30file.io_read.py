#123 : 파일을 읽는 3가지 함수

'''
fname='2022.05.30 test.txt'
f=open(fname,'r',encoding='utf-8')
data = f.read()
print(data)
f.close()
'''

print('***********2번째')
fname='2022.05.30 test.txt'

f=open(fname,'r')
print('읽기전',f.tell())
f.seek(0)


f=open(fname,'r')
print('읽기전',f.tell())
for s in f:
    print(s)
f.close()

'''
f=open(fname,'r',encoding='utf-8')
print('읽기 전',f.tell())
data = f.readline()
print('읽기 후',f.tell())
data = f.readline()
print('읽기 후',f.tell())
print(data)
f.close()
'''
'''
print('***********3번째')
fname='2022.05.30 test.txt'
f=open(fname,'r',encoding='utf-8')
data = f.readlines()
print(data)
f.close()
'''


#쓰기함수 write vs writelines
# f.write(문자열)

f= open('2022.05.30 test2.txt','w',encoding='utf-8')
data=['사과','딸기','수박','복숭아']
f.writelines(data)
f.close()

f= open('2022.05.30 test2.txt','r',encoding='utf-8')
if f.writable():
    f.write('내용쓰기')
else:
    print('파일 쓰기 불가')
f.close()
#####################################################

f=open('friends_2022.05.30.txt','r',encoding='utf-8')
data=f.readlines()

f1=[]

for d in data:
    a = d.split(':')
    if a[0]=='Monica':
        f1.append(d)
    else:
        pass

f2='Monica.txt'
f2 = open(f2,'w',encoding='utf-8')
f2.writelines(f1)
f2.close()

f.close()