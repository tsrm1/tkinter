from tkinter import *
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# есть аналог виджета Text с готовой вертикальной прокруткой - ScrolledText 
# в пакете tkinter.scrolledtext
from tkinter.scrolledtext import ScrolledText

st = ScrolledText(root, width=50,  height=10)
st.pack(fill=BOTH, side=LEFT, expand=True)


###############################################################################################
root.mainloop()

