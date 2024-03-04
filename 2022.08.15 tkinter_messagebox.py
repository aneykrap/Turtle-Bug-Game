from tkinter import *
from tkinter import messagebox

def btn1_click():
    #확인창
    r = messagebox.showinfo('확인',message='로그인 합니다')
    print(r)

def btn2_click():
    #경고창
    messagebox.showwarning('경고',message='암호화 되지 않았습니다')

def btn3_click():
    #에러
    messagebox.showerror('에러',message='통신중 장애가 발생했습니다.')

def btn4_click():
    #질문
    r = messagebox.askquestion('질문',message='로그인 하시겠습니까?')
    print(r) # yes , no

def btn5_click():
    r = messagebox.askokcancel('질문',message='전송 하시겠습니까?')
    print(r) #True False

def btn6_click():
    r = messagebox.askyesno('질문',message='정보를 등록 하시겠습니까?')
    print(r) #True False

def btn7_click():
    r = messagebox.askretrycancel('확인',message='다시 시도 하시겠습니까?')
    print(r) #True False


win = Tk()
win.title('messagebox 테스트')
win.option_add('*Font','맑은고딕 20')

btn1 = Button(win,text='showinfo',width=30, command=btn1_click)
btn2 = Button(win,text='showwarning',width=30, command=btn2_click)
btn3 = Button(win,text='showerror',width=30, command=btn3_click)
btn4 = Button(win,text='askquestion',width=30, command=btn4_click)
btn5 = Button(win,text='askokcancel',width=30, command=btn5_click)
btn6 = Button(win,text='askyesno',width=30, command=btn6_click)
btn7 = Button(win,text='askretrycancel',width=30, command=btn7_click)

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()

win.mainloop()