from tkinter import *


# Создаём окно
wnd = Tk()

# Создаём функции для кнопок
def function1():
    lbl1["text"] = "Мяу"

def function2():
    lbl2["text"] = "Мур"

# Создаём кнопки
btn1 = Button(wnd, command=function1, text = "Помяукать")
btn2 = Button(wnd, command=function2, text = "Помурчать")

#Создаём текстовые метки
lbl1 = Label(wnd)
lbl2 = Label(wnd)

# Отображение элементов в окне
btn1.pack()
btn2.pack()
lbl1.pack()
lbl2.pack()

# Показ окна
wnd.mainloop()