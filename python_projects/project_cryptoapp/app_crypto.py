# required modules and dependencies 

import requests
import json
from tkinter import *
import sqlite3
from tkinter import messagebox, Menu




root = Tk()
root.title('My Crypto Portfolio')
root.iconbitmap('favicon.ico')

connect_database = sqlite3.connect('coinDatabase')
connect_Object = connect_database.cursor()

# connect_Object.execute('CREATE TABLE IF NOT EXISTS coins(id INTEGER PRIMARY KEY AUTOINCREMENT, symbol TEXT, number of coins INTEGER, price INTEGER)')
# connect_database.commit()

    
# def update_data(symbol, id):
#     connect_Object.execute('UPDATE coins SET symbol WHERE id = (id)')

# def insert_data(id, symbol, number, price):
#     connect_Object.execute('INSERT INTO coins VALUES(?,?,?,?)',
#                             (id, symbol, number, price))
#     connect_database.commit()   



def reset():
    for cell in root.winfo_children():
        cell.destroy()
    app_header()
    appNavigation()
    myPortfolio()
    
    
def appNavigation():
    def clear_all():
        connect_Object.execute('DELETE FROM coins')
        connect_database.commit()
        messagebox.showinfo('Portfolio Notification', 'All Coins Cleared from Portfolio - Add New Coins')
        reset()
        
    def close_app():
        root.destroy()
        
    menu = Menu(root)
    file_item = Menu(menu)
    file_item.add_command(label='Clear Portfolio', command=clear_all)
    file_item.add_command(label='Exit App', command=close_app)
    menu.add_cascade(label='File', menu=file_item)
    root.config(menu=menu)

