# uni_20200324.csv 파일을 읽기
# 조건1)사용자로부터 지역 입력받기 region = input()
# 조건2)사용자로부터 표준대계열을 입력받음 kind = input()

#파일열기 : open(), uni_20200324.csv
#파일 한줄읽기 :readline()

'''
for d in f:
    data = r.readline()
    data에 들어오는 문자열
    lst = data.split(',') => 리스트로 리턴
    lst[3]==region 그리고 kind in lst[12]
    새로운 파일에 쓰기(write(data))==> 계속 여는것은 무리임 
'''
#파일닫기 : close(),with문 사용시 생략가능

region=input('지역입력:')
kind = input('표준대계열 입력:')
out_list=[]

with open('uni_20200324.csv','r') as f:
    # 한글 안 깨짐f.read()
    try:
        for data in f:
            dat=f.readline() #한줄의 데이터가 입력
            lst=dat.split(',') 
            #학과 상태가 폐지X => 출력
            #print(lst[11]) => 확인
            if lst[11] != '폐지' and region==lst[3] and kind in lst[12]:
                out_list.append(dat) #새로운 리스트에 append
                
    except:
        print('에러발생')
if len(out_list) >=0:
    f2 =open('2022.06.13 '+region+'.txt','w',encoding='utf-8')
    f2.writelines(out_list)
    f2.close()
    print('추출완료:','2022.06.13 '+region+'.txt')
else:
    print('추출된 정보가 없습니다. ')
