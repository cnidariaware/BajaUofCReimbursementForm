
import pandas as pd
from tkinter import *

#https://www.geeksforgeeks.org/python-gui-tkinter/

from tkinter import *
form_window = Tk()
form_window.title("Reinbusement Form") 

new_form = Menu(form_window)
new_form.add_command(label='New')

Label(form_window, text='Name (Last name if there is someone who shares your name)').grid(row=0) 
Label(form_window, text='Final Total on reciept $(CAD)').grid(row=1) 
person_name = Entry(form_window, text='Scott Webber') 
amount_CAD = Entry(form_window) 
person_name.grid(row=0, column=1) 
amount_CAD.grid(row=1, column=1) 
mainloop() 

