import random as r

f= open('2022.06.27 data.txt','r',encoding='utf-8')
data_lst = f.readlines()
f.close()
ask = []
answer = []

#문제 구성
for i in range(len(data_lst)):
    lst = data_lst[i].split('|')
    #lst[0]=>번호 lst[1]=>문제 lst[2]=>정답
    ask.append(lst[1].strip())
    answer.append(lst[2].strip())

#사용자에게 문제 내기
while True :
    n = r.randint(1,len(ask))
    s = input(ask[n])
    if s == answer[n]:
        print('이 어려운걸 맞히다니! 천재')
    else:
        print('문제의 정답은', answer[n] )

