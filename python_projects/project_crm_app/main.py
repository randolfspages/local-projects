import customtkinter
#import CTkListbox
from tkinter import *
import mysql.connector as mysql



conn = mysql.connect(host = 'localhost', 
                           user = 'root', 
                           password = 'Wynethopp0402@',
                           auth_plugin='mysql_native_password',
                           database = 'project')

my_cursor = conn.cursor()

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.title('CRM App')
root.iconbitmap()
root.geometry('300x500')


root.grid_rowconfigure(0, weight=0)
root.grid_columnconfigure((0, 1), weight=0)
  
  
def refresh():
    for cell in root.winfo_children():
        cell.destroy()
        refresh_Button()
        crmAPP()
       

def crmAPP(): 
    def clear_fields():
        root.customerId_entry.delete(0, END)
        root.firstName_entry.delete(0, END)
        root.lastName_entry.delete(0, END)
        root.contactNumber_entry.delete(0, END)

        
    def addCustomers():
        sql_command = '''INSERT INTO customers
        (customerId, firstName, lastName, whatsAppNo)
        VALUES (%s, %s, %s, %s)'''
        value = (root.customerId_entry.get(), root.firstName_entry.get(), root.lastName_entry.get(), root.contactNumber_entry.get())
        my_cursor.execute(sql_command, value)
        clear_fields()
        conn.commit()
        

    def searchCustomer(firstName):
        sql_command  = 'select * from customers where firstName = %s' 
        value = (firstName,)
        my_cursor.execute(sql_command, value)
        result = my_cursor.fetchall()
        for data in result:
            displaySearchResult(data)
            root.firstNameSearch_entry.delete(0, END)
            searchCustomer.__delattr__
        
        
    def displaySearchResult(result):
        listbox = Listbox(root ,width=30, height=2)
        listbox.grid(row=7, columnspan=2, pady=10) 
        listbox.insert (END, result)
            
    
    def listCustomers():
        listCustomers_query = Tk()
        listCustomers_query.title('Customer List')
        listCustomers_query.geometry('350x5000')
        my_cursor.execute('select * from customers')
        result = my_cursor.fetchall()
        row = 0
        for x in result:
            id = x[0]
            fname = x[1]
            lname = x[2]
            whatsAppNumber = x[3]
            
            newWindowLabel = Label(listCustomers_query, text=id, borderwidth=1, relief=GROOVE)
            newWindowLabel.grid(row=row+1, column=0, sticky=NSEW)
            
            newWindowLabel = Label(listCustomers_query, text=fname, borderwidth=1, relief=GROOVE)
            newWindowLabel.grid(row=row+1, column=1, sticky=NSEW)
            
            newWindowLabel = Label(listCustomers_query, text=lname, borderwidth=1, relief=GROOVE)
            newWindowLabel.grid(row=row+1, column=2, sticky=NSEW)
            
            newWindowLabel = Label(listCustomers_query, text=whatsAppNumber, borderwidth=1, relief=GROOVE)
            newWindowLabel.grid(row=row+1, column=3, sticky=NSEW)
                
            row += 1        
    
        # New Window Headers
        customerId = Label(listCustomers_query, text='Customer \nID', borderwidth=1, relief=GROOVE)
        customerId.grid(row=0, column=0, sticky=NSEW)


        customerId = Label(listCustomers_query, text='Fist \nName', borderwidth=1, relief=GROOVE)
        customerId.grid(row=0, column=1, sticky=NSEW)


        customerId = Label(listCustomers_query, text='Last \nName', borderwidth=1, relief=GROOVE)
        customerId.grid(row=0, column=2, sticky=NSEW)


        customerId = Label(listCustomers_query, text='Whatsapp \nNumber', borderwidth=1, relief=GROOVE)
        customerId.grid(row=0, column=3, sticky=NSEW)


    
    # HEADING
    root.label = customtkinter.CTkLabel(master=root, text='Registration')
    root.label.grid(row=0, columnspan=2, sticky='NSEW', pady=10)


    # LABELS 
    root.customerId_label = customtkinter.CTkLabel(master=root, text='ID No.:')
    root.customerId_label.grid(row=1, column=0, padx=5, pady=5)

    root.firstName_label = customtkinter.CTkLabel(master=root, text='First Name:')
    root.firstName_label.grid(row=2, column=0, padx=5, pady=5)

    root.lastName_label = customtkinter.CTkLabel(master=root, text='Last Name:')
    root.lastName_label.grid(row=3, column=0, padx=5, pady=5)

    root.contactNumber_label = customtkinter.CTkLabel(master=root, text='Contact Number:')
    root.contactNumber_label.grid(row=4, column=0, padx=5, pady=5)


    # ENTRIES
    root.customerId_entry = customtkinter.CTkEntry(master=root, width=60)
    root.customerId_entry.grid(row=1, column=1, padx=5, pady=5)

    root.firstName_entry = customtkinter.CTkEntry(master=root)
    root.firstName_entry.grid(row=2, column=1, padx=5, pady=5)

    root.lastName_entry = customtkinter.CTkEntry(master=root)
    root.lastName_entry.grid(row=3, column=1, padx=5, pady=5)

    root.contactNumber_entry = customtkinter.CTkEntry(master=root)
    root.contactNumber_entry.grid(row=4, column=1, padx=5, pady=5)

    root.firstNameSearch_entry = customtkinter.CTkEntry(master=root, placeholder_text='Search customer')
    root.firstNameSearch_entry.grid(row=6, column=0, padx=5, pady=5)


    # BUTTONS
    root.addEntry_Button = customtkinter.CTkButton(master=root, text='Add Customer', command=addCustomers)
    root.addEntry_Button.grid(row=5, column=0, padx=5, pady=20)

    root.listCustomers_button = customtkinter.CTkButton(master=root, text='List Customers', command=listCustomers)
    root.listCustomers_button.grid(row=5, column=1, padx=5, pady=5)

    root.search_button = customtkinter.CTkButton(master=root, text='Search Customer', command=lambda:searchCustomer(root.firstNameSearch_entry.get()))
    root.search_button.grid(row=6, column=1, padx=5, pady=5)
    
    
def refresh_Button():
    root.refresh_button = customtkinter.CTkButton(master=root, text='Refresh', command=refresh)
    root.refresh_button.grid(row=8, columnspan=2, padx=5, pady=10)


# LISTBOX
# listbox = Listbox(master=root, command=displaySearchResult)
# listbox.grid(row=7, columspan=2, padx=5, pady=5)

refresh_Button()
crmAPP()
root.mainloop()
