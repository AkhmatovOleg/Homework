import tkinter
import os

from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберете файл",
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] = text['text'] + filename
    os.startfile(filename)


window = tkinter.Tk()
window.title('Проводник', )
window.geometry('600x150')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл', height=4, width=90, background="silver", foreground='green')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=40, height=2, text='Выбрать файл', foreground='green',
                               command=file_select)
button_select.grid(column=1, row=2, pady=10)

window.mainloop()
