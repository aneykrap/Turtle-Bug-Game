#pickle 라이브러리

# txt,csv => text 파일 => 메모장
# tsv,ini
# smi 자막파일
# pickle 데이터는 파이썬에서 제공하는 형태로써
# text 파일이 아님, 

import pickle
# lst =[1,2,3,4,5]

# with open('2022.07.18 test.txt','wb')as f:
#     pickle.dump( lst  ,f)

# # 위에서 저장한 파일 열기

# with open('2022.07.18 test.txt','rb') as f:
#     data = pickle.load(f)
#     print(data)

#166
a= {1:'a',2:'b',3:'c'}
b=[1,2,3,4,5]

with open('picklefile.bin','wb') as f:
    pickle.dump(a,f)
    pickle.dump(b,f)

with open('picklefile.bin','rb') as f:
    while True:
        try:
            data = pickle.load(f)
            print(data)
        except:
            break

#167
#쓰기
with open('picklefile','wb') as f:
    for i in range(10):
        pickle.dump(i,f)

with open('picklefile','rb') as f:
    while True: 
        try:
            data = pickle.load(f)
            print(data)
        except:
            break

