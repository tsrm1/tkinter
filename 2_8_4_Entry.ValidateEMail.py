from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("400x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


def blank_phone_entry():
    phone_entry.delete(0, END)               # удаление введенного текста
    phone_entry.insert(0, blank_text)         # вставка текста по умолчанию

def verifikation_tel(tel='', blank_text="", max_lang=12):
    error_code = 0          # всё ОК
    if tel == blank_text:
        error_code = 1      # данные совпадают с шаблоном (небыло ввода инфо)
    elif len(tel) == 0:
        error_code = 2      # данные отсутствуют
    elif tel[0] != "+":
        error_code = 2      # неверный формат данных
    elif len(tel)>1:
        if not tel[len(tel)-1].isdigit():
            error_code = 3  # недопустимые символы при вводе
    if len(tel)>max_lang:
        error_code = 4
    # error_code = 0 # всё ОК
    # error_code = 1 # данные совпадают с шаблоном (небыло ввода инфо)
    # error_code = 2 # неверный формат данных
    # error_code = 3 # недопустимые символы при вводе
    return error_code


def verifikation_email(mail=''):
    error_code = 0          # всё ОК
    login = mail[0:mail.find("@")]
    domain = mail[mail.find("@")+1:]

    domain_lev1=domain.split(".")
    domain_lev1=domain_lev1[len(domain_lev1)-1]
    
    temp = login + domain
    temp = ''.join(temp.split("_"))
    temp = ''.join(temp.split("."))

    count_sum = len(temp)
    count_digit = 0
    count_char = 0
    for i in range(len(temp)):
        if temp[i].isdigit():
            count_digit +=1
        elif temp[i].isalpha():
            count_char +=1
        else:
            print(f'Wrong symbol in E-Mail -> {temp[i]}')

    if len(login)<2:
        error_code = 1 # Неверный формат логина
    elif domain.find(".") < 1 or len(domain_lev1) < 2:
        error_code = 2 # Неверный формат домена
    elif count_sum != count_digit + count_char:
        error_code = 3 # Неверный набор символов

    # test_mail = aa1a!1a1.2a2_3b3-444_bb4bb@222.333.444
    print("error_code=", error_code)
    return error_code


def is_tel_valid(newval, op):
    print(f'Tel={newval}, P={op}')
    error_code = verifikation_tel(tel=newval)
    if error_code > 0:
        result = False
        if error_code==1:
            phone_entry_errmsg.set("Введите номер телефона!")
        elif error_code==2 or error_code==3:
            phone_entry_errmsg.set("Формат данных +12345678901")
        elif error_code==4:
            phone_entry_errmsg.set("Достигнута максимальная длинна данных!")
        else:
            phone_entry_errmsg.set("")
    else:
        result = True
        phone_entry_errmsg.set("")

    # валидация (focus/focusin/focusout/key)
    if op=="key":
        pass
    # elif op=="focus":
    #     print("Fokus")
    # elif op=="focusin":
    #     print("Fokusin")
    elif op=="focusout" and len(newval) < 12:
        # print("Fokusout")
        blank_phone_entry()
        phone_entry_errmsg.set("Необходимо ввести номер телефона!")
    return result
    
def is_email_valid(newval, op):
    print(f'E-Mail={newval}, P={op}')
    result = True

    if op=="focusout":
        # print("E-Mail Fokusout")
        result = True
        error_code = verifikation_email(mail=newval)
        if error_code > 0:
            result = False
            if error_code==1:
                email_entry_errmsg.set("Неверный формат логина!")
            elif error_code==2:
                email_entry_errmsg.set("Неверный формат домена")
            elif error_code==3:
                email_entry_errmsg.set("Неверный набор символов!")
        else:
            email_entry_errmsg.set("")
        # phone_entry_errmsg.set("")
    return result


blank_text=""

phone_entry_check = (root.register(is_tel_valid), "%P", "%V")
email_entry_check = (root.register(is_email_valid), "%P", "%V")

# значение "%V" представляет событие, 
# которое вызывает валидацию (focus/focusin/focusout/key). 
# Тогда в функции валидации с помощью второго параметра мы сможем получить это значение

phone_entry_errmsg = StringVar()
email_entry_errmsg = StringVar()
 
phone_entry = ttk.Entry(validate="all", validatecommand=phone_entry_check) 
phone_entry.place(x=5, y=5)

 
phone_error_label = ttk.Label(foreground="red", textvariable=phone_entry_errmsg, wraplength=250)
phone_error_label.place(x=140, y=5)

email_entry = ttk.Entry(validate="all", validatecommand=email_entry_check) 
email_entry.place(x=5, y=30)

email_error_label = ttk.Label(foreground="red", textvariable=email_entry_errmsg, wraplength=250)
email_error_label.place(x=140, y=30)
 
another_entry = ttk.Entry() 
another_entry.place(x=5, y=55)
another_entry.focus()               # устанавливаем фокус на поле ввода
 

###############################################################################################
root.mainloop()
