
import pandas as pd
import os
from datetime import datetime
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

    Button(form_window, text='Submit', command=lambda:submitted(form_window, person_name, amount_CAD, reason, selected_file), anchor='w', justify='left').grid(row=row_counter)
    row_counter += 1

    form_window.mainloop() 

def submitted(window, name_submitted, total_money, reason, proof_of_payment):
    current_time = datetime.now()
    file_submitted_name = f'{name_submitted.get()}{current_time.month:02d}{current_time.day:02d}{current_time.year}{total_money.get()}'
    #file_submitted_name = proof_of_payment.cget("text")

    file_name = "Reimbursement Data.xlsx"
    subdirectory_name = "Cleaned Up Forms"
    
    file_path = os.path.join(os.getcwd(), subdirectory_name, file_name)
    
    if not os.path.exists(file_path):
        messagebox.showerror(
            title="Critical Error",
            message="expected file path not found, and expected file not found\n please contact software/logistics team lead"
        )
        window.destroy()
        os._exit(1)

    appended_data = {
        'Name': name_submitted.get(), 
        'Final Total $CAD': total_money.get(),
        'Reason(optional)': reason.get(),
        'Reimbursed (Y/N)': 'N',
        'Receipt File Name': file_submitted_name
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
    file_submit = f'{file_submitted_name}{file_extension}'

    new_file_name = os.path.join(file_submit_path, file_submit)
    with open(receipt_file, 'r') as input_file:
        # Read the contents of the input file
        file_contents = input_file.read()

    # Open the new file for writing
    with open(file_submit, 'w') as new_file:
        # Write the contents to the new file
        new_file.write(file_contents)
    


    messagebox.showinfo(title='Submitted', message='You have successfully submitted')
    return


def select_file(tk_window, selected_file):
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
        receipt_file = file_name
        formatted_file_name = os.path.basename(file_name)
        tk_window["text"] = formatted_file_name
    else:
        messagebox.showinfo(
            title="No selected file",
            message="Please select a file"
        )


if __name__ == "__main__":
    submit_window()