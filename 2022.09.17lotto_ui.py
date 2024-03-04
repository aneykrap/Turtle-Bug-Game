from tkinter import *
from tkinter import messagebox 
import random as r
import time
import requests
from bs4 import BeautifulSoup

win = Tk()
s_width =410
s_height=400
win.title('lotto')
win.geometry('%dx%d'%(s_width,s_height))
win.option_add('*font','돋음 12')

def get_lottonum(num_str):
    
    ret_data=''
    url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo='
    res = requests.get(url+num_str)
    soup = BeautifulSoup(res.text,'html.parser')

    data=soup.find('div',attrs={'class':'nums'})

    s=data.text
    lst = s.splitlines()

    # print('당첨번호:',lst[4],lst[5],lst[6],lst[7],lst[8],lst[9])
    # print('보너스번호:',lst[14])
    ret_data='당첨번호:'+' '+' '.join(lst[4:10]) +'\n보너스 번호: '+lst[14]

    return ret_data

def get_lottodata():
    num = ent.get().strip()
    if num =='':
        messagebox.showinfo('알림','회차정보를 입력하세요')
        return
    if not num.isnumeric():
        messagebox.showinfo('알림','회차에 숫자를 입력하세요')
        return    

    data = get_lottonum(num)
    lbl_nums['text']=data


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




lbl = Label(win,text='회차정보를 입력하세요')
lbl.grid(row=0,column=0)

ent = Entry(win, justify='right')
ent.grid(row=0,column=1,columnspan=3,sticky=W+E)

btn = Button(win,text='가져오기',command=get_lottodata)
btn.grid(row=0,column=5)

lbl_nums = Label(win,text='당첨번호 :')
lbl_nums.grid(row=2,column=0,columnspan=2)
win.mainloop()