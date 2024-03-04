# 2022년 5월 기준
# 세대수가 50만 이상인 시군구만 추출
#1. 11 입력 => 서울 해당내용 나옴
#2. 세대수를 사용자 입력 , 5월 기준 입력 세대수 이상
''' ********** 1번임 ***************
code_1 = input('시군구 코드를 입력하세요')


with open('최종1_행정구역_시군구_별_주민등록세대수_20220620194517.csv','r',encoding='utf-8') as f:
    for data in f:
        dat=f.readline() #한줄의 데이터가 입력
        lst = dat.split(',')
        #print(lst)
        lst1=lst[0].split(' ')
        #print(lst1)
        #print(lst1[0])
        if lst1[0][:2] == code_1 :
            print(dat)
        #lst1=lst[0].split(' ')
        #lst1==code_1:
            #print(dat)

'''

#2번 
code_2 = input('세대수(5월 기준)를 입력하세요')
file_list=[]
i=0

with open('최종1_행정구역_시군구_별_주민등록세대수_20220620194517.csv','r',encoding='utf-8') as f:
    for data in f:
        if i!=0:
            #dat=f.readline() #한줄의 데이터가 입력
            lst = data.split(',')
            lst1 = lst[0].split(' ')
            if int(lst[4])>= int(code_2) and len(lst1[0])==5:
                file_list.append(data)
        i+=1

f2 =open('2022.06.20 test.txt','w',encoding='utf-8')
f2.writelines(file_list)
f2.close()