# 1. Function to call 
def myPortfolio():
    api = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&convert=USD&CMC_PRO_API_KEY=b6862996-981d-4686-a486-ad5a8e475b01')
    api_load = json.loads(api.content)
    

    # color schema
    # return green if amount is greater 0
    # and red if amount is less than 0

    def font_color(amount):
        if amount > 0:
            return 'green'
        else:
            return 'red'
    
    
    connect_Object.execute('SELECT * FROM coins')
    result = connect_Object.fetchall()
    
    def addCoin():
        connect_Object.execute('INSERT INTO coins(symbol, number, price) VALUES(?, ?, ?)', (enter_symbol.get(), enter_numberOfCoins.get(), enter_price.get()))
        connect_database.commit()
        messagebox.showinfo('Portfolio Notification', 'Coin Added to Portfolio Successfully!')
        reset()
        
        
    def updateCoin():
        connect_Object.execute('UPDATE coins SET symbol=?, number=?, price=? WHERE id =?', (update_symbol.get(), update_numberOfCoins.get(), update_price.get(), portId.get()))
        connect_database.commit()
        messagebox.showinfo('Portfolio Notification', 'Coin Updated Successfully!')
        reset()
    
    def deleteCoin():
        connect_Object.execute('DELETE FROM coins WHERE id=?', (portId_Delete.get(),))
        connect_database.commit()
        messagebox.showinfo('Portfolio Notification', 'Coin Deleted from Portfolio Successfully!')
        reset()
        
    # List of coins purchased  
    # coins = [{'symbol':'BTC','number of coins': 15,'price': 140}, 
    #         {'symbol':'ETH','number of coins': 5,'price': 3.9}, 
    #         {'symbol':'USDT','number of coins': 3,'price': 1.2},
    #         {'symbol':'SOL','number of coins': 10,'price': 4.2},
    #         {'symbol':'BNB','number of coins': 5,'price': 6.3},
    #         {'symbol':'XRP','number of coins': 10,'price': 23},
    #         {'symbol':'USDC','number of coins': 5,'price': 3},
    #         {'symbol':'ADA','number of coins': 3,'price': 5.5},
    #         {'symbol':'AVAX','number of coins': 32,'price': 6.6},
    #         {'symbol':'DOGE','number of coins': 5,'price': 3.7},
    #         {'symbol':'DOT','number of coins': 12,'price': 4.3},
    #         {'symbol':'TRX','number of coins': 5,'price': 2.3},
    #         {'symbol':'LINK','number of coins': 4,'price': 14},
    #         {'symbol':'ICP','number of coins': 15,'price': 7.5},
    #         {'symbol':'ATOM','number of coins': 50,'price': 7},
    #         {'symbol':'BCH','number of coins': 3,'price': 2},
    #         {'symbol':'LTC','number of coins': 2,'price': 5},
    #         {'symbol':'DAI','number of coins': 9,'price': 2.2},
    #         {'symbol':'SHIB','number of coins': 5,'price': 3.6},
    #         {'symbol':'TON','number of coins': 3,'price': 8},
    #         {'symbol':'MATIC','number of coins': 5,'price': 4.5}
    #       ]
    
    totalPortfolioCostOfCoins = 0
    totalCurrentCostOfCoins = 0
    totalPortfolioPNL = 0
    rowNumber = 1
    
    for number in range(0, 100):
        for coin in result:
            if coin[1] == api_load['data'][number]['symbol']:
                
                # parameters settings
                transactionNo = number + 1
                coinSymbol = api_load['data'][number]['symbol']
                coinName = api_load['data'][number]['name']
                currentPricePerCoin = api_load['data'][number]['quote']['USD']['price']
                noOfCoinsPurchased = coin[2]
                purchasedPricePerCoin = coin[3]
                costOfCoinsPurchased =  noOfCoinsPurchased * purchasedPricePerCoin
                currentCostOfCoins = currentPricePerCoin * noOfCoinsPurchased
                pnlPerCoin = currentPricePerCoin - purchasedPricePerCoin
                totalpnl = currentCostOfCoins - costOfCoinsPurchased
                totalPortfolioCostOfCoins += costOfCoinsPurchased
                totalCurrentCostOfCoins += currentCostOfCoins
                totalPortfolioPNL += totalpnl
                
            
                # FILLING IN THE LABELS
                
                portfolioNoLabel = Label(root, text = '00{}'.format(coin[0]), borderwidth=1, relief=SUNKEN)
                portfolioNoLabel.grid(row=rowNumber, column=0, sticky=NSEW)
                
                coinNameIdLabel = Label(root, text = coinName + ' ({})'.format(coinSymbol), borderwidth=1, relief=SUNKEN)
                coinNameIdLabel.grid(row=rowNumber, column=1, sticky=NSEW)
                
                noOfCoinsPurchasedLable = Label(root, text = noOfCoinsPurchased, borderwidth=1, relief=SUNKEN)
                noOfCoinsPurchasedLable.grid(row=rowNumber, column=2, sticky=NSEW)
                
                purchasedPricePerCoinLabel = Label(root, text = '${:,.2f}'.format(purchasedPricePerCoin), borderwidth=1, relief=SUNKEN)
                purchasedPricePerCoinLabel.grid(row=rowNumber, column=3, sticky=NSEW)
                
                costOfCoinsPurchasedLabel = Label(root, text = '${:,.2f}'.format(costOfCoinsPurchased), borderwidth=1, relief=SUNKEN)
                costOfCoinsPurchasedLabel.grid(row=rowNumber, column=4, sticky=NSEW)
                
                currentPricePerCoinLabel = Label(root, text = '${:,.2f}'.format(currentPricePerCoin), borderwidth=1, relief=SUNKEN)
                currentPricePerCoinLabel.grid(row=rowNumber, column=5, sticky=NSEW)
                
                currentCostOfCoinsLabel = Label(root, text = '${:,.2f}'.format(currentCostOfCoins), borderwidth=1, relief=SUNKEN)
                currentCostOfCoinsLabel.grid(row=rowNumber, column=6, sticky=NSEW)
                
                pnlPerCoinLabel = Label(root, text = '${:,.2f}'.format(pnlPerCoin), borderwidth=1, relief=SUNKEN, fg=font_color(pnlPerCoin))
                pnlPerCoinLabel.grid(row=rowNumber, column=7, sticky=NSEW)
                
                totalPnlPerCoinLabel = Label(root, text = '${:,.2f}'.format(totalpnl), borderwidth=1, relief=SUNKEN, fg=font_color(totalpnl))
                totalPnlPerCoinLabel.grid(row=rowNumber, column=8, sticky=NSEW)
                
                rowNumber += 1
    
    totalPortfolioCostOfCoinsLabel = Label(root, text = '${:,.2f}'.format(totalPortfolioCostOfCoins), borderwidth=1, relief=SUNKEN) 
    totalPortfolioCostOfCoinsLabel.grid(row=rowNumber, column=4, sticky=NSEW)
     
    totalCurrentCostOfCoinsLabel = Label(root, text = '${:,.2f}'.format(totalCurrentCostOfCoins), borderwidth=1, relief=SUNKEN) 
    totalCurrentCostOfCoinsLabel.grid(row=rowNumber, column=6, sticky=NSEW) 
    
    totalPortfolioPNLLabel = Label(root, text = '${:,.2f}'.format(totalPortfolioPNL), borderwidth=1, relief=SUNKEN, fg=font_color(totalPortfolioPNL)) 
    totalPortfolioPNLLabel.grid(row=rowNumber, column=8, sticky=NSEW)  
    
          
    # INSERT DATA
    enter_symbol = Entry(root, width=5, borderwidth=1, relief=SUNKEN)
    enter_symbol.grid(row=rowNumber + 1, column=1)
    
    enter_numberOfCoins = Entry(root, width=5, borderwidth=1, relief=SUNKEN)
    enter_numberOfCoins.grid(row=rowNumber + 1, column=2)
    
    enter_price = Entry(root, width=5, borderwidth=1, relief=SUNKEN)
    enter_price.grid(row=rowNumber + 1, column=3)
    
    addCoinButton = Button(root, text = 'ADD COIN', command=addCoin, borderwidth=3, relief=GROOVE)
    addCoinButton.grid(row=rowNumber + 1 , column=4, sticky=NSEW) 
    
    
    #UPDATE
    portId = Entry(root, width=5, borderwidth=1, relief=SUNKEN)
    portId.grid(row=rowNumber + 2, column=0)
    
    update_symbol = Entry(root, width=5, borderwidth=1, relief=SUNKEN)
    update_symbol.grid(row=rowNumber + 2, column=1)
    
    update_numberOfCoins = Entry(root, width=5, borderwidth=1, relief=SUNKEN)
    update_numberOfCoins.grid(row=rowNumber + 2, column=2)
    
    update_price = Entry(root, width=5, borderwidth=1, relief=SUNKEN)
    update_price.grid(row=rowNumber + 2, column=3)
    
    updateButton = Button(root, text = 'UPDATE COIN', command=updateCoin, borderwidth=3, relief=GROOVE)
    updateButton.grid(row=rowNumber + 2 , column=4, sticky=NSEW) 
     
    
    # DELETE
    portId_Delete = Entry(root, width=5, borderwidth=1, relief=SUNKEN)
    portId_Delete.grid(row=rowNumber + 4, column=0)
    
    deleteButton = Button(root, text = 'DELETE COIN', command=deleteCoin, borderwidth=3, relief=GROOVE)
    deleteButton.grid(row=rowNumber + 4, column=4, sticky=NSEW) 
        
    api = '' # (THE SIMPLE LOGIC- empty the table before updating with new data)
        
    refreshButton = Button(root, text = 'REFRESH', command=reset, borderwidth=3, relief=GROOVE)
    refreshButton.grid(row=rowNumber + 1 , column=8, sticky=NSEW)     
            

# print(api_load['data'][0])
# print(api_load['data'][0]['name'] + '-' + api_load['data'][0]['symbol'])
# print('${:,.2f}'.format(api_load['data'][0]['quote']['USD']['price']))

#heading
def app_header():
    portfolio_id = Label(root, text='Coin \nID Number', borderwidth=1, relief=SUNKEN)
    portfolio_id.grid(row=0, column=0, sticky=NSEW)

    coinName = Label(root, text='Coin Name-ID', borderwidth=1, relief=SUNKEN)
    coinName.grid(row=0, column=1, sticky=NSEW)

    coinName = Label(root, text='No. of Coins \nPurchased', borderwidth=1, relief=SUNKEN)
    coinName.grid(row=0, column=2, sticky=NSEW)

    purchasePrice = Label(root, text='Purchased Price \nPer Coin', borderwidth=1, relief=SUNKEN)
    purchasePrice.grid(row=0, column=3, sticky=NSEW)

    costOfCoins = Label(root, text='Cost of Coins \nPurchased', borderwidth=1, relief=SUNKEN)
    costOfCoins.grid(row=0, column=4, sticky=NSEW)

    currentPricePerCoin = Label(root, text='Current Price \nPer Coin', borderwidth=1, relief=SUNKEN)
    currentPricePerCoin.grid(row=0, column=5, sticky=NSEW)

    currentCostOfCoins = Label(root, text='Current Cost \nof Coins', borderwidth=1, relief=SUNKEN)
    currentCostOfCoins.grid(row=0, column=6, sticky=NSEW)

    pnlPerCoin = Label(root, text='P\L \nPer Coin', borderwidth=1, relief=SUNKEN)
    pnlPerCoin.grid(row=0, column=7, sticky=NSEW)

    totalpnl = Label(root, text='Total P\L', borderwidth=1, relief=SUNKEN)
    totalpnl.grid(row=0, column=8, sticky=NSEW)



app_header()
appNavigation()
myPortfolio()
root.mainloop()

connect_Object.close()
connect_database.close()


# Creating the EXECUTABLE FILE (Convert .py FILE to exe FILE)
# first instal the library call PYINSTALLER (Inside the terminal type the command - pip install pyinstaller)
# There are 2 methods to create the EXECUTABLE FILE
# 1. Direct Method (pyinstaller file_name.py)
# 2. Complex Method (pyinstaller file_name.py --onefile --noconsole --icon=favicon.ico)