from tkinter import *
win = Tk()
win.title('음료주문')
win.geometry('%dx%d'%(300,400))

menu={'아메리카노':3500,'코코아':4000,'밀크티':4500,'자몽차':5000,'딸기쉐이크':4800}
order={}
#버튼 누를때마다 order에 추가하는 함수
def menu_order(s):
    if not s in menu:
        print('판매하는 품목이 아님:',s)
    else: 
        if s in order:
            order[s] +=1  #개수를 증가
        else:
            order[s] =1
    #print(order)
    order_show()

#order 총 계산
def order_show():
    tot = 0
    lst = list(order.keys())
    #print('-------------------주문내역----------------------')
    textarea.delete('1.0',END) #text 위젯의 전체내용 삭제
    textarea.insert(END,'-----------------주문내역-----------------\n')
    for i in range(len(lst)):
        name = (lst[i]) # : 사용자가 주문한 품목의 이름
        cnt = order[name] # 사용자가 주문한 수량
        danga = menu[lst[i]] # lst[i]의 단가
        data=(name+':'+ str(cnt)+'*'+str(danga)+'='+format(cnt*danga,',d')+'원')
        textarea.insert(END,data+'\n')
        tot += cnt*danga
    textarea.insert(END,'------------------------------------------\n')
    textarea.insert(END,'총금액:'+format(tot,',d')+'원')

    # order 개수만큼 loop 돌면서 계산 : 주문수량 * 단가 
    # 품목별 소계
    # 전체 모두 합산한 것
    # print 





    

'''
menu_order('아메리카노')
print(order)
menu_order('아메리카노')
print(order)
menu_order('밀크티')
print(order)
'''

#     print('자몽차:',r)
#화면 4개 배치 : 구버전
'''
ack()btn = Button(win,text='아메리카노',fg='black',height=2,width=31,cursor='arrow',command=lambda: menu_order('아메리카노'))
btn.p

btn_2 = Button(win,text='코코아',fg='black',height=2,width=31,cursor='arrow',command=lambda: menu_order('코코아'))
btn_2.pack()

btn_3 = Button(win,text='밀크티',fg='black',height=2,width=31,cursor='arrow',command=lambda: menu_order('밀크티'))
btn_3.pack()

btn_4 = Button(win,text='자몽차',fg='black',height=2,width=31,cursor='arrow',command=lambda: menu_order('자몽차'))
btn_4.pack()
'''
lst = list(menu.keys())
btn_lst=[]
for i in range(len(lst)):
    b=Button(win,text=lst[i],fg='black',height=2,width=31,cursor='arrow',command=lambda x=lst[i]: menu_order(x)).pack()
    btn_lst.append(b)

# 주문내역을 보여줄 Textarea 사용
textarea = Text(win, width=50, height=10, bg='lightblue')
textarea.pack()


win.mainloop()