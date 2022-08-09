import mysql.connector
from  tkinter import messagebox

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Yash",
    database="inventorymanagement"
)
mycursor = mydb.cursor()


def createInParty(itemType, item, name, accno, ifsccode,mobile,email):
    sqlformula = f"SELECT name FROM inparty WHERE itemtype='{itemType}' AND item='{item}' AND name='{name}' AND accno='{accno}'"
    mycursor.execute(sqlformula)
    myresult = mycursor.fetchall()

    if myresult==[]:
        sqlformula = "INSERT INTO inparty (itemType, item, name, accno, ifsccode,mobile,email) VALUES (%s, %s, %s, %s,%s,%s,%s)"
        Party = (itemType, item, name, accno, ifsccode,mobile,email)

        mycursor.execute(sqlformula, Party)
        mydb.commit()
        messagebox.showinfo('Success', 'InParty Added Successfully')
    else:
        messagebox.showerror('ERROR','InParty Already Present')

def InPartyList(ItemType,Item):
    sqlformula=f"SELECT name FROM inparty WHERE itemtype='{ItemType}' AND item='{Item}'"
    mycursor.execute(sqlformula)
    myresult = mycursor.fetchall()
    l=['Select']
    for r in myresult:
        l.append(r[0])

    return l

def InPartyListALL():
    sqlformula=f"SELECT name FROM inparty"
    mycursor.execute(sqlformula)
    myresult = mycursor.fetchall()
    l=['All']
    for r in myresult:
        l.append(r[0])
    return l


