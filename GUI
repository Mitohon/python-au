import tkinter as tk
import datetime
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title ("Насколько ты младше Владимира Ильича Ленина")
window.geometry('1000x600+200+100')
frame = Frame (
    window,
    padx=10,
    pady=10,
)
frame.pack(expand = True)
t_lb = Label (
    frame,
    text=('Все мы знаем Владимира Ильича Ленина. '
            'Благодаря данной программе вы сможете узнать, сколько времени вам не хватило,'),
    font = 'Comic 12'
)
t_lb.grid ()
t1_lb = Label (
    frame,
    text = (' чтобы родиться в один день с этим человеком'),
    font = 'Comic 12'
)
t1_lb.grid ()
t2_lb = Label (
    frame,
    text = ('(приносим извинения перед теми, кто родился раньше и не имеет возможности воспользоваться калькулятором)'),
    font = 'Comic 12'
)
t2_lb.grid ()
t4_lb = Label (
    frame,
    text = (),
)
t4_lb.grid ()
t3_lb = Label (
    frame,
    text = ('Введите год своего рождения'),
    font = 'Comic 20'
)
t3_lb.grid(row=5, column=0)
b_tf = Entry (
    frame,
)
b_tf.grid(row=6, column=0)
def calculate_tf():
    r=int(b_tf.get())
    r_1 = (r - 1870)
    messagebox.showinfo('Результат', f'Ваша разницы в возрасте составляет {r_1} лет' )
a_btn=Button (
    frame,
    text=('Узнать, насколько я младше'),
    command=calculate_tf
)
a_btn.grid()
window.mainloop()
