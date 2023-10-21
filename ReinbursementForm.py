
import pandas as pd
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

#https://www.geeksforgeeks.org/python-gui-tkinter/

receipt_file = 0



def submit_window():
    form_window = Tk()
    form_window.title("Reinbursement Form") 
    row_counter = 0

    new_form = Menu(form_window)
    new_form.add_command(label='New')

    Label(form_window, text="This standardizes all of our reciepts that we recieve and logs \nthem away so that we can easily get the money you \nspent on the club back to you.", anchor='w', justify='left').grid(row=row_counter, rowspan=2, columnspan=2)
    row_counter += 2
    
    Label(form_window, text="Please put the amount on the reciept we will split the bill on \nfood for you no need to go through mental gymnatics", anchor='w', justify='left').grid(row=row_counter, rowspan=2, columnspan=2)
    row_counter += 2

    Label(form_window, text=" ").grid(row=row_counter, columnspan=2)
    row_counter += 1

    Label(form_window, text='Name (Last name if there is \nsomeone who shares your name)', anchor='w', justify='left').grid(row=row_counter)
    person_name = Entry(form_window)
    person_name.grid(row=row_counter, column=1)
    row_counter += 1

    Label(form_window, text='Final Total on reciept $(CAD)', anchor='w', justify='left').grid(row=row_counter)
    amount_CAD = Entry(form_window)
    amount_CAD.grid(row=row_counter, column=1)
    row_counter += 1

    Label(form_window, text='Reason (optional)', justify='left').grid(row=row_counter)
    reason = Entry(form_window)
    reason.grid(row=row_counter, column=1)
    row_counter += 1
    
    Label(form_window, text='Picture or PDF or reciept', justify='left').grid(row=row_counter)
    selected_file = Label(form_window, text="", anchor='w', justify='left')
    selected_file.grid(row=row_counter, column=1)
    row_counter += 1
    open_button = Button(form_window, text='Browse...' , command=lambda:select_file(selected_file, receipt_file)).grid(row=row_counter, column=1)
    row_counter += 1


    Button(form_window, text='Submit', command=lambda:submitted(), anchor='w', justify='left').grid(row=row_counter)
    row_counter += 1

    mainloop() 

def submitted():
    #add pandas for excell file input
    messagebox.showinfo(title='Submitted', message='You have successfully submitted')


def select_file(tk_window, select_file):
    filetypes = (
        ('PDF file', '*.pdf'),
        ('PNG file', '*.png'),
        ('JPEG file', '*.jpeg'),
        ('JPG file', '*.jpg')
    )

    file_name = fd.askopenfilename(
        title='Open a file',
        filetypes=filetypes)
    if(file_name != None):
        messagebox.showinfo(
            title='Selected File',
            message=file_name
        )
        select_file = file_name
        formatted_file_name = os.path.basename(file_name)
        tk_window["text"] = formatted_file_name
    else:
        messagebox.showinfo(
            title="No selected file",
            message="Please select a file"
        )


if __name__ == "__main__":
    submit_window()