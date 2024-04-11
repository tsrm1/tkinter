from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Добавление тегов
# Теги позволяют определить форматирование. 
# Тег добавляется с помощью метода add_tag() класса Text:
# tag_add(tagName, index1, index2)

# Первый параметр устанавливает имя тега, 
# второй параметр - index1 указывает на начальный символ, 
# с которого начинает применяться тег. 
# третий параметр - (но необязательно), который устанавливает конечный символ, 
# к которому применяется тег.

# Для прикрепления тега к определенному тексту также можно использовать метод insert, 
# который добавляет текст, и в качестве второго параметра передать тег или набор тегов, 
# которые будут применяться к добавляемому тексту:
# insert(index, text, tagName)
# insert(index, text, (tagName1, tagName2,...tagNameN))

# С помощью метода tag_configure() для тега можно сконфигурировать стили.
# tag_configure(имя_тега, стили)

# Стили представляют параметры 
# background, 
# bgstipple, 
# borderwidth, 
# elide, 
# fgstipple, 
# font, 
# foreground, 
# justify, 
# lmargin1, 
# lmargin2, 
# offset, 
# overstrike, 
# relief, 
# rmargin, 
# spacing1, 
# spacing2, 
# spacing3, 
# tabs, 
# tabstyle, 
# underline
# wrap, 

editor = Text(wrap = "none")
editor.pack(expand=1, fill=BOTH)
editor.insert("1.0","Hello ")
# создаем тег highlightline и прикрепляем его к символам 1.0 до 1.2
editor.tag_add("highlightline", "1.0", "1.2")
# добавляем текст, к которому применяется тег highlightline
editor.insert("end","World", "highlightline")
editor.insert("end","\nHello All!")
# устанавливаем стили тега highlightline
editor.tag_configure("highlightline", background="#ccc", foreground="red", font="TkFixedFont", relief="raised")
 
# # Метод remove_tag() удаляет тег с определенных символов:
# # В данном случае удаляем тег "highlightline" с символов с 0 по 2-й в первой строке.
# editor.tag_remove("highlightline", "1.0", "1.2")

# # удалить тег со всех символов, к которым он применяется:
# editor.tag_delete("highlightline")





###############################################################################################
root.mainloop()
