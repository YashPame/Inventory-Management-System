import mysql.connector
import datetime
from datetime import date
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Yash",
    database="inventorymanagement"
)
mycursor = mydb.cursor()


def AddItemToInventory(itemType, item, quantity, unit):
    sqlformula = f"SELECT quantity FROM inventory WHERE itemtype='{itemType}' AND item='{item}' AND unit='{unit}'"
    mycursor.execute(sqlformula)
    myresult = mycursor.fetchall()

    if myresult == []:
        sqlformula = "INSERT INTO inventory (itemType, item, quantity,unit) VALUES (%s, %s, %s,%s)"
        ID = (itemType, item, quantity, unit)
        mycursor.execute(sqlformula, ID)
        mydb.commit()
    else:
        quantityf = float(quantity) + float(myresult[0][0])

        sql = f"UPDATE inventory SET quantity='{quantityf}' WHERE itemtype='{itemType}' AND item='{item}' AND unit='{unit}'"
        mycursor.execute(sql)
        mydb.commit()




def AddItemToInventoryDetailed(itemType, item, inparty, price, quantity, unit):
    sqlformula = f"SELECT price, quantity FROM inventorydetailed WHERE itemtype='{itemType}' AND item='{item}' AND inparty='{inparty}' AND unit='{unit}'"
    mycursor.execute(sqlformula)
    myresult = mycursor.fetchall()

    if myresult == []:
        sqlformula = "INSERT INTO inventorydetailed (itemType, item, inparty, price, quantity,unit,profit) VALUES (%s, %s, %s, %s,%s,%s,%s)"
        ID = (itemType, item, inparty, price, quantity, unit, '0')
        mycursor.execute(sqlformula, ID)
        mydb.commit()
    else:
        price = str(float((float(price) + float(myresult[0][0])) / 2))
        quantityf = float(quantity) + float(myresult[0][1])

        sql = f"UPDATE inventorydetailed SET price='{price}' , quantity='{quantityf}' WHERE itemtype='{itemType}' AND item='{item}' AND inparty='{inparty}' AND unit='{unit}'"
        mycursor.execute(sql)
        mydb.commit()

    with open('InventoryAdditionSummary.txt', 'a') as f:
        content = f"\n{str(date.today())} {str(datetime.datetime.now().strftime('%H:%M:%S'))}----Add----{itemType}, {item}, {inparty}, {price}, {quantity}, {unit} "
        f.write(content)

    AddItemToInventory(itemType, item, quantity, unit)
    messagebox.showinfo('Success', 'Item Added Successfully')


def RemoveItemFromInventory(itemType, item, quantity, unit):
    sqlformula = f"SELECT quantity FROM inventory WHERE itemtype='{itemType}' AND item='{item}' AND unit='{unit}'"
    mycursor.execute(sqlformula)
    myresult = mycursor.fetchall()

    if myresult == []:
        pass
    else:
        quantityf = str(float(myresult[0][0]) - float(quantity))

        if float(quantityf) >= 0:
            sql = f"UPDATE inventory SET quantity='{quantityf}' WHERE itemtype='{itemType}' AND item='{item}' AND unit='{unit}'"
            mycursor.execute(sql)
            mydb.commit()

        else:
            pass


def RemoveItemFromInventoryDetailed(itemType, item, inparty, price, quantity, unit, R):
    sqlformula = f"SELECT price, quantity,profit FROM inventorydetailed WHERE itemtype='{itemType}' AND item='{item}' AND inparty='{inparty}' AND unit='{unit}'"
    mycursor.execute(sqlformula)
    myresult = mycursor.fetchall()

    if myresult == []:
        messagebox.showerror('Error', 'No Item Present')
    else:
        profit = str(((float(price) - float(myresult[0][0])) * float(quantity)) + float(myresult[0][2]))
        quantityf = str(float(myresult[0][1]) - float(quantity))
        if float(quantityf) >= 0:
            sql = f"UPDATE inventorydetailed SET profit='{profit}' , quantity='{quantityf}' WHERE itemtype='{itemType}' AND item='{item}' AND inparty='{inparty}' AND unit='{unit}'"
            mycursor.execute(sql)
            mydb.commit()
            with open('InventoryAdditionSummary.txt', 'a') as f:
                content = f"\n{str(date.today())} {str(datetime.datetime.now().strftime('%H:%M:%S'))}----Remove----{itemType}, {item}, {inparty}, {price}, {quantity}, {unit},{R} "
                f.write(content)

            RemoveItemFromInventory(itemType, item, quantity, unit)
            messagebox.showinfo('Success','Item Removed Successfully')
        else:
            messagebox.showerror('Error', 'Quantity available is less')


def CheckingItems(ItemType, Item, InParty):
    if ItemType=='All' and Item!='All' and InParty!='All':
        sqlformula = f"SELECT * FROM inventorydetailed WHERE item='{Item}' AND inparty='{InParty}'"
        mycursor.execute(sqlformula)
        myresult = mycursor.fetchall()
        S = ''
        for i in myresult:
            IT = i[0]
            I = i[1]
            IP = i[2]
            P = i[3]
            Q = i[4]
            U = i[5]
            Pr = i[6]

            a = f"{IT}-{I}-{IP}\nCostPrice-{P}, Quantity-{Q} {U}, Profit-{Pr}\n\n"
            S = S + a
        return S

    elif ItemType=='All' and Item=='All' and InParty!='All':
        sqlformula = f"SELECT * FROM inventorydetailed WHERE inparty='{InParty}'"
        mycursor.execute(sqlformula)
        myresult = mycursor.fetchall()
        S = ''
        for i in myresult:
            IT = i[0]
            I = i[1]
            IP = i[2]
            P = i[3]
            Q = i[4]
            U = i[5]
            Pr = i[6]

            a = f"{IT}-{I}-{IP}\nCostPrice-{P}, Quantity-{Q} {U}, Profit-{Pr}\n\n"
            S = S + a
        return S

    elif ItemType=='All' and Item=='All' and InParty=='All':
        sqlformula = f"SELECT * FROM inventorydetailed"
        mycursor.execute(sqlformula)
        myresult = mycursor.fetchall()
        S = ''
        for i in myresult:
            IT = i[0]
            I = i[1]
            IP = i[2]
            P = i[3]
            Q = i[4]
            U = i[5]
            Pr = i[6]

            a = f"{IT}-{I}-{IP}\nCostPrice-{P}, Quantity-{Q} {U}, Profit-{Pr}\n\n"
            S = S + a
        return S

    if ItemType!='All' and Item=='All' and InParty=='All':
        sqlformula = f"SELECT * FROM inventorydetailed WHERE itemtype='{ItemType}'"
        mycursor.execute(sqlformula)
        myresult = mycursor.fetchall()
        S = ''
        for i in myresult:
            IT = i[0]
            I = i[1]
            IP = i[2]
            P = i[3]
            Q = i[4]
            U = i[5]
            Pr = i[6]

            a = f"{IT}-{I}-{IP}\nCostPrice-{P}, Quantity-{Q} {U}, Profit-{Pr}\n\n"
            S = S + a
        return S

    elif ItemType!='All' and Item!='All' and InParty=='All':
        sqlformula = f"SELECT * FROM inventorydetailed WHERE itemtype='{ItemType}' AND item='{Item}'"
        mycursor.execute(sqlformula)
        myresult = mycursor.fetchall()
        S = ''
        for i in myresult:
            IT = i[0]
            I = i[1]
            IP = i[2]
            P = i[3]
            Q = i[4]
            U = i[5]
            Pr = i[6]

            a = f"{IT}-{I}-{IP}\nCostPrice-{P}, Quantity-{Q} {U}, Profit-{Pr}\n\n"
            S = S + a
        return S

    elif ItemType != 'All' and Item != 'All' and InParty != 'All':
        sqlformula = f"SELECT * FROM inventorydetailed WHERE itemtype='{ItemType}' AND item='{Item}' AND inparty='{InParty}'"
        mycursor.execute(sqlformula)
        myresult = mycursor.fetchall()
        S = ''
        for i in myresult:
            IT = i[0]
            I = i[1]
            IP = i[2]
            P = i[3]
            Q = i[4]
            U = i[5]
            Pr = i[6]

            a=f"{IT}-{I}-{IP}\nCostPrice-{P}, Quantity-{Q} {U}, Profit-{Pr}\n\n"
            S=S+a

        return S

    else:
        S=''
        return S


def AllItem(item):
    sqlformula = f"SELECT * FROM inventory WHERE item='{item}'"
    mycursor.execute(sqlformula)
    myresult = mycursor.fetchall()
    S = ''
    for i in myresult:
        IT = i[0]
        I = i[1]
        Q = i[2]
        U = i[3]

        a = f"{IT}-{I}\n Quantity-{Q} {U}\n\n"
        S = S + a

    return S

