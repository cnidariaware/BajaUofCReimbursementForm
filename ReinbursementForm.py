
import pandas as pd
import os
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

#holds the location of the file selected when user selects it
global receipt_file
receipt_file = ""

#the window that pops up when trying to submit the
def submit_window():
    form_window = Tk()                          #the window itself
    form_window.title("Reinbursement Form")     #title at the top of the window
    row_counter = 0                             #tkinter uses a grid system with columns and rows

    """
    new_form = Menu(form_window)                #need to be fixed or removed
    new_form.add_command(label='New')           #add commands to remove all tet and deselect files
    """

    Label(form_window, text="This standardizes all of our reciepts that we recieve and logs \nthem away so that we can easily get the money you \nspent on the club back to you.", anchor='w', justify='left').grid(row=row_counter, rowspan=2, columnspan=2)
    row_counter += 2    #takes up two row for text to be visable general instructions
    
    Label(form_window, text="Please put the amount on the reciept we will split the bill on \nfood for you no need to go through mental gymnatics", anchor='w', justify='left').grid(row=row_counter, rowspan=2, columnspan=2)
    row_counter += 2    #takes up 2 twos for text mroe genral instructions

    Label(form_window, text=" ").grid(row=row_counter, columnspan=2)
    row_counter += 1    #fake text for space

    #Text for input
    Label(form_window, text='Name (Last name if there is \nsomeone who shares your name)', anchor='w', justify='left').grid(row=row_counter)
    person_name = Entry(form_window)    #the text box for entires
    person_name.grid(row=row_counter, column=1)
    row_counter += 1    

    Label(form_window, text='Final Total on reciept $(CAD)', anchor='w', justify='left').grid(row=row_counter)
    amount_CAD = Entry(form_window)     #the entry box window for all strings
    amount_CAD.grid(row=row_counter, column=1)  #need to filter for just doubles
    row_counter += 1

    Label(form_window, text='Reason (optional)', justify='left').grid(row=row_counter)
    reason = Entry(form_window)         #the entry box window for all strings
    reason.grid(row=row_counter, column=1)
    row_counter += 1
    
    Label(form_window, text='Picture or PDF or reciept', justify='left').grid(row=row_counter)
    selected_file = Label(form_window, text="", anchor='w', justify='left')
    selected_file.grid(row=row_counter, column=1)
    row_counter += 1
    open_button = Button(form_window, text='Browse...' , command=lambda:select_file(selected_file, receipt_file)).grid(row=row_counter, column=1)
    row_counter += 1    #button for opening window to pick a file

    Button(form_window, text='Submit', command=lambda:submitted(form_window, person_name, amount_CAD, reason), anchor='w', justify='left').grid(row=row_counter)
    row_counter += 1

    form_window.mainloop() 

#function that appends the data to the .xlsx file and makes a copy of the document and places it into the clean up forms so it may be given as evidence
def submitted(window, name_submitted, total_money, reason):
    global receipt_file
    current_time = datetime.now()
    file_submitted_name = f'{name_submitted.get()}{current_time.month:02d}{current_time.day:02d}{current_time.year}{total_money.get()}'

    excel_file = "Reimbursement Data.xlsx"
    subdirectory_name = "Cleaned Up Forms"
    
    file_path = os.path.join(os.getcwd(), subdirectory_name, excel_file)
    
    if not os.path.exists(file_path):
        messagebox.showerror(
            title="Critical Error",
            message="expected file path not found, and expected file not found\n please contact software/logistics team lead"
        )
        window.destroy()
        os._exit(1)

    file_extension = os.path.splitext(file_submitted_name)[1]
    file_submit = f'{file_submitted_name}{file_extension}'
    appended_data = {
        'Name': name_submitted.get(), 
        'Final Total $CAD': total_money.get(),
        'Reason(optional)': reason.get(),
        'Reimbursed (Y/N)': 'N',
        'Receipt File Name': file_submit
        }
    new_data = pd.DataFrame([appended_data], index=[0])
    excel_file_path = file_path

     # Read the existing data from the Excel file
    existing_data = pd.read_excel(excel_file_path)

    # Combine the existing data with the new data
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)

    # Write the combined data back to the Excel file without changing column sizes
    combined_data.to_excel(excel_file_path, index=False)

    file_submit_path = os.path.join(os.getcwd(), subdirectory_name)
    file_extension = os.path.splitext(file_submitted_name)[1]
    file_submit_path = os.path.join(file_submit_path, file_submit)

    new_file_name = os.path.join(file_submit_path, file_submit)
    if os.path.exists(receipt_file):
        # with open(receipt_file, 'r') as input_file:
        with open(receipt_file, 'rb') as input_file:
            # Continue with file operations
            # Read the contents of the input file
            file_contents = input_file.read()

            # Open the new file for writing
        with open(file_submit_path, 'wb') as new_file:
            # Write the contents to the new file
            new_file.write(file_contents)

    else:
            messagebox.showinfo(title="error", message=f"File '{receipt_file}' does not exist.")
        
    messagebox.showinfo(title='Submitted', message='You have successfully submitted')
    return


def select_file(tk_window, selected_file):
    filetypes = (
        ('PDF file', '*.pdf'),
        ('PNG file', '*.png'),
        ('JPEG file', '*.jpeg'),
        ('JPG file', '*.jpg')
    )
    global receipt_file
    receipt_file = fd.askopenfilename(
        title='Open a file',
        filetypes=filetypes)
    if(receipt_file != None):
        messagebox.showinfo(
            title='Selected File',
            message=receipt_file
        )
        formatted_file_name = os.path.basename(receipt_file)
        tk_window["text"] = formatted_file_name
    else:
        messagebox.showinfo(
            title="No selected file",
            message="Please select a file"
        )


if __name__ == "__main__":
    submit_window()