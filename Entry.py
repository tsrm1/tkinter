from tkinter import *


def char_validate(d, P):
    pattern = "c.create_text(100, 100, text='Текст')"
    if d == '1':
        if P == pattern:
            print('Alles richtig.')
        elif pattern.startswith(P):
            print('Schreib weiter ...')
        else:
            print('Incorrekt symbol!')
    return True


root = Tk()
root.geometry('300x400')

field_check = (root.register(char_validate), "%d", "%P")
c = Canvas(root)

c.create_text(100, 100, text='Text')
c.pack()

field = Entry(validate="key", validatecommand=field_check)
field.pack()

root.mainloop()