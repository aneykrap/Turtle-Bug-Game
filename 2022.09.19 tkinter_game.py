# 창크기 :1000*500
# 제목 : 도형 달리기

import time
from tkinter import *
import random as r

title = '도형 달리기'
s_width,s_height =1000,500
start_x, end_x =20, s_width-20
start_tm =0 #스페이스바를 눌렀을 때 시간

#시작여부 flag
play = False
#키보드 눌렸을때 호출되는 함수
def press_key(event):
    global play,start_tm
    if event.keysym=='space':
        play = True
        start_tm = time.time()


#출발선과 도착선 좌표

win = Tk()
s_width,s_height =1000,500
title = '도형 달리기'
win.title(title)
win.geometry('%dx%d'%(s_width,s_height))
win.resizable(False,False) #창크기 변경불가
win.bind('<KeyPress>',press_key)#(이벤트명, 함수명)

#출발선과 도착선 좌표
start_x, end_x =20, s_width-20
start_tm =0 #스페이스바를 눌렀을 때 시간


#캔버스 붙이기
cvs = Canvas(win)
cvs.config(width = s_width, height=s_height)
cvs.pack()

#안내 메세지 나타내기
text=cvs.create_text((s_width/2,20),text='시작하려면 스페이스바를 눌러주세요')

#도형 2개 그리기
#첫번째 도형
x1,y1 = start_x, int(s_height/3)
rect1= cvs.create_rectangle(x1,y1,x1+40,y1+40,fill='red')

#두번째 도형 : 첫번째 도형보다 아래, blue
x2,y2 = start_x, int((s_height/3)*1.8)
rect2= cvs.create_rectangle(x2,y2,x2+40,y2+40,fill='blue')

while True:
    if play :
        #기존의 정보 모두 지우기
        cvs.delete(rect1,rect2, text)

        #얼마만큼 이동할 것인지 계산
        x1+= r.randint(5,20)
        rect1= cvs.create_rectangle(x1,y1,x1+40,y1+40,fill='red')

        #두번째 도형 : 첫번째 도형보다 아래, blue
        x2+= r.randint(5,20)
        rect2= cvs.create_rectangle(x2,y2,x2+40,y2+40,fill='blue')

        time.sleep(1/15) # 1/27초

        #결승선에 도착한 도형이 있으면 게임 종료
        #두 사각형의 x좌표값과 end_x 값을 비교해서 결승선에 도착했는지 검사
        if  x1+40 >= end_x :
            play = False
            gap_time = time.time()-start_tm
            gap_time = round(gap_time,2)
            gap_time = str(gap_time)
            cvs.create_text((s_width/2,20),text='[빨강 승리!! 도착!] == 기록:'+gap_time)
            break
        elif x2+40 >= end_x :
            play = False
            gap_time = time.time()-start_tm
            gap_time = round(gap_time,2)
            gap_time = str(gap_time)
            cvs.create_text((s_width/2,20),text='[빨강 승리!! 도착!] == 기록:'+gap_time)        
            break
        #새로 그리기
    win.update()
print('end')
win.mainloop()
        