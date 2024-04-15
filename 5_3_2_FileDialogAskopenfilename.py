from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("600x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


# # Диалоговые окна
# # Модуль filedialog предоставляет функциональность файловых диалоговых окон, 
# # которые позволяют выбрать файл или каталог для различных задач. 
# # В частности в модуле для работы с файлами определены следующие функции:

# # askopenfilename(): 
# # открывает диалоговое окно для выбора файла и возвращает путь к выбранному файлу. 
# # Если файл не выбран, возвращается пустая строка ""

# # askopenfilenames(): 
# # открывает диалоговое окно для выбора файлов и возвращает список путей к выбранным файлам. 
# # Если файл не выбран, возвращается пустая строка ""

# # asksaveasfilename(): 
# # открывает диалоговое окно для сохранения файла и возвращает путь к сохраненному файлу. 
# # Если файл не выбран, возвращается пустая строка ""

# # asksaveasfile(): 
# # открывает диалоговое окно для сохранения файла и возвращает сохраненный файл. 
# # Если файл не выбран, возвращается None

# # askdirectory(): 
# # открывает диалоговое окно для выбора каталога и возвращает путь к выбранному каталогу. 
# # Если файл не выбран, возвращается пустая строка ""

# # askopenfile(): 
# # открывает диалоговое окно для выбора файла и возвращает выбранный файл. 
# # Если файл не выбран, возвращается None

# # askopenfiles(): 
# # открывает диалоговое окно для выбора файлов и возвращает список выбранных файлов

# # Эти функции могут принимать ряд параметров:
# # confirmoverwrite: нужно ли подтверждение для перезаписи файла (для диалогового окна сохранения файла)
# # defaultextension: расширение по умолчанию
# # filetypes: шаблоны типов файлов
# # initialdir: стартовый каталог, который открывается в окне
# # initialfile: файл по умолчанию
# # title: заголовок диалогового окна
# # typevariable: переменная, к которой привязан выбранный файл
# # filedialog.askopenfiles(title="Выбор файла", initialdir="D://tkinter", defaultextension="txt", initialfile="hello.txt")


from tkinter import filedialog

root.grid_rowconfigure(index=0, weight=1)
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)
 
text_editor = Text()
text_editor.grid(column=0, columnspan=2, row=0)
 
# открываем файл в текстовое поле
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text =file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)
 
# сохраняем текст из текстового поля в файл
def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)
 
open_button = ttk.Button(text="Открыть файл", command=open_file)
open_button.grid(column=0, row=1, sticky=NSEW, padx=10)
 
save_button = ttk.Button(text="Сохранить файл", command=save_file)
save_button.grid(column=1, row=1, sticky=NSEW, padx=10)


###############################################################################################
root.mainloop()