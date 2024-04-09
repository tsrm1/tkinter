from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("100x550+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(100,550)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################
position = {"padx":1, "pady":1, "anchor":NW}
 
facebook = "facebook"
linkedin = "linkedin"
mail = "mail"
teams = "teams"
telegram = "telegram"
viber = "viber"
whatsup = "whatsup"
 
messenger = StringVar(value=facebook)    # по умолчанию будет выбран элемент с value=java
 
header = ttk.Label(textvariable=messenger)
header.pack(**position)
 
facebook_img = PhotoImage(file="./ico/facebook.png")
linkedin_img = PhotoImage(file="./ico/linkedin.png")
mail_img = PhotoImage(file="./ico/mail.png")
teams_img = PhotoImage(file="./ico/teams.png")
telegram_img = PhotoImage(file="./ico/telegram.png")
viber_img = PhotoImage(file="./ico/viber.png")
whatsup_img = PhotoImage(file="./ico/whatsup.png")
  
facebook_btn = ttk.Radiobutton( value=facebook, variable=messenger, image=facebook_img)
facebook_btn.pack(**position)
  
linkedin_btn = ttk.Radiobutton(value=linkedin, variable=messenger, image=linkedin_img)
linkedin_btn.pack(**position)
 
java_btn = ttk.Radiobutton(value=mail, variable=messenger, image=mail_img)
java_btn.pack(**position)

teams_btn = ttk.Radiobutton(value=teams, variable=messenger, image=teams_img)
teams_btn.pack(**position)

telegram_btn = ttk.Radiobutton(value=telegram, variable=messenger, image=telegram_img)
telegram_btn.pack(**position)

viber_btn = ttk.Radiobutton(value=viber, variable=messenger, image=viber_img)
viber_btn.pack(**position)

whatsup_btn = ttk.Radiobutton(value=whatsup, variable=messenger, image=whatsup_img)
whatsup_btn.pack(**position)


###############################################################################################
root.mainloop()
