from tkinter import*
# from tkinter import messagebox
#사용자 정보 딕셔너리
user_lst ={ '이황':'123' ,'이이':'456' ,'신사임당':'789'}

def click_btn():
    data_1 = entry_1.get().strip()
    data_2 = entry_2.get().strip()
    result = False

    if data_1=='':
        print('ID를 입력해주세요')
    elif data_2=='':
        print('PASSWORD를 입력해주세요')
    

    #정보를 입력했는지 확인
    if data_1=='' or data_2=='':
        print('로그인 정보를 입력하세요')
    #ID가 회원정보에 있는지 확인 : user_lst 의 키 값에 존재하는 지 체크
    if data_1 in user_lst:
        print('존재함')
    else: 
        print('ID확인 불가 ')
        return result
    #비밀번호도 일치하는지 확인
    if data_2 in user_lst[data_1] == data_2:
        print('비밀번호 일치함')
    else: 
        print('비밀번호 오류')
        return result
    result = True


win = Tk()
win.title('로그인')
win.geometry('%dx%d'%(600,200))

lbl_1 = Label(win,text='ID 입력',font='arial')
lbl_1.place(x=10,y=10)
#lbl_1.pack()

entry_1 = Entry(win,font='arial',bd=5,cursor='pirate',width=31)
entry_1.place(x=200,y=10)
#entry_1.pack()

lbl_2 = Label(win,text='PASSWORD 입력',font='arial')
lbl_2.place(x=10,y=50)
#lbl_2.pack()

entry_2 = Entry(win,font='arial',bd=5,cursor='pirate',width=31)
entry_2.place(x=200,y=50)

#entry_2.pack()

button = Button(win,font='arial',text='로그인',fg='black',cursor='arrow',height=1,width=31,command=click_btn)
button.place(x=10,y=90)
#button.pack()

win.mainloop()