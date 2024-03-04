from tkinter import *
from unittest import result
win = Tk()
win.title('계산기')
win.option_add('*font','맑은고딕 15')

btn_lst=[['7','8','9','+'],
         ['4','5','6','-'],
         ['1','2','3','x'],
         ['C','0','=','/']]

def click_calc(s):
    if s =='C':
        ent.delete(0,END)
    elif s =='=':
        sick = ent.get()
        sick = sick.replace('x','*')
        result =eval(sick)
        ent.delete(0,END)
        ent.insert(0,str(result))
    else:
        ent.insert(END,s)

ent = Entry(win, justify='left')
ent.grid(row=0,column=0,columnspan=4,sticky=W+E)

for r in range(len(btn_lst)):
    for c in range(len(btn_lst[r])):
        Button(win,text=btn_lst[r][c],width=5,height=3,command=lambda x=btn_lst[r][c]: click_calc(x)).grid(row=r+1, column=c)

win.mainloop()