from tkinter import *
import models.CalcHandler as ch
from models.Stock import Stock

window = Tk()
frame_a = Frame()
frame_b = Frame()

class Table:
     
    def __init__(self,root, total_rows, total_columns, lst):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='green',
                               font=('Arial',20,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

def submit():
    ticker = entry.get()
    options = []
    stock = Stock(ticker)
    list_options = ch.getOptions(stock)
    list_options = ch.rankOptions(list_options)
    for option in list_options:
        option_tuple = (option.optionType, option.maturity_date, option.exercise_price)
        options.append(option_tuple)
    total_rows = len(options)
    total_columns = len(options[0])
    t = Table(frame_a, total_rows, total_columns, options)
    t.pack()
    frame_a.pack()
    entry.set("")

entry = Entry(master=frame_b)
entry.pack()
sub_btn=Button(master=frame_b,text = 'Submit', command = submit)
sub_btn.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()

