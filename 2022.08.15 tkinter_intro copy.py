# tkinter 라이브러리
# GUI : 그래픽 유저 인터페이스
# GUI를 제공하는 라이브러리

#기본적인 위젯 (컨트롤)
#Button (버튼)
#Label 
#CheckButton
#Radio Button(택 1만)
#Entry (엔트리,1줄 입력상자)
#Text (여러줄 입력상자)
#Menu (메뉴)
#Menubutto(메뉴에 들어가는 서브 메뉴)
#Frame

# #기본적인 화면 만들기
# from tkinter import*
# #윈도우 새롭게 생성
# #기본 윈도우 창이 생성(최소,최대,닫기),아이콘,타이틀

# win = Tk()
# s_width = 800
# s_height = 600

# # 윈도우 사이즈(크기)

# win.geometry('%dx%d'%(s_width,s_height))

# #윈도우 창의 제목주기
# win.title('나의 첫번째 윈도우')

# def click_btn():
#     print('버튼 눌렸다!!')
#     win.destroy()
#     win.quit()

# #기본 폰트 설정
# win.option_add('*Font','맑은고딕 20')

# #레이블
# lbl = Label(win,text='나는 파이썬이 좋아')
# lbl.pack()

# #입력상자
# txt = Entry(win)
# txt.pack()

# #버튼
# btn = Button(win,text='동의합니다')
# btn.pack()

# btn_close = Button(win,text='닫기',command=click_btn)
# btn_close.pack()


# from tkinter import*

# win = Tk()
# # s_width = 800
# # s_height = 600

# # win.geometry('%dx%d'%(s_width,s_height))

# lbl = Label(win,text='Welcome, Please input your name',bg='yellow',fg ='blue')
# lbl.pack()

# txt = Entry(win)
# txt.pack()

# btn = Button(win,text='확인',bg = 'orange',height=5,width=20, cursor='pirate')
# btn.pack()


# win.mainloop()

#193 레이블,엔트리,버튼 배치하기
from tkinter import*

def click_btn():
    data = entry.get()  
    print(data)
    button['fg'] =data


win = Tk()

lbl = Label(win,text='Welcome, Please input your name',bg='beige',font='arial')
lbl.pack()

entry = Entry(win,font='arial',text='input here',bd=5,cursor='pirate',width=31)
entry.pack()

button = Button(win,font='arial',text='확인',fg='red',cursor='arrow',height=1,width=31,command=click_btn)
button.pack()


win.mainloop()

# a ='Welcome, Please input your name'

# print(len(a))

import sys 
import random 

