#,for 문
#[1,2,3........]print(i)
#while 문
#   주의사상 무한루프에 빠지지 않도록 
'''i=1
while i <=10:
    print(i)
    i+=1
for i in range(1,11):'''

#
# i = 1
# while True:
#     print(i)
#     i +=1   
#     if i == 11:
#         break

#2) while문과 함께 알아야 할 continue
'''i=0
while i <=100:#짝수만 출력
    # if i%2==0:
    #      print(i)
    i += 1
    if i%2==1:
        continue
    
    print(i)
'''

#구구단
#2단
'''dan = 2
i=1
while i <10:
    print(dan,'x',i,'=',dan*i)
    i +=1
'''
#2단부터 9단까지
'''''
dan = 2
while dan < 10:
    i= 1
    while i <10:
        print(dan,'x',i,'=',dan*i,end='\t')
        i +=1
    print()
    dan +=1

'''

#for문 2단
#dan = 2
for dan in range(2,10):
    for i in range(1,10):
        print(dan,'x',i,'=',dan*i,end = '\t')
    print()
