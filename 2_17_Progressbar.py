from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x450+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Progressbar
# Виджет Progressbar предназначен для отображения хода выполнения какого-либо процесса. Основные параметры Progressbar:
# value: текущее значение виджета (тип float)
# maximum: максимальное значение (тип float)
# variable: определяет переменную IntVar/DoublerVar, которая хранит текущее значение виджета
# mode: определяет режим, принимает значения "determinate" (конечный) и "indeterminate" (бесконечный)
# orient: определяет ориентацию виджета, принимает значения "vertical" (вертикальый) и "horizontal" (горизонтальный)
# length: длина виджета

# вертикальный Progressbar
ttk.Progressbar(orient="vertical", length=100, value=40).pack(pady=5)
 
# горизонтальный Progressbar
ttk.Progressbar(orient="horizontal", length=150, value=20).pack(pady=5)

###############################################################################################

# С помощью параметра variable можно привязать значение прогрессбара 
# к переменной типа IntVar или DoublerVar:

value_var = IntVar(value=30)
 
progressbar =  ttk.Progressbar(orient="horizontal", variable=value_var)
progressbar.pack(fill=X, padx=6, pady=6)
 
label = ttk.Label(textvariable=value_var)
label.pack(anchor=NW, padx=6, pady=6)

###############################################################################################

# Методы Progressbar
# Некоторые важные методы виджета:
# start([interval]): запускает перемещение индикатора через определенные интервалы времени. 
# Каждый раз, когда пройдет очередной интервал, индикатор смещается на одно деление вперед. 
# По умолчанию интервал равен 50 миллисекунд
# step([delta]): увеличивает значение индикатора на значение из параметра delta 
# (по умолчанию равен 1.0)
# stop(): останавливает перемещение индикатора

value_var = IntVar()
 
progressbar1 =  ttk.Progressbar(orient="horizontal", variable=value_var)
progressbar1.pack(fill=X, padx=6, pady=6)
 
label = ttk.Label(textvariable=value_var)
label.pack(anchor=NW, padx=6, pady=6)
 
def start(): progressbar1.start(250) # запускаем progressbar, ms
def stop(): progressbar1.stop()      # останавливаем progressbar
 
start_btn = ttk.Button(text="Start", command=start)
start_btn.pack(padx=6, pady=6)
stop_btn = ttk.Button(text="Stop", command=stop)
stop_btn.pack(padx=6, pady=6)

###############################################################################################

# Режим прогрессбара
# Параметр mode отвечает за установку режима прогрессбара и может принимать два значения:

# "indeterminate": прогрессбар показывает индикатор, 
# который перемещается без остановки между двумя краями виджета, 
# то есть фактически бесконечно продолжает перемещение. 
# Данный режим подходит, когда сложно расчитать, 
# насколько должен перемещаться индикатор при отображении хода некоторой задачи

# "determinate": индикатор прогрессбара проходит от начала до конца и затем завершает перемещение. 
# Значение по умолчанию. Подходит для отображения таких процессов, 
# где можно подсчитать перемещение индикатора. 
# Например, копируется 100 файлов, и, если параметр maximum равен 100, 
# при копировании одного файла перемещаем индикатор на одно деление вперед.

# mode="indeterminate"
# По нажатию на кнопку start_btn также запускается процесс. 
# Когда индикатор дойдет до конца, он начинает обратное движение:
progressbar =  ttk.Progressbar(orient="horizontal", mode="indeterminate")
progressbar.pack(fill=X, padx=10, pady=10)
 
start_btn = ttk.Button(text="Start", command=progressbar.start)
start_btn.pack(anchor=SW, side=LEFT, padx=10, pady=10)
 
stop_btn = ttk.Button(text="Stop", command=progressbar.stop)
stop_btn.pack(anchor=SE, side=RIGHT, padx=10, pady=10)



###############################################################################################
root.mainloop()
