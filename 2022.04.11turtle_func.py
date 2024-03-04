from tkinter import mainloop
import turtle as t


def draw_line(x,y):
    t.pendown()
    t.goto(x,y)

# (0,0) 스크린의 정가운데에 turtle 이 위치하게 됨

t.onscreenclick(draw_line)

















mainloop()