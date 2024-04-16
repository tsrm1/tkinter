from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("600x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Темы

# Тема представляет коллекцию стилей. 
# Все стили одно темы проектируются таким образом, 
# чтобы визуально сочетаться друг с другом. 
# Применение определенной темы означает, 
# что к виджетам будут применяться стили из данной темы.

# По умолчанию Tkinter уже предоставляет ряд тем. Чтобы их получить, 
# можно использовать метод theme_names() класса ttk.Style

for theme in ttk.Style().theme_names():
    print(theme)

# winnative
# clam
# alt
# default
# classic
# vista
# xpnative
print("###############################################################################################")


# Для получения текущей темы можно использовать метод theme_use()
current_theme = ttk.Style().theme_use()
print(current_theme)
print("###############################################################################################")

###############################################################################################

# устанавливаем тему "classic"
ttk.Style().theme_use("classic")
 
ttk.Button(text="Click").pack(anchor=CENTER, expand=1)
print(current_theme)
print("###############################################################################################")

###############################################################################################


# выбранная тема
selected_theme = StringVar()
style = ttk.Style()
 
# изменение текущей темы
def change_theme():
    style.theme_use(selected_theme.get())
 
ttk.Label(textvariable=selected_theme, font="Helvetica 13").pack(anchor=NW)
 
for theme in style.theme_names():
    ttk.Radiobutton(text=theme, 
                value=theme,
                variable=selected_theme,
                command=change_theme).pack(anchor=NW)
    
    
###############################################################################################
root.mainloop()