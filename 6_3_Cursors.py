from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("600x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# # Курсоры
# # Tkinter позволяет настроить форму курсора для виджетов. 
# # Для этого у виджетов применяется параметр cursor.

# установка курсора в области окна
root.config(cursor="watch")     

# установка курсора над текстом
ttk.Label(text="Hello World!", cursor="pencil").pack(anchor=CENTER, expand=1)

###############################################################################################

# # Виджеты могут использовать следующие курсоры:
# arrow
# based_arrow_down
# based_arrow_up
# boat
# bogosity
# bottom_left_corner
# bottom_right_corner
# bottom_side
# bottom_tee
# box_spiral
# center_ptr
# circle
# clock
# coffee_mug
# cross
# cross_reverse
# crosshair
# diamond_cross
# dot
# dotbox
# double_arrow
# draft_large
# draft_small
# draped_box
# exchange
# fleur
# gobbler
# gumby
# hand1
# hand2
# heart
# icon
# iron_cross
# left_ptr
# left_side
# left_tee
# leftbutton
# ll_angle
# lr_angle
# man
# middlebutton
# mouse
# pencil
# pirate
# plus
# question_arrow
# right_ptr
# right_side
# right_tee
# rightbutton
# rtl_logo
# sailboat
# sb_down_arrow
# sb_h_double_arrow
# sb_left_arrow
# sb_right_arrow
# sb_up_arrow
# sb_v_double_arrow
# shuttle
# sizing
# spider
# spraycan
# star
# target
# tcross
# top_left_arrow
# top_left_corner
# top_right_corner
# top_side
# top_tee
# trek
# ul_angle
# umbrella
# ur_angle
# watch
# xterm
# X_cursor

###############################################################################################

root.mainloop()