#1 
'''
a=[1,2,3]
try:
    print(a[4])   
except:
    print('에러발생')

#2
brith ={'홍길동':'2000년 3월 1일','김춘추':'604년'}
a = input('생일을 알고 싶은 사람을 입력하세요:')    

try:
    print(brith[a])
except:
    print('데이터베이스에 존재하지 않는 이름입니다.')

#3
hp=280
print('현재 체력은',hp,'입니다.')
hit = 0

while hit != 'save':
    hit = (input('데미지를 몇 입었습니까?'))
    if hit == 'save':
        f= open('save.txt','w',encoding='utf-8')
        f.write(str(hp))
        f.close()

    else:
        hit=int(hit)
        hp=hp-hit
        print('체력이 %d 남았습니다.'%hp)

#4
try:
    print('세이브 된 파일을 불러오는 중...')
    f= open('save.txt','r',encoding='utf-8')
    hp= int(f.read())
    print('현재 체력은',hp,'입니다.')
    f.close()

except:
    print('파일을 찾을 수 없습니다.')

'''

#5

f= open('score.txt','r',encoding='utf-8')
score_list=[]

for data in f:   
    score_list.append(int(data))

score_sum = sum(score_list)
score_average = score_sum/len(score_list)

print('전체 합은 %d 입니다.'%score_sum)
print('전체 평균은 %d 입니다.'%score_average)

#6
'''
nation = ['한국','미국','일본','중국','러시아','베트남']

a= input('나라 이름을 입력하세요:')
try:


except:
    f = open('ErrorLog.txt','a',encoding='utf-8')
    f.write()
    f.close()

'''


