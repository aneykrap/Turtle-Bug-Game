from tkinter import *
from tkinter import messagebox
def click_culc():
    #키 받기
    height= entry_1.get().strip()
    #몸무게 받기
    weight= entry_2.get().strip()
    #입력하지 않았을 수도 있고
    if height =='' or weight== '':
        messagebox.showinfo(title='알림',message='키와 몸무게를 반드시 입력해야 합니다.')
        return False
    #입력하긴 했는데 숫자가 아닌 문자 : 문자열 
    if not height.isdigit() or not weight.isdigit():
        messagebox.showinfo(title='알림',message='키와 몸무게를 반드시 입력해야 합니다.')
        return False

    height =int(height)
    weight =int(weight)
    bmi = round(weight/(height/100)**2,2)

    if 0<=bmi<18.5:
        bmi_result=str('저체중')
        fname='bmi1.png'
    elif 18.5<=bmi<25:
        bmi_result=str('표준')
        fname='bmi2.png'
    elif 25<=bmi<30:
        bmi_result=str('과체중')
        fname='bmi3.png'
    elif 30<=bmi<40:
        bmi_result=str('비만')
        fname='bmi4.png'
    elif 40<=bmi:
        bmi_result=str('고도비만')
        fname='bmi5.png'
    bmi = str(bmi)
    lbl_3.config(text=bmi_result+'/ bmi 지수:'+bmi)
    show_bmiimg(fname)


    
def show_bmiimg(fname):
    img = PhotoImage(file= fname, master = win)
    lbl_img.config(image=img,height=300)
    lbl_img.image =img
    lbl_img.update()

win = Tk()
win.title('BMI 계산기')
win.option_add('*font','맑은고딕 15')
#win.geometry('%dx%d'%(500,400))


lbl_1 = Label(win,text='키(cm)',pady=5,justify='right')
lbl_1.grid(row=0,column=0)

lbl_2 = Label(win,text='몸무게(kg)',pady=5,justify='right')
lbl_2.grid(row=1,column=0)

lbl_3 = Label(win,text='BMI 결과',pady=5)
lbl_3.grid(row=3,columnspan=2)

lbl_img = Label(win,text='BMI 이미지',bg ='white',height=10, pady=5)
lbl_img.grid(row=4,columnspan=2,sticky=E+W)

entry_1 = Entry(win,font='arial',bd=5)
entry_1.grid(row=0,column=1)

entry_2 = Entry(win,font='arial',bd=5)
entry_2.grid(row=1,column=1)

button = Button(win,font='arial',text='결과확인',pady=10,command=click_culc)
button.grid(row=2,columnspan=2,sticky=E+W)



win.mainloop()