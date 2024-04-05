from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################
 
# # для обработки нажатия на кнопку ее параметру command надо передать функцию, 
# # которая будет вызываться при нажатии на кнопку
# def click(): 
#     print("Hello")
 
# btn = ttk.Button(text="Click", command=click)
# btn.pack()


# ряд встроенных событий Tkinter 
# Activate: окно становится активным.
# Deactivate: окно становится неактивным.
# MouseWheel: прокрутка колеса мыши.
# KeyPress: нажатие клавиши на клавиатуре.
# KeyRelease: освобождение нажатой клавиши
# ButtonPress: нажатие кнопки мыши.
# ButtonRelease: освобождение кнопки мыши.
# Motion: движение мыши.
# Configure: изменение размера и положения виджета
# Destroy: удаление виджета
# FocusIn: получение фокуса
# FocusOut: потеря фокуса.
# Enter: указатель мыши вошел в пределы виджета.
# Leave: указатель мыши покинул виджет.
# <ButtonPress-1> нажатие кнопки мыши, "1" указывает на левую кнопку мыши
# <ButtonPress-3> нажатие кнопки мыши, "3" указывает на правую кнопку мыши


# Привязка событий
# Для привязки события к виджету применяется метод bind(<событие>, функция):


# обработаем события получения и потери фокуса для кнопки:
def entered(event): 
    btn["text"] ="Enter"
 
def left(event): 
    btn["text"] ="Leave"
 
def key_pressed(event): 
    btn["text"] ="Key pressed"
 
def key_released(event): 
    btn["text"] ="Key released"
 
def mouse_wheel(event): 
    btn["text"] ="Mouse wheel"
 
def ButtonPress(event): 
    btn["text"] ="ButtonPress"
 
def ButtonRelease(event): 
    btn["text"] ="ButtonRelease"
 
def Deactivate(event): 
    btn["text"] ="Deactivate"

btn = ttk.Button(text="Click")
btn.pack(anchor=CENTER, expand=1)
 
btn.bind("<Enter>", entered)
btn.bind("<Leave>", left)
btn.bind("<KeyPress>", key_pressed)
btn.bind("<KeyRelease>", key_released)
btn.bind("<MouseWheel>", mouse_wheel)
btn.bind("<ButtonPress>", ButtonPress)
btn.bind("<ButtonRelease>", ButtonRelease)
# root.bind("<Deactivate>", Deactivate)


# Удаление события
# Для открепления события от виджета вызывается метод unbind(), 
# в который передается шаблон события:
# widget.unbind(event)


root.mainloop()


# Модификаторы события
# Часто используемые модификаторы:

# Alt: нажата клавиша Alt
# Control: нажата клавиша Ctrl
# Shift: нажата клавиша Shift
# Any: нажата любая клавиша

# Клавиши
# Также в шаблоне можно указать конкретные клавиши или комбинации. Некоторые из них:
# Alt_L: левая клавиша alt
# Alt_R: правая клавиша alt
# BackSpace: клавиша backspace
# Cancel: клавиша break
# Caps_Lockклавиша CapsLock
# Control_L: левая клавиша control
# Control_R: правая клавиша control
# Delete: клавиша Delete
# Down: клавиша ↓
# End: клавиша end
# Escape: клавиша esc
# Execute: клавиша SysReq
# F1: клавиша F1
# F2: клавиша F2
# Fi: функциональная клавиша Fi
# F12: клавиша F12
# Home: клавиша home
# Insert: клавиша insert
# Left: клавиша ←
# Linefeed: клавиша Linefeed (control-J)
# KP_0: клавиша 0
# KP_1: клавиша 1
# KP_2: клавиша 2
# KP_3: клавиша 3
# KP_4: клавиша 4
# KP_5: клавиша 5
# KP_6: клавиша 6
# KP_7: клавиша 7
# KP_8: клавиша 8
# KP_9: клавиша 9
# KP_Add: клавиша +
# KP_Begin: центральная клавиша (5)
# KP_Decimal: клавиша точка (.)
# KP_Delete: клавиша delete
# KP_Divide: клавиша /
# KP_Down: клавиша ↓
# KP_End: клавиша end
# KP_Enter: клавиша enter
# KP_Home: клавиша home
# KP_Insert: клавиша insert
# KP_Left: клавиша ←
# KP_Multiply: клавиша ×
# KP_Next: клавиша PageDown
# KP_Prior: клавиша PageUp
# KP_Right: клавиша →
# KP_Subtract: клавиша -
# KP_Up: клавиша ↑
# Next: клавиша PageDown
# Num_Lock: клавиша NumLock
# Pause: клавиша pause
# Print: клавиша PrintScrn
# Prior: клавиша PageUp
# Return: клавиша Enter
# Right: клавиша →
# Scroll_Lock: клавиша ScrollLock
# Shift_L: левая клавиша shift
# Shift_R: правая клавиша shift
# Tab: клавиша tab

