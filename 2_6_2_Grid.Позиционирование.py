from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


for c in range(2): root.columnconfigure(index=c, weight=1)
for r in range(2): root.rowconfigure(index=r, weight=1)
 
# Объединение ячеек
# Параметр columnspan указывает, столько столбцов, а параметр rowspan сколько строк 
# должен занимать виджет. 


# Растяжение на два столбца:
btn1 = ttk.Button(text="button 1")
# columnspan=2 - растягиваем на два столбца
btn1.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)
btn3 = ttk.Button(text="button 3")
btn3.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)
btn4 = ttk.Button(text="button 4")
btn4.grid(row=1, column=1, ipadx=6,  ipady=6, padx=5, pady=5)


# # Растяжение на две строки:
# btn2 = ttk.Button(text="button 2")
# # rowspan=2 - растягиваем на две строки
# btn2.grid(row=0, column=1, rowspan=2, ipadx=6, ipady=55, padx=5, pady=5)
# btn1 = ttk.Button(text="button 1")
# btn1.grid(row=0, column=0, ipadx=6, ipady=6, padx=5, pady=5)
# btn3 = ttk.Button(text="button 3")
# btn3.grid(row=1, column=0, ipadx=6,  ipady=6, padx=5, pady=5)

# # Параметр sticky задает выравнивание виджета в ячейке, если размер ячейки больше размера этого виджета. Этот параметр может принимать следующие значения:
# # n: положение вверху по центру
# # e: положение в правой части контейнера по центру
# # s: положение внизу по центру
# # w: положение в левой части контейнера по центру
# # nw: положение в верхнем левом углу
# # ne: положение в верхнем правом углу
# # se: положение в нижнем правом углу
# # sw: положение в нижнем левом углу
# # ns: растяжение по вертикали
# # ew: растяжение по горизонтали
# # nsew: растяжение по горизонтали и вертикали
# # По умолчанию виджет позиционируется по центру ячейки
# for r in range(3):
#     for c in range(3):
#         btn = ttk.Button(text=f"({r},{c})")
#         btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4, sticky=NSEW)

root.mainloop()


