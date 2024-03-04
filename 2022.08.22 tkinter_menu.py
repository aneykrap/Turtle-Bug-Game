from re import sub
from tkinter import *
#tkinter 메뉴 만들기
# 1. 메뉴바 만들기 ==> 윈도우에 붙임
# 2. 상위 메뉴를 만들어서 메뉴바 붙임
# 3. 하위메뉴를 만들어서 상위메뉴에 붙임

win =Tk()
win.title('메뉴만들기 연습')
win.geometry('500x500')

# 메뉴바 만들기
menubar = Menu(win)
win.config(menu=menubar)


# 메뉴 추가하기
mnu1 = Menu(menubar,tearoff=0)
mnu1.add_command(label='새로 만들기')
mnu1.add_command(label='새창')
mnu1.add_command(label='열기')
mnu1.add_command(label='저장')
mnu1.add_command(label='다른이름으로 저장')
mnu1.add_separator()
mnu1.add_command(label='페이지 설정')
mnu1.add_command(label='인쇄')
mnu1.add_separator()
mnu1.add_command(label='끝내기')

mnu2 = Menu(menubar,tearoff=0)
mnu2.add_command(label='실행취소')
mnu2.add_separator()
mnu2.add_command(label='복사')
mnu2.add_command(label='붙여넣기')
mnu2.add_command(label='삭제')
mnu2.add_separator()
mnu2.add_command(label='Bing으로 검색')
mnu2.add_command(label='찾기')
mnu2.add_command(label='다음 찾기')
mnu2.add_command(label='이전 찾기')
mnu2.add_command(label='바꾸기')
mnu2.add_command(label='이동')
mnu2.add_separator()
mnu2.add_command(label='모두선택')
mnu2.add_command(label='시간/날짜')

mnu3 = Menu(menubar,tearoff=0)
mnu3.add_command(label='자동 줄 바꿈(w)')
mnu3.add_command(label='글꼴(F)')

mnu4 = Menu(menubar,tearoff=0)

sub_menu = Menu(mnu4,tearoff=0)
sub_menu.add_cascade(label='확대하기/축소하기')

#mnu4.add_command(label='확대하기/축소하기') # 서브 메뉴가 붙어있는 경우
mnu4.add_cascade(label='확대하기/축소하기',menu=sub_menu)
sub_menu.add_command(label='확대')
sub_menu.add_command(label='축소')
sub_menu.add_command(label='확대하기/축소하기 기본값 복원')

mnu4.add_checkbutton(label='상태 표시줄(S)') #체크표시 버튼


mnu5 = Menu(menubar,tearoff=0)
mnu5.add_command(label='도움말 보기(H)')
mnu5.add_command(label='피드백 보내기(F)')
mnu5.add_separator()
mnu5.add_command(label='메모장 정보(A)')

menubar.add_cascade(label='파일',menu=mnu1)
menubar.add_cascade(label='편집',menu=mnu2)
menubar.add_cascade(label='서식',menu=mnu3)
menubar.add_cascade(label='보기',menu=mnu4)
menubar.add_cascade(label='도움말',menu=mnu5)

win.mainloop()