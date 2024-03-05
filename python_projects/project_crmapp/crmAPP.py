from tkinter import *
import mysql.connector as mysql



root = Tk()
root.title('CRM App')
root.iconbitmap()
root.geometry('350x500')

conn = mysql.connect(host = 'localhost', 
                           user = 'root', 
                           password = 'Wynethopp0402@',
                           auth_plugin='mysql_native_password',
                           database = 'project')

# print(conn)

# create a cursor and initialise it for our connection to the database
my_cursor = conn.cursor()


# my_cursor.execute('create database project')

# my_cursor.execute('show databases')
# for database in my_cursor:
#     print(database[0])

# my_cursor.execute('create table if not exists customers (customerId INT PRIMARY KEY, firstName VARCHAR(255), birthDate VARCHAR(255), emailAddress VARCHAR(255), digitalAddress VARCHAR(255), contactNumber INT(225))')
# # my_cursor.execute('select * from customers')

# my_cursor.execute('alter table customers ADD (lastName VARCHAR(255))')

# # for data in my_cursor.description:
# #     print(data)

# def reset():
#     for cell in root.winfo_children():
#         cell.destroy()
#     app_header()
#     appNavigation()
#     myPortfolio()

def clear_fields():
    customerId_entry.delete(0, END)
    firstName_entry.delete(0, END)
    lastName_entry.delete(0, END)
    birthDate_entry.delete(0, END)
    emailAddress_entry.delete(0, END)
    digitalAddress_entry.delete(0, END)
    contactNumber_entry.delete(0, END)
    discountCode_entry.delete(0, END)
    paymentMethod_entry.delete(0, END)
    
def addCustomers():
    sql_command = '''INSERT INTO customers
    (customerId, firstName, lastName, birthDate, emailAddress, digitalAddress, contactNumber, paymentMethod, discountCode)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    value = (customerId_entry.get(), firstName_entry.get(), lastName_entry.get(), birthDate_entry.get(), emailAddress_entry.get(), digitalAddress_entry.get(), contactNumber_entry.get(), discountCode_entry.get(), paymentMethod_entry.get())
    my_cursor.execute(sql_command, value)
    clear_fields()
    conn.commit()
    
  
  
    
    
def listCustomers():
    listCustomers_query = Tk()
    listCustomers_query.title('Customer List')
    listCustomers_query.geometry('1000x1000')
    my_cursor.execute('select * from customers')
    result = my_cursor.fetchall()
    row = 0
    for x in result:
        id = x[0]
        fname = x[1]
        lname = x[2]
        bdate = x[3]
        email = x[4]
        address = x[5]
        contact = x[6]
        pm = x[7]
        dc = x[8]
        
        newWindowLabel = Label(listCustomers_query, text=id, borderwidth=1, relief=GROOVE)
        newWindowLabel.grid(row=row+1, column=0, sticky=NSEW)
        
        newWindowLabel = Label(listCustomers_query, text=fname, borderwidth=1, relief=GROOVE)
        newWindowLabel.grid(row=row+1, column=1, sticky=NSEW)
        
        newWindowLabel = Label(listCustomers_query, text=lname, borderwidth=1, relief=GROOVE)
        newWindowLabel.grid(row=row+1, column=2, sticky=NSEW)
        
        newWindowLabel = Label(listCustomers_query, text=bdate, borderwidth=1, relief=GROOVE)
        newWindowLabel.grid(row=row+1, column=3, sticky=NSEW)
        
        newWindowLabel = Label(listCustomers_query, text=email, borderwidth=1, relief=GROOVE)
        newWindowLabel.grid(row=row+1, column=4, sticky=NSEW)
        
        newWindowLabel = Label(listCustomers_query, text=address, borderwidth=1, relief=GROOVE)
        newWindowLabel.grid(row=row+1, column=5, sticky=NSEW)
        
        newWindowLabel = Label(listCustomers_query, text=contact, borderwidth=1, relief=GROOVE)
        newWindowLabel.grid(row=row+1, column=6, sticky=NSEW)
        
        newWindowLabel = Label(listCustomers_query, text=pm, borderwidth=1, relief=GROOVE)
        newWindowLabel.grid(row=row+1, column=7, sticky=NSEW)
        
        newWindowLabel = Label(listCustomers_query, text=dc, borderwidth=1, relief=GROOVE)
        newWindowLabel.grid(row=row+1, column=8, sticky=NSEW)
        
        row += 1
        
        
   
# New Window Headers
    customerId = Label(listCustomers_query, text='Customer \nID', borderwidth=1, relief=GROOVE)
    customerId.grid(row=0, column=0, sticky=NSEW)
    
    customerId = Label(listCustomers_query, text='Fist \nName', borderwidth=1, relief=GROOVE)
    customerId.grid(row=0, column=1, sticky=NSEW)
    
    customerId = Label(listCustomers_query, text='Last \nName', borderwidth=1, relief=GROOVE)
    customerId.grid(row=0, column=2, sticky=NSEW)
    
    customerId = Label(listCustomers_query, text='Date \nof Birth', borderwidth=1, relief=GROOVE)
    customerId.grid(row=0, column=3, sticky=NSEW)
    
    customerId = Label(listCustomers_query, text='Email \nAddress', borderwidth=1, relief=GROOVE)
    customerId.grid(row=0, column=4, sticky=NSEW)
    
    customerId = Label(listCustomers_query, text='Digital \nAddress', borderwidth=1, relief=GROOVE)
    customerId.grid(row=0, column=5, sticky=NSEW)
    
    customerId = Label(listCustomers_query, text='Contact \nNumber', borderwidth=1, relief=GROOVE)
    customerId.grid(row=0, column=6, sticky=NSEW)
    
    customerId = Label(listCustomers_query, text='Discount \nCode', borderwidth=1, relief=GROOVE)
    customerId.grid(row=0, column=7, sticky=NSEW)
    
    customerId = Label(listCustomers_query, text='Payment \nMethod', borderwidth=1, relief=GROOVE)
    customerId.grid(row=0, column=8, sticky=NSEW)
    


# def delete_fields():
#     firstName_entry.delete(0, END)
#     lastName_entry.delete(0, END)
#     birthDate_entry.delete(0, END)
#     emailAddress_entry.delete(0, END)
#     digitalAddress_entry.delete(0, END)
#     contactNumber_entry.delete(0, END)
#     discountCode_entry.delete(0, END)
#     paymentMethod_entry.delete(0, END)
    
    
# Heading
titlelabel = Label(root, text='Customers Database')
titlelabel.grid(row=0, column=0, columnspan= 2, sticky=NSEW, pady=20)

customerId_label = Label(root, text='Custumer Id: ')
customerId_label.grid(row=1, column=0, sticky=E, padx=10)

customerId_entry = Entry(root, borderwidth=2, relief=SUNKEN)
customerId_entry.grid(row=1, column=1, sticky=W)

firstName_label = Label(root, text='First Name: ')
firstName_label.grid(row=2, column=0, sticky=E, padx=10)

firstName_entry = Entry(root, borderwidth=2, relief=SUNKEN)
firstName_entry.grid(row=2, column=1, sticky=W)

lastName_label = Label(root, text='Last Name: ')
lastName_label.grid(row=3, column=0, sticky=E, padx=10)

lastName_entry = Entry(root, borderwidth=2, relief=SUNKEN)
lastName_entry.grid(row=3, column=1, sticky=W)

birthDate_label = Label(root, text='Date of Birth: ')
birthDate_label.grid(row=4, column=0, sticky=E, padx=10)

birthDate_entry = Entry(root, borderwidth=2, relief=SUNKEN)
birthDate_entry.grid(row=4, column=1, sticky=W)

emailAddress_label = Label(root, text='Email Address: ')
emailAddress_label.grid(row=5, column=0, sticky=E, padx=10)

emailAddress_entry = Entry(root, borderwidth=2, relief=SUNKEN)
emailAddress_entry.grid(row=5, column=1, sticky=W)

digitalAddress_label = Label(root, text='Digital Address: ')
digitalAddress_label.grid(row=6, column=0, sticky=E, padx=10)

digitalAddress_entry = Entry(root, borderwidth=2, relief=SUNKEN)
digitalAddress_entry.grid(row=6, column=1, sticky=W)

contactNumber_label = Label(root, text='Mobile Number: ')
contactNumber_label.grid(row=7, column=0, sticky=E, padx=10)

contactNumber_entry = Entry(root, borderwidth=2, relief=SUNKEN)
contactNumber_entry.grid(row=7, column=1, sticky=W)

discountCode_label = Label(root, text='Discount Code: ')
discountCode_label.grid(row=8, column=0, sticky=E, padx=10)

discountCode_entry = Entry(root, borderwidth=2, relief=SUNKEN)
discountCode_entry.grid(row=8, column=1, sticky=W)

paymentMethod_label = Label(root, text='Payment Method: ')
paymentMethod_label.grid(row=9, column=0, sticky=E, padx=10)

paymentMethod_entry = Entry(root, borderwidth=2, relief=SUNKEN)
paymentMethod_entry.grid(row=9, column=1, sticky=W)



# Buttons

addEntry_Button = Button(root, text='Add Customer', command=addCustomers)
addEntry_Button.grid(row=10, column=0, padx=10, pady=10)


clearFields_Button = Button(root, text='Clear Fields', command=clear_fields)
clearFields_Button.grid(row=10, column=1)


listCustomers_buttons = Button(root, text='List Customers', command=listCustomers)
listCustomers_buttons.grid(row=11, column=0, sticky=E, padx=10)



root.mainloop()
conn.close()