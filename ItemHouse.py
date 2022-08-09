import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Yash",
    database="inventorymanagement"
)
mycursor = mydb.cursor()


def createItem(itemType, item):
    sqlformula = f"SELECT * FROM itempresent WHERE itemtype='{itemType}' AND item='{item}'"
    mycursor.execute(sqlformula)
    myresult = mycursor.fetchall()
    if myresult==[]:
        sqlformula = "INSERT INTO itempresent (itemType, item) VALUES (%s, %s)"
        Party = (itemType, item)

        mycursor.execute(sqlformula, Party)
        mydb.commit()
        messagebox.showinfo('Success', 'Item Added Successfully')
    else:
        messagebox.showerror('ERROR', 'Item Already Present')


def ItemList(ItemType):
    sqlformula = f"SELECT item FROM itempresent WHERE itemtype='{ItemType}'"
    mycursor.execute(sqlformula)
    myresult = mycursor.fetchall()
    l = ['Select']
    for r in myresult:
        l.append(r[0])

    return l

def ItemListAll():
    sqlformula = f"SELECT item FROM itempresent"
    mycursor.execute(sqlformula)
    myresult = mycursor.fetchall()
    l = ['All']
    for r in myresult:
        l.append(r[0])

    return l











