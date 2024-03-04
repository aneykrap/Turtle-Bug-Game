from tkinter import *
from tkinter import messagebox 
import random as r
import time
win = Tk()
s_width =400
s_height=550
win.title('표적 프로그램')
win.geometry('%dx%d'%(s_width,s_height))
win.option_add('*font','돋음 12')
s_time = 0 #시작시간 저장
c_number = 0 #엔트리에 넣은 숫자값 저장   
g_btn = None #동적으로 생성된 버튼이 저장되는 변수
g_cnt =0
g_color =['yellow','white','green','lightblue','red'] #5
g_pos = [0.2,0.3,0.4,0.5,0.6,0.7,0.8] #7
g_size =1


def click_start(): #필요변수
    global s_time,c_number
    c_number = ent.get().strip() #리턴값 :  문자열

    if c_number=='':
        messagebox.showinfo('알림','입력상자에 원하는 개수를 입력하세요.')
        return
    if not c_number.isdigit():
        messagebox.showinfo('알림','숫자를 입력하세요.')
        return

    c_number=int(c_number) #입력값을 정수형으로 변환

    s_time = time.time()  #시작시간 저장

    #(방법1)윈도우에 객체 제거
    # lbl.destroy()
    # ent.destroy()
    # btn.destroy()
    #(방법2222222222)윈도우에 객체 제거
    for wg in win.grid_slaves():
        wg.destroy()
    create_btn()
    

#동적버튼 생성함수    
def create_btn():
    #pass
    global g_btn,g_cnt,g_size
    if g_btn != None:
        g_btn.destroy()

    if g_cnt == c_number: #몇 초 걸렸는지 알려주기
        #걸린시간 계산
        gap_time=time.time()-s_time
        #레이블생성해서 걸린시간 표시
        lbl_time = Label(win, text='걸린시간'+str(round(gap_time,2)))
        lbl_time.place(relx=0.5,rely=0.5)
        return

    g_cnt +=1   #새로 생성
    g_size=r.randint(1,5)
    g_btn=Button(win,text=str(g_cnt), bg= r.choice(g_color),width=g_size*2, height=g_size, command=create_btn)
    g_btn.place(relx=r.choice(g_pos), rely=r.choice(g_pos))

lbl = Label(win,text='몇 개의 표적을 만들까요?')
lbl.grid(row=0,column=0)

ent = Entry(win, justify='left')
ent.grid(row=0,column=1,columnspan=3,sticky=W+E)

btn = Button(win,text='start',command=click_start)
btn.grid(row=0,column=5)
#exe 만들기
# 인스톨러 라이브러리 필요
#pip list 입력 -> pyinstaller 
#pyinstaller --onefile 'z:\work_python\Yena\2022.09.17 aim.py' 

#설치방법
#명령창에 pip install pyinstaller 
#설치제거
#pip uninstall pyinstaller
win.mainloop()