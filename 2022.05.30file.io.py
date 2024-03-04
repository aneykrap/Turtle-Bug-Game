#파일 다루기: 읽고 쓰기

#텍스트 파일
#ini 소프트웨어 구동될 때 사용되는 텍스트 파일
#txt 메모장에서 읽기 가능
#csv 콤마 구분자로 데이터가 들어가 있는 경우
#    이름,성별,나이. 주소
#    홍길동,남,18,남원
#tsv 탭 구분자로 데이터
#    이름   성별    나이    주소
#    홍길동 남  16  남원 
# 탭()대신에 프로그램에서 읽었을때 \t

#파이썬 내장함수로 제공/import 사용하지 않고 가능
#열기함수 : open()
#닫기함수 : close()
#읽기     : read()
#쓰기     : write()
#encoding 옵션에서 한글깨짐을 방지하려면 다음의 3가지 기억
#1) utf-8
#2) cp949
#3) euc-kr

#1)파일생성
f = open('2022.05.30 test.txt','w',encoding='utf-8')
#open(파일명,모드,인코딩)
#                   w: write(쓰기)-없으면 만들고 있으면 덮어쓴다. (오버라이트)
#                   r: read (읽기전용)-오직 읽기만 가능,쓰기하면 에러
#                   a:apeend(추가)-기존파일에 추가

f.write('오늘만든 텍스트 파일이지.')
f.close()

#2) 생성한 파일 읽기
'''
fname='2022.05.30 test.txt'
f= open(fname,'r',encoding='utf-8')
data =f.read()
print(data)



'''
#f.write('내용을 추가하려고 합니다.') #에러:r로 열어서

f.close()
'''
#3) 파일에 내용 추가하기
f=open(fname,'a',encoding='utf-8')
f.write('\n내용추가')
f.close()

'''

f=open('num.txt','w',encoding='utf-8')
for i in range(1,11):
    data= '%d번째 줄입니다.\n'%i
    f.write(data)
f.close()

f=open('add_data.txt','a',encoding='utf-8')
for i in range(1,101):
    data='\t%d'%i
    f.write(data)
f.close()


f=open('exp.txt','w',encoding='utf-8')
for i in range(1,6):
    data='제%d의 아해가 무섭다고 그리오\n'%i
    f.write(data)
f.close()
    