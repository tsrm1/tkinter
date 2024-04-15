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

def choose_file():
    filepath = filedialog.askopenfilename()
    text_editor.delete("1.0", END)
    text_editor.insert("1.0", filepath)

def choose_files():
    filepath = filedialog.askopenfilenames()
    text_editor.delete("1.0", END)
    text_editor.insert("1.0", filepath)

def save_filename():
    filepath = filedialog.asksaveasfilename()
    text_editor.delete("1.0", END)
    text_editor.insert("1.0", filepath)

def save_as_file():
    filepath = filedialog.asksaveasfile()
    text_editor.delete("1.0", END)
    text_editor.insert("1.0", filepath)

def open_directory():
    filepath = filedialog.askdirectory()
    text_editor.delete("1.0", END)
    text_editor.insert("1.0", filepath)

def open_file():
    filepath = filedialog.askopenfile()
    text_editor.delete("1.0", END)
    text_editor.insert("1.0", filepath)

def open_files():
    filepath = filedialog.askopenfiles()
    text_editor.delete("1.0", END)
    text_editor.insert("1.0", filepath)


askopenfilename_button = ttk.Button(text="Выбрать файл", command=choose_file)
askopenfilename_button.grid(column=0, row=1, sticky=NSEW, padx=10)


askopenfilenames_button = ttk.Button(text="Выбрать файлы", command=choose_files)
askopenfilenames_button.grid(column=1, row=1, sticky=NSEW, padx=10)


asksaveasfilename_button = ttk.Button(text="Выбрать файл", command=save_filename)
asksaveasfilename_button.grid(column=0, row=2, sticky=NSEW, padx=10)


asksaveasfile_button = ttk.Button(text="Выбрать файлы", command=save_as_file)
asksaveasfile_button.grid(column=1, row=2, sticky=NSEW, padx=10)


askdirectory_button = ttk.Button(text="Выбрать каталог", command=open_directory)
askdirectory_button.grid(column=0, row=3, sticky=NSEW, padx=10)


askopenfile_button = ttk.Button(text="Выбрать файл", command=open_file)
askopenfile_button.grid(column=0, row=4, sticky=NSEW, padx=10)


askopenfiles_button = ttk.Button(text="Выбрать файлы", command=open_files)
askopenfiles_button.grid(column=1, row=4, sticky=NSEW, padx=10)



###############################################################################################
root.mainloop()