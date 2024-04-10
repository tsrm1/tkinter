from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
# from tkinter import messagebox              # подключаем пакет Окно сообщений

root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("360x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Notebook. Создание вкладок
# Виджет Notebook представляет набор вкладок. 
# параметры виджета следующие:
# width: ширина виджета
# height: высота виджета
# cursor: курсор при наведении на виджет
# padding: отступы от границ виджета до его содержимого
# style: стиль виджета
# создаем набор вкладок

# Для управления вкладками Notebook предоставляет ряд методов:

# для добавления вкладки применяется метод add()
# add(child, state, sticky, padding, text, image, compound, underline)
# Параметры метода
# child: добавляемый виджет, для которого собственно и создается вкладка. Обычно это Frame, который затем добавляет другие виджеты
# state: состояние вкладки. Возможные значения: "normal", "disabled", "hidden"
# sticky: определяет прикрепление виджета к определенной стороне вкладки
# padding: отступы от границ вкладки до внутреннего содержимого
# text: заголовок вкладки
# image: изображение в заголовке вкладке
# compound: управляет расположением изображения и текста в заголовке вкладки
# underline: определяет номер подчеркнутого символа в заголовке вкладки

# Кроме того, чтобы скрыть временно вкладку, применяется метод hide()
# В качестве параметра принимает идентификатор вкладки, 
# который по умолчанию представляет числовой индекс вкладки начиная с 0
# hide(tabId)

# Чтобы совсем удалить вкладку, применяется метод forget()
# forget(child)

# Добавление изображений
# За установку изображения в заголовке вкладки отвечает параметр image метода add. Кроме того, с помощью параметра compound можно задать расположение картинки относительно текста. В частности, параметр compound может принимать следующие значения:
# top: изображение поверх текста
# bottom: изображение под текстом
# left: изображение слева от текста
# right: изображение справа от текста
# none: при наличии изображения отображается только изображение
# text: отображается только текст
# image: отображается только изображение


notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
 
# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
 
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)
 
# # добавляем фреймы в качестве вкладок. Название вкладок без изображений
# notebook.add(frame1, text="Python")
# notebook.add(frame2, text="Java")

# Импортируем изображения
WhatsUp_logo = PhotoImage(file="./ico/whatsup.png")
Telegram_logo = PhotoImage(file="./ico/telegram.png")
Viber_logo = PhotoImage(file="./ico/viber.png")

# добавляем фреймы в качестве вкладок. Название вкладок с изображением
notebook.add(frame1, text="WhatsUp", image=WhatsUp_logo, compound=LEFT)
notebook.add(frame2, text="Telegram", image=Telegram_logo, compound=LEFT)
notebook.add(frame3, text="Viber", image=Viber_logo, compound=LEFT)






###############################################################################################
root.mainloop()
