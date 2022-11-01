from tkinter import *

import models.CalcHandler as ch
from models.Stock import Stock

window = Tk()
window.geometry("1100x400")
window.eval('tk::PlaceWindow . center')
frame_aa = Frame()
frame_a = Frame()
frame_b = Frame()

#creates a class table
class Table:
     
    def __init__(self,root, total_rows, total_columns, lst):
         
        # code for creating table
        for i in range(total_rows):
            #For first row aka headers
            if i == 0:
                for j in range(total_columns):
                    self.e = Entry(root, width=20, fg='yellow',
                               font=('Arial',20,'bold'))
                 
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])
            else:
                #Rest 
                for j in range(total_columns):
                    
                    self.e = Entry(root, width=20, fg='green',
                                font=('Arial',20,'bold'))
                    
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])

#When button clicked calculates options and creates table
def submit():
    ticker = entry.get().upper()
    entry.delete(0, 'end')
    label.config(text=ticker)
    options = [("Rank", "Option Type", "Maturity date", "Exercise price")]
    stock = Stock(ticker)
    list_options = ch.getOptions(stock)
    list_options = ch.rankOptions(list_options)
    for i, option in enumerate(reversed(list_options)):
        option_tuple = (str(i + 1), option.optionType, option.maturity_date, '$' + str(round(option.exercise_price, 2)))
        options.append(option_tuple)
    total_rows = len(options)
    total_columns = len(options[0])
    t = Table(frame_a, total_rows, total_columns, options)
    t.pack()
    frame_a.pack()

#GUI components
label = Label(master=frame_aa, text = "Stock", font=("Helvetica", 20))
label.pack()
entry = Entry(master=frame_b)
entry.pack()
sub_btn=Button(master=frame_b,text = 'Submit', command = submit)
sub_btn.pack()

frame_aa.pack()
frame_a.pack()
frame_b.pack()

window.title("Option predictor")
window.mainloop()

