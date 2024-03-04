from tkinter import *

win = Tk()
win.title('grid 배치')
#win.geometry('%dx%d'%(100,100))

#동적 레이블생성
lbl_lst=[]
for r in range(3):
    for c in range(3):
        lbl = Label(win,text='('+str(r)+','+str(c)+')',width=5)
        lbl.grid(row=r,column=c)
        lbl_lst.append(lbl)

# lbl_1 = Label(win,text='1',font='arial')
# lbl_1.grid(row=0,column=0)

# lbl_2 = Label(win,text='2',font='arial')
# lbl_2.grid(row=0,column=1)

# lbl_3 = Label(win,text='3',font='arial')
# lbl_3.grid(row=0,column=2)

# lbl_4 = Label(win,text='4',font='arial')
# lbl_4.grid(row=1,column=0)

# lbl_5 = Label(win,text='5',font='arial')
# lbl_5.grid(row=1,column=1)

# lbl_6 = Label(win,text='6',font='arial')
# lbl_6.grid(row=1,column=2)

# lbl_7 = Label(win,text='7',font='arial')
# lbl_7.grid(row=2,column=0)

# lbl_8 = Label(win,text='8',font='arial')
# lbl_8.grid(row=2,column=1)

# lbl_9 = Label(win,text='9',font='arial')
# lbl_9.grid(row=2,column=2)


win.mainloop()