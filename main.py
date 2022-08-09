from tkinter import *
from tkinter import ttk
import InPartyCreationSelection
from tkinter import messagebox
import InventoryHouse
import ItemHouse
import itemTypeLists


class InventoryManagement:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1536x864+0+0')
        self.root.config(bd=7, relief=SOLID)
        self.root.title('Inventory Management')
        title = Label(self.root, text='Inventory Management', bd=5, relief=GROOVE,
                      font=('times new roman', 30, 'bold'), pady=2).pack(fill=X)

        self.f2 = Frame()
        self.f3 = Frame()
        self.f4 = Frame()

        self.BTN1Variable = StringVar()
        self.BTN1Variable.set('')
        self.BTN2Variable = StringVar()
        self.BTN2Variable.set('')
        self.BTN3Variable = StringVar()
        self.BTN3Variable.set('')
        self.BTN4Variable = StringVar()
        self.BTN4Variable.set('')
        self.BTN5Variable = StringVar()
        self.BTN5Variable.set('')
        self.BTN6Variable = StringVar()
        self.BTN6Variable.set('')
        self.BTN7Variable = StringVar()
        self.BTN7Variable.set('')
        self.BTN8Variable = StringVar()
        self.BTN8Variable.set('')

        self.LABEL1Variable = StringVar()
        self.LABEL1Variable.set('')
        self.LABEL2Variable = StringVar()
        self.LABEL2Variable.set('')
        self.LABEL3Variable = StringVar()
        self.LABEL3Variable.set('')
        self.LABEL4Variable = StringVar()
        self.LABEL4Variable.set('')
        self.LABEL5Variable = StringVar()
        self.LABEL5Variable.set('')
        self.LABEL6Variable = StringVar()
        self.LABEL6Variable.set('')
        self.LABEL7Variable = StringVar()
        self.LABEL7Variable.set('')
        self.LABEL8Variable = StringVar()
        self.LABEL8Variable.set('')
        self.LABEL9Variable = StringVar()
        self.LABEL9Variable.set('')

        self.LABEL2ENTRY2Variable = StringVar()
        self.LABEL3ENTRY3Variable = StringVar()
        self.LABEL4ENTRY4Variable = StringVar()
        self.LABEL5ENTRY5Variable = StringVar()
        self.LABEL6ENTRY6Variable = StringVar()
        self.LABEL7ENTRY7Variable = StringVar()
        self.LABEL8ENTRY8Variable = StringVar()
        self.LABEL9ENTRY9Variable = StringVar()

        self.UserNameTXTVariable = StringVar()
        self.UserNameTXTVariable.set('')
        self.UserPhoneNoTXTVariable = StringVar()
        self.UserPhoneNoTXTVariable.set('')

        self.ItemType = ''
        self.Item = ''
        self.InParty = ''
        self.price = ''
        self.quantity = ''
        self.unit = ''
        self.reason = ''

        self.LeftMainFrame_f1()

    def LeftMainFrame_f1(self):
        self.f1 = Frame(self.root, bd=5, relief=GROOVE)
        self.f1.place(x=10, y=65, width=300, height=720)

        self.LoginBTN = Button(self.f1, text='LogIn', font=('Agency FB', 20, 'bold'), bd=5,
                               relief=RAISED, command=self.LogInFRAME)
        self.LoginBTN.place(x=20, y=20, width=250, height=50)

        self.____ = Button(self.f1, text='---------', font=('Agency FB', 20, 'bold'), bd=5,
                           relief=RAISED)
        self.____.place(x=20, y=90, width=250, height=50)

        self.____ = Button(self.f1, text='---------', font=('Agency FB', 20, 'bold'), bd=5,
                           relief=RAISED)
        self.____.place(x=20, y=160, width=250, height=50)

    def LogInFRAME(self):
        self.LoginBTN.config(bg='yellow')
        self.f4.destroy()
        self.f3.destroy()
        self.f2.destroy()

        self.f3 = Frame(self.root, bd=5, relief=GROOVE)
        self.f3.place(x=321, y=100, width=880, height=320)

        self.LABEL1Variable.set('Logging In...')
        self.LABEL2Variable.set('Enter User ID')
        self.LABEL3Variable.set('Enter Password')

        self.LABEL1 = Label(self.f3, text=self.LABEL1Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL1.place(x=20, y=20, width=700, height=50)

        self.LABEL2 = Label(self.f3, text=self.LABEL2Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL2.place(x=20, y=90, width=400, height=50)

        self.LABEL3 = Label(self.f3, text=self.LABEL3Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL3.place(x=20, y=160, width=400, height=50)

        self.LABEL2ENTRY2 = Entry(self.f3, text=self.LABEL2ENTRY2Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL2ENTRY2.place(x=460, y=90, width=390, height=50)

        self.LABEL3ENTRY3 = Entry(self.f3, text=self.LABEL3ENTRY3Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL3ENTRY3.place(x=460, y=160, width=390, height=50)

        self.SubmitBTN = Button(self.f3, text='Log In', font=('Agency FB', 25, 'bold'), bd=5, relief=RIDGE,
                                command=self.LogInDetailsCheck)
        self.SubmitBTN.place(x=460, y=230, width=390, height=60)

    def LogInDetailsCheck(self):
        # Check for login Details
        self.f3.destroy()

        self.RightMainFrame_LogIN_f4_f2()

    def Clearing(self):
        self.LABEL1Variable.set('')
        self.LABEL2Variable.set('')
        self.LABEL3Variable.set('')
        self.LABEL4Variable.set('')
        self.LABEL5Variable.set('')
        self.LABEL6Variable.set('')
        self.LABEL7Variable.set('')
        self.LABEL8Variable.set('')
        self.LABEL9Variable.set('')

        self.LABEL2ENTRY2Variable.set('')
        self.LABEL3ENTRY3Variable.set('')
        self.LABEL4ENTRY4Variable.set('')
        self.LABEL5ENTRY5Variable.set('')
        self.LABEL6ENTRY6Variable.set('')
        self.LABEL7ENTRY7Variable.set('')
        self.LABEL8ENTRY8Variable.set('')
        self.LABEL9ENTRY9Variable.set('')

    def RightMainFrame_LogIN_f4_f2(self):
        self.UserNameTXTVariable.set('Name')
        self.UserPhoneNoTXTVariable.set('Phone')

        self.f4 = Frame(self.root, bd=5, relief=GROOVE)
        self.f4.place(x=321, y=80, width=880, height=140)

        self.UserNameLBL = Label(self.f4, text='  Name', font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE,
                                 anchor='w')
        self.UserNameLBL.place(x=10, y=10, width=200, height=50)
        self.UserNameTXT = Label(self.f4, text=self.UserNameTXTVariable.get(), font=('Agency FB', 20, 'bold'), bd=5,
                                 relief=RIDGE, anchor='w')
        self.UserNameTXT.place(x=220, y=10, width=200, height=50)

        self.UserPhoneNoLBL = Label(self.f4, text='  Phone Number', font=('Agency FB', 20, 'bold'), bd=5,
                                    relief=RIDGE, anchor='w')
        self.UserPhoneNoLBL.place(x=10, y=70, width=200, height=50)
        self.UserPhoneNoTXT = Label(self.f4, text=self.UserPhoneNoTXTVariable.get(), font=('Agency FB', 20, 'bold'),
                                    bd=5, relief=RIDGE, anchor='w')
        self.UserPhoneNoTXT.place(x=220, y=70, width=200, height=50)

        self.f2 = Frame(self.root, bd=5, relief=GROOVE)
        self.f2.place(x=1212, y=65, width=300, height=720)
        self.BTN1Variable.set('Add Items')
        self.BTN2Variable.set('Remove Items')
        self.BTN3Variable.set('Check Items')
        self.BTN4Variable.set('Create In-Party')
        self.BTN5Variable.set('Create Item')
        self.BTN6Variable.set('-------')
        self.BTN7Variable.set('Clear Frames')
        self.BTN8Variable.set('Log Out')

        self.BTN1 = Button(self.f2, text=self.BTN1Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                           command=self.AddItemFrame)
        self.BTN1.place(x=20, y=20, width=250, height=50)

        self.BTN2 = Button(self.f2, text=self.BTN2Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                           command=self.RemoveItemFrame)
        self.BTN2.place(x=20, y=90, width=250, height=50)

        self.BTN3 = Button(self.f2, text=self.BTN3Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                           command=self.CheckItemsFrame)
        self.BTN3.place(x=20, y=160, width=250, height=50)

        self.BTN4 = Button(self.f2, text=self.BTN4Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                           command=self.CreateInPartyFrame)
        self.BTN4.place(x=20, y=230, width=250, height=50)

        self.BTN5 = Button(self.f2, text=self.BTN5Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                           command=self.CreateItem)
        self.BTN5.place(x=20, y=300, width=250, height=50)

        self.BTN6 = Button(self.f2, text=self.BTN6Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED)
        self.BTN6.place(x=20, y=370, width=250, height=50)

        self.BTN7 = Button(self.f2, text=self.BTN7Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                           command=self.ClearFrames)
        self.BTN7.place(x=20, y=440, width=250, height=50)

        self.BTN8 = Button(self.f2, text=self.BTN8Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                           command=self.LogOut)
        self.BTN8.place(x=20, y=510, width=250, height=50)

    def AddItemFrame(self):
        self.BTN1.config(bg='yellow')
        self.BTN2.config(bg='SystemButtonFace')
        self.BTN3.config(bg='SystemButtonFace')
        self.BTN4.config(bg='SystemButtonFace')
        self.BTN5.config(bg='SystemButtonFace')
        self.BTN6.config(bg='SystemButtonFace')
        self.BTN7.config(bg='SystemButtonFace')
        self.BTN8.config(bg='SystemButtonFace')
        self.Clearing()
        self.f3.destroy()
        self.f3 = Frame(self.root, bd=5, relief=GROOVE)
        self.f3.place(x=321, y=240, width=880, height=550)

        self.LABEL1Variable.set('Adding Item')
        self.LABEL2Variable.set('Select Item Type')
        self.LABEL3Variable.set('Select Item')
        self.LABEL4Variable.set('Select In-Party')
        self.LABEL5Variable.set('Price')
        self.LABEL6Variable.set('Quantity & Unit')

        self.LABEL1 = Label(self.f3, text=self.LABEL1Variable.get(), font=('Agency FB', 20, 'bold'), bd=3, relief=RIDGE)
        self.LABEL1.place(x=10, y=10, width=400, height=40)

        self.LABEL2 = Label(self.f3, text=self.LABEL2Variable.get(), font=('Agency FB', 15, 'bold'), bd=3, relief=RIDGE)
        self.LABEL2.place(x=10, y=60, width=150, height=30)

        def CheckItemType():
            def CheckItem():
                def CheckInParty():
                    self.InParty = InPartycmb.get()
                    if self.InParty == 'Select':
                        messagebox.showerror('ERROR', 'Select InParty')
                    else:
                        Details()

                self.Item = Itemcmb.get()
                if self.Item == 'Select':
                    messagebox.showerror('ERROR', 'Select item')
                else:
                    self.LABEL4 = Label(self.f3, text=self.LABEL4Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                        relief=RIDGE)
                    self.LABEL4.place(x=10, y=140, width=150, height=30)
                    InParty = InPartyCreationSelection.InPartyList(self.ItemType, self.Item)
                    InParty[0] = 'Select'
                    InPartycmb = ttk.Combobox(self.f3, value=InParty)
                    InPartycmb.place(x=170, y=140, width=150, height=30)
                    InPartycmb.current(0)
                    Checkbtn = Button(self.f3, text="✔", font="lucida 10 bold", relief=RAISED, border=3,
                                      command=CheckInParty)
                    Checkbtn.place(x=335, y=140, height=30)

            # Check Selected Item Type and return items in particular item type
            self.ItemType = ItemTypecmb.get()
            if self.ItemType == 'Select':
                messagebox.showerror('ERROR', 'Select item type')
            else:
                self.LABEL3 = Label(self.f3, text=self.LABEL3Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                    relief=RIDGE)
                self.LABEL3.place(x=10, y=100, width=150, height=30)

                Item = ItemHouse.ItemList(self.ItemType)
                Item[0] = 'Select'
                Itemcmb = ttk.Combobox(self.f3, value=Item)
                Itemcmb.place(x=170, y=100, width=150, height=30)
                Itemcmb.current(0)
                Checkbtn = Button(self.f3, text="✔", font="lucida 10 bold", relief=RAISED, border=3, command=CheckItem)
                Checkbtn.place(x=335, y=100, height=30)

        ItemType = itemTypeLists.itemType
        ItemType[0] = 'Select'
        ItemTypecmb = ttk.Combobox(self.f3, value=ItemType)
        ItemTypecmb.place(x=170, y=60, width=150, height=30)
        ItemTypecmb.current(0)
        Checkbtn = Button(self.f3, text="✔", font="lucida 10 bold", relief=RAISED, border=3, command=CheckItemType)
        Checkbtn.place(x=335, y=60, height=30)

        def Details():
            def Detail():
                self.price = self.LABEL5ENTRY5Variable.get()
                self.quantity = self.LABEL6ENTRY6Variable.get()
                self.unit = Unitcmb.get()
                if self.price == '':
                    messagebox.showerror('ERROR', 'Enter Price')
                elif self.quantity == '':
                    messagebox.showerror('ERROR', 'Enter Quantity')
                elif self.unit == 'Select':
                    messagebox.showerror('ERROR', 'Select Unit')
                else:
                    self.AddItemFinal()

            self.LABEL5 = Label(self.f3, text=self.LABEL5Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                relief=RIDGE)
            self.LABEL5.place(x=10, y=190, width=150, height=30)

            self.LABEL5ENTRY5 = Entry(self.f3, text=self.LABEL5ENTRY5Variable, font=('Agency FB', 15, 'bold'), bd=3,
                                      relief=RIDGE)
            self.LABEL5ENTRY5.place(x=170, y=190, width=100, height=30)

            self.LABEL6 = Label(self.f3, text=self.LABEL6Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                relief=RIDGE)
            self.LABEL6.place(x=10, y=220, width=150, height=30)
            self.LABEL6ENTRY6 = Entry(self.f3, text=self.LABEL6ENTRY6Variable, font=('Agency FB', 15, 'bold'), bd=3,
                                      relief=RIDGE)
            self.LABEL6ENTRY6.place(x=170, y=220, width=100, height=30)

            Unit = itemTypeLists.UnitType
            Unitcmb = ttk.Combobox(self.f3, value=Unit)
            Unitcmb.place(x=280, y=220, width=70, height=30)
            Unitcmb.current(0)

            self.SubmitBTN = Button(self.f3, text='Add Item', font=('Agency FB', 18, 'bold'), bd=3, relief=RIDGE,
                                    command=Detail)
            self.SubmitBTN.place(x=460, y=270, width=390, height=40)

    def AddItemFinal(self):
        IT = self.ItemType
        I = self.Item
        IP = self.InParty
        P = self.price
        Q = self.quantity
        U = self.unit

        InventoryHouse.AddItemToInventoryDetailed(IT, I, IP, P, Q, U)

        self.f3.destroy()

        self.Clearing()
        self.BTN1.config(bg='SystemButtonFace')
        self.BTN2.config(bg='SystemButtonFace')
        self.BTN3.config(bg='SystemButtonFace')
        self.BTN4.config(bg='SystemButtonFace')
        self.BTN5.config(bg='SystemButtonFace')
        self.BTN6.config(bg='SystemButtonFace')
        self.BTN7.config(bg='SystemButtonFace')
        self.BTN8.config(bg='SystemButtonFace')

    def RemoveItemFrame(self):
        self.BTN1.config(bg='SystemButtonFace')
        self.BTN2.config(bg='yellow')
        self.BTN3.config(bg='SystemButtonFace')
        self.BTN4.config(bg='SystemButtonFace')
        self.BTN5.config(bg='SystemButtonFace')
        self.BTN6.config(bg='SystemButtonFace')
        self.BTN7.config(bg='SystemButtonFace')
        self.BTN8.config(bg='SystemButtonFace')
        self.Clearing()

        self.f3.destroy()
        self.f3 = Frame(self.root, bd=5, relief=GROOVE)
        self.f3.place(x=321, y=240, width=880, height=550)

        self.LABEL1Variable.set('Removing Item')
        self.LABEL2Variable.set('Select Item Type')
        self.LABEL3Variable.set('Select Item')
        self.LABEL4Variable.set('Select In-Party')
        self.LABEL5Variable.set('Selling Price')
        self.LABEL6Variable.set('Quantity & Unit')
        self.LABEL7Variable.set('Sold To')

        self.LABEL1 = Label(self.f3, text=self.LABEL1Variable.get(), font=('Agency FB', 20, 'bold'), bd=3, relief=RIDGE)
        self.LABEL1.place(x=10, y=10, width=400, height=40)

        self.LABEL2 = Label(self.f3, text=self.LABEL2Variable.get(), font=('Agency FB', 15, 'bold'), bd=3, relief=RIDGE)
        self.LABEL2.place(x=10, y=60, width=150, height=30)

        def CheckItemType():
            def CheckItem():
                def CheckInParty():
                    self.InParty = InPartycmb.get()
                    if self.InParty == 'Select':
                        messagebox.showerror('ERROR', 'Select InParty')
                    else:
                        Details()

                self.Item = Itemcmb.get()
                if self.Item == 'Select':
                    messagebox.showerror('ERROR', 'Select Item')
                else:
                    self.LABEL4 = Label(self.f3, text=self.LABEL4Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                        relief=RIDGE)
                    self.LABEL4.place(x=10, y=140, width=150, height=30)
                    InParty = InPartyCreationSelection.InPartyList(self.ItemType, self.Item)
                    InParty[0] = 'Select'
                    InPartycmb = ttk.Combobox(self.f3, value=InParty)
                    InPartycmb.place(x=170, y=140, width=150, height=30)
                    InPartycmb.current(0)
                    Checkbtn = Button(self.f3, text="✔", font="lucida 10 bold", relief=RAISED, border=3,
                                      command=CheckInParty)
                    Checkbtn.place(x=335, y=140, height=30)

            # Check Selected Item Type and return items in particular item type
            self.ItemType = ItemTypecmb.get()
            if self.ItemType == 'Select':
                messagebox.showerror('ERROR', 'Select Item Price')
            else:
                self.LABEL3 = Label(self.f3, text=self.LABEL3Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                    relief=RIDGE)
                self.LABEL3.place(x=10, y=100, width=150, height=30)

                Item = ItemHouse.ItemList(self.ItemType)
                Item[0] = 'Select'
                Itemcmb = ttk.Combobox(self.f3, value=Item)
                Itemcmb.place(x=170, y=100, width=150, height=30)
                Itemcmb.current(0)
                Checkbtn = Button(self.f3, text="✔", font="lucida 10 bold", relief=RAISED, border=3, command=CheckItem)
                Checkbtn.place(x=335, y=100, height=30)

        ItemType = itemTypeLists.itemType
        ItemType[0] = 'Select'
        ItemTypecmb = ttk.Combobox(self.f3, value=ItemType)
        ItemTypecmb.place(x=170, y=60, width=150, height=30)
        ItemTypecmb.current(0)
        Checkbtn = Button(self.f3, text="✔", font="lucida 10 bold", relief=RAISED, border=3, command=CheckItemType)
        Checkbtn.place(x=335, y=60, height=30)

        def Details():
            def Detail():
                self.price = self.LABEL5ENTRY5Variable.get()
                self.quantity = self.LABEL6ENTRY6Variable.get()
                self.unit = Unitcmb.get()
                self.reason = self.LABEL7ENTRY7Variable.get()

                if self.price == '':
                    messagebox.showerror('ERROR', 'Enter Price')
                elif self.price == '':
                    messagebox.showerror('ERROR', 'Enter Price')
                elif self.unit == 'Select':
                    messagebox.showerror('ERROR', 'Select Unit')

                else:
                    self.RemoveItemFinal()

            self.LABEL5 = Label(self.f3, text=self.LABEL5Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                relief=RIDGE)
            self.LABEL5.place(x=10, y=190, width=150, height=30)

            self.LABEL5ENTRY5 = Entry(self.f3, text=self.LABEL5ENTRY5Variable, font=('Agency FB', 15, 'bold'), bd=3,
                                      relief=RIDGE)
            self.LABEL5ENTRY5.place(x=170, y=190, width=100, height=30)

            self.LABEL6 = Label(self.f3, text=self.LABEL6Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                relief=RIDGE)
            self.LABEL6.place(x=10, y=220, width=150, height=30)
            self.LABEL6ENTRY6 = Entry(self.f3, text=self.LABEL6ENTRY6Variable, font=('Agency FB', 15, 'bold'), bd=3,
                                      relief=RIDGE)
            self.LABEL6ENTRY6.place(x=170, y=220, width=100, height=30)

            Unit = itemTypeLists.UnitType
            Unitcmb = ttk.Combobox(self.f3, value=Unit)
            Unitcmb.place(x=280, y=220, width=70, height=30)
            Unitcmb.current(0)

            self.LABEL7 = Label(self.f3, text=self.LABEL7Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                relief=RIDGE)
            self.LABEL7.place(x=10, y=260, width=150, height=30)

            self.LABEL7ENTRY7 = Entry(self.f3, text=self.LABEL7ENTRY7Variable, font=('Agency FB', 15, 'bold'), bd=3,
                                      relief=RIDGE)
            self.LABEL7ENTRY7.place(x=170, y=260, width=150, height=30)

            self.SubmitBTN = Button(self.f3, text='Remove Item', font=('Agency FB', 18, 'bold'), bd=3, relief=RIDGE,
                                    command=Detail)
            self.SubmitBTN.place(x=460, y=310, width=390, height=40)

    def RemoveItemFinal(self):
        IT = self.ItemType
        I = self.Item
        IP = self.InParty
        P = self.price
        Q = self.quantity
        U = self.unit
        R = self.reason

        InventoryHouse.RemoveItemFromInventoryDetailed(IT, I, IP, P, Q, U, R)

        self.f3.destroy()

        self.Clearing()
        self.BTN1.config(bg='SystemButtonFace')
        self.BTN2.config(bg='SystemButtonFace')
        self.BTN3.config(bg='SystemButtonFace')
        self.BTN4.config(bg='SystemButtonFace')
        self.BTN5.config(bg='SystemButtonFace')
        self.BTN6.config(bg='SystemButtonFace')
        self.BTN7.config(bg='SystemButtonFace')
        self.BTN8.config(bg='SystemButtonFace')

    def CheckItemsFrame(self):
        self.BTN1.config(bg='SystemButtonFace')
        self.BTN2.config(bg='SystemButtonFace')
        self.BTN3.config(bg='yellow')
        self.BTN4.config(bg='SystemButtonFace')
        self.BTN5.config(bg='SystemButtonFace')
        self.BTN6.config(bg='SystemButtonFace')
        self.BTN7.config(bg='SystemButtonFace')
        self.BTN8.config(bg='SystemButtonFace')
        self.Clearing()

        self.f3.destroy()
        self.f3 = Frame(self.root, bd=5, relief=GROOVE)
        self.f3.place(x=321, y=240, width=880, height=550)

        self.LABEL1Variable.set('Checking Item')
        self.LABEL2Variable.set('Select Item Type')
        self.LABEL3Variable.set('Select Item')
        self.LABEL4Variable.set('Select In-Party')

        self.LABEL1 = Label(self.f3, text=self.LABEL1Variable.get(), font=('Agency FB', 20, 'bold'), bd=3, relief=RIDGE)
        self.LABEL1.place(x=10, y=10, width=400, height=40)

        self.LABEL2 = Label(self.f3, text=self.LABEL2Variable.get(), font=('Agency FB', 15, 'bold'), bd=3, relief=RIDGE)
        self.LABEL2.place(x=10, y=60, width=150, height=30)

        def CheckItemType():
            def CheckItem():
                def CheckInParty():
                    self.InParty = InPartycmb.get()
                    if self.InParty == 'Select':
                        messagebox.showerror('ERROR', 'Select item')
                    else:
                        Details()

                self.Item = Itemcmb.get()
                if self.Item == 'All':
                    self.LABEL4 = Label(self.f3, text=self.LABEL4Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                        relief=RIDGE)
                    self.LABEL4.place(x=10, y=140, width=150, height=30)
                    InParty = InPartyCreationSelection.InPartyListALL()
                    InPartycmb = ttk.Combobox(self.f3, value=InParty)
                    InPartycmb.place(x=170, y=140, width=150, height=30)
                    InPartycmb.current(0)
                    Checkbtn = Button(self.f3, text="Check Items", font="lucida 10 bold", relief=RAISED, border=3,
                                      command=CheckInParty)
                    Checkbtn.place(x=335, y=140, height=30)
                else:
                    self.LABEL4 = Label(self.f3, text=self.LABEL4Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                        relief=RIDGE)
                    self.LABEL4.place(x=10, y=140, width=150, height=30)
                    InParty = InPartyCreationSelection.InPartyList(self.ItemType, self.Item)
                    InParty[0] = 'All'
                    InPartycmb = ttk.Combobox(self.f3, value=InParty)
                    InPartycmb.place(x=170, y=140, width=150, height=30)
                    InPartycmb.current(0)
                    Checkbtn = Button(self.f3, text="Check Items", font="lucida 10 bold", relief=RAISED, border=3,
                                      command=CheckInParty)
                    Checkbtn.place(x=335, y=140, height=30)

            # Check Selected Item Type and return items in particular item type
            self.ItemType = ItemTypecmb.get()
            if self.ItemType == 'All':
                self.LABEL3 = Label(self.f3, text=self.LABEL3Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                    relief=RIDGE)
                self.LABEL3.place(x=10, y=100, width=150, height=30)

                Item = ItemHouse.ItemListAll()
                Itemcmb = ttk.Combobox(self.f3, value=Item)
                Itemcmb.place(x=170, y=100, width=150, height=30)
                Itemcmb.current(0)
                Checkbtn = Button(self.f3, text="✔", font="lucida 10 bold", relief=RAISED, border=3, command=CheckItem)
                Checkbtn.place(x=335, y=100, height=30)
            else:
                self.LABEL3 = Label(self.f3, text=self.LABEL3Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                    relief=RIDGE)
                self.LABEL3.place(x=10, y=100, width=150, height=30)

                Item = ItemHouse.ItemList(self.ItemType)
                Item[0] = 'All'
                Itemcmb = ttk.Combobox(self.f3, value=Item)
                Itemcmb.place(x=170, y=100, width=150, height=30)
                Itemcmb.current(0)
                Checkbtn = Button(self.f3, text="✔", font="lucida 10 bold", relief=RAISED, border=3, command=CheckItem)
                Checkbtn.place(x=335, y=100, height=30)

        ItemType = itemTypeLists.itemType
        ItemType[0] = 'All'
        ItemTypecmb = ttk.Combobox(self.f3, value=ItemType)
        ItemTypecmb.place(x=170, y=60, width=150, height=30)
        ItemTypecmb.current(0)
        Checkbtn = Button(self.f3, text="✔", font="lucida 10 bold", relief=RAISED, border=3, command=CheckItemType)
        Checkbtn.place(x=335, y=60, height=30)

        def Details():
            itemstext = InventoryHouse.CheckingItems(self.ItemType, self.Item, self.InParty)

            if itemstext != '':
                txt = Text(self.f3, font=('Agency FB', 15, 'bold'))
                txt.place(x=10, y=190, width=400, height=200)

                txt.delete(0.0, END)
                txt.insert(INSERT, itemstext)

                scrollbar = Scrollbar(txt)
                scrollbar.pack(side=RIGHT, fill=Y)
                scrollbar.config(command=txt.yview)
                txt.config(yscrollcommand=scrollbar.set)
            else:
                txt = Text(self.f3, font=('Agency FB', 15, 'bold'))
                txt.place(x=10, y=190, width=400, height=200)

                txt.delete(0.0, END)

                scrollbar = Scrollbar(txt)
                scrollbar.pack(side=RIGHT, fill=Y)
                scrollbar.config(command=txt.yview)
                txt.config(yscrollcommand=scrollbar.set)

            itemstext = InventoryHouse.AllItem(self.Item)
            if itemstext != '':
                txt = Text(self.f3, font=('Agency FB', 15, 'bold'))
                txt.place(x=430, y=190, width=400, height=200)

                txt.delete(0.0, END)
                txt.insert(INSERT, itemstext)

                scrollbar = Scrollbar(txt)
                scrollbar.pack(side=RIGHT, fill=Y)
                scrollbar.config(command=txt.yview)
                txt.config(yscrollcommand=scrollbar.set)
            else:
                txt = Text(self.f3, font=('Agency FB', 15, 'bold'))
                txt.place(x=10, y=190, width=400, height=200)

                txt.delete(0.0, END)

                scrollbar = Scrollbar(txt)
                scrollbar.pack(side=RIGHT, fill=Y)
                scrollbar.config(command=txt.yview)
                txt.config(yscrollcommand=scrollbar.set)

    def CreateInPartyFrame(self):
        self.BTN1.config(bg='SystemButtonFace')
        self.BTN2.config(bg='SystemButtonFace')
        self.BTN3.config(bg='SystemButtonFace')
        self.BTN4.config(bg='yellow')
        self.BTN5.config(bg='SystemButtonFace')
        self.BTN6.config(bg='SystemButtonFace')
        self.BTN7.config(bg='SystemButtonFace')
        self.BTN8.config(bg='SystemButtonFace')
        self.Clearing()
        self.f3.destroy()
        self.f3 = Frame(self.root, bd=5, relief=GROOVE)
        self.f3.place(x=321, y=240, width=880, height=550)

        self.LABEL1Variable.set('Creating In Party')
        self.LABEL2Variable.set('Select Item Type')
        self.LABEL3Variable.set('Select Item')

        self.LABEL5Variable.set('Party Name')
        self.LABEL6Variable.set('Party Acc No')
        self.LABEL7Variable.set('Party IFSC Code')
        self.LABEL8Variable.set('Mobile')
        self.LABEL9Variable.set('Email')

        self.LABEL1 = Label(self.f3, text=self.LABEL1Variable.get(), font=('Agency FB', 20, 'bold'), bd=3, relief=RIDGE)
        self.LABEL1.place(x=10, y=10, width=400, height=40)

        self.LABEL2 = Label(self.f3, text=self.LABEL2Variable.get(), font=('Agency FB', 15, 'bold'), bd=3, relief=RIDGE)
        self.LABEL2.place(x=10, y=60, width=150, height=30)

        def CheckItemType():
            def CheckItem():
                self.Item = Itemcmb.get()
                if self.Item == 'Select':
                    messagebox.showerror('Error', 'Select Item')
                else:
                    Details()

            self.ItemType = ItemTypecmb.get()
            if self.ItemType == 'Select':
                messagebox.showerror('Error', 'Select Item Type')
            else:
                self.LABEL3 = Label(self.f3, text=self.LABEL3Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                    relief=RIDGE)
                self.LABEL3.place(x=10, y=100, width=150, height=30)

                Item = ItemHouse.ItemList(self.ItemType)
                Item[0] = 'Select'
                Itemcmb = ttk.Combobox(self.f3, value=Item)
                Itemcmb.place(x=170, y=100, width=150, height=30)
                Itemcmb.current(0)
                Checkbtn = Button(self.f3, text="✔", font="lucida 10 bold", relief=RAISED, border=3, command=CheckItem)
                Checkbtn.place(x=335, y=100, height=30)

        ItemType = itemTypeLists.itemType
        ItemType[0] = 'Select'
        ItemTypecmb = ttk.Combobox(self.f3, value=ItemType)
        ItemTypecmb.place(x=170, y=60, width=150, height=30)
        ItemTypecmb.current(0)
        Checkbtn = Button(self.f3, text="✔", font="lucida 10 bold", relief=RAISED, border=3, command=CheckItemType)
        Checkbtn.place(x=335, y=60, height=30)

        def Details():

            self.LABEL5 = Label(self.f3, text=self.LABEL5Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                relief=RIDGE)
            self.LABEL5.place(x=10, y=190, width=150, height=30)

            self.LABEL5ENTRY5 = Entry(self.f3, text=self.LABEL5ENTRY5Variable, font=('Agency FB', 15, 'bold'), bd=3,
                                      relief=RIDGE)
            self.LABEL5ENTRY5.place(x=170, y=190, width=150, height=30)

            self.LABEL6 = Label(self.f3, text=self.LABEL6Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                relief=RIDGE)
            self.LABEL6.place(x=10, y=230, width=150, height=30)
            self.LABEL6ENTRY6 = Entry(self.f3, text=self.LABEL6ENTRY6Variable, font=('Agency FB', 15, 'bold'), bd=3,
                                      relief=RIDGE)
            self.LABEL6ENTRY6.place(x=170, y=230, width=150, height=30)

            self.LABEL7 = Label(self.f3, text=self.LABEL7Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                relief=RIDGE)
            self.LABEL7.place(x=10, y=270, width=150, height=30)

            self.LABEL7ENTRY7 = Entry(self.f3, text=self.LABEL7ENTRY7Variable, font=('Agency FB', 15, 'bold'), bd=3,
                                      relief=RIDGE)
            self.LABEL7ENTRY7.place(x=170, y=270, width=150, height=30)

            self.LABEL8 = Label(self.f3, text=self.LABEL8Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                relief=RIDGE)
            self.LABEL8.place(x=10, y=310, width=150, height=30)

            self.LABEL8ENTRY8 = Entry(self.f3, text=self.LABEL8ENTRY8Variable, font=('Agency FB', 15, 'bold'), bd=3,
                                      relief=RIDGE)
            self.LABEL8ENTRY8.place(x=170, y=310, width=150, height=30)

            self.LABEL9 = Label(self.f3, text=self.LABEL9Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                relief=RIDGE)
            self.LABEL9.place(x=10, y=350, width=150, height=30)

            self.LABEL9ENTRY9 = Entry(self.f3, text=self.LABEL9ENTRY9Variable, font=('Agency FB', 15, 'bold'), bd=3,
                                      relief=RIDGE)
            self.LABEL9ENTRY9.place(x=170, y=350, width=150, height=30)

            self.SubmitBTN = Button(self.f3, text='Create In-Party', font=('Agency FB', 18, 'bold'), bd=3, relief=RIDGE,
                                    command=self.CreateInPartyFinal)
            self.SubmitBTN.place(x=460, y=400, width=390, height=40)

    def CreateInPartyFinal(self):
        if self.LABEL5ENTRY5Variable.get() == '':
            messagebox.showerror('Error', 'Enter Party Name')
        elif self.LABEL8ENTRY8Variable.get() == '':
            messagebox.showerror('Error', 'Enter Party Mobile Number')
        else:
            IT = self.ItemType
            I = self.Item
            IP = self.LABEL5ENTRY5Variable.get()
            IPA = self.LABEL6ENTRY6Variable.get()
            IPF = self.LABEL7ENTRY7Variable.get()
            M = self.LABEL8ENTRY8Variable.get()
            E = self.LABEL9ENTRY9Variable.get()

            InPartyCreationSelection.createInParty(IT, I, IP, IPA, IPF, M, E)

    def CreateItem(self):
        self.BTN1.config(bg='SystemButtonFace')
        self.BTN2.config(bg='SystemButtonFace')
        self.BTN3.config(bg='SystemButtonFace')
        self.BTN4.config(bg='SystemButtonFace')
        self.BTN5.config(bg='yellow')
        self.BTN6.config(bg='SystemButtonFace')
        self.BTN7.config(bg='SystemButtonFace')
        self.BTN8.config(bg='SystemButtonFace')
        self.Clearing()
        self.f3.destroy()
        self.f3 = Frame(self.root, bd=5, relief=GROOVE)
        self.f3.place(x=321, y=240, width=880, height=550)

        self.LABEL1Variable.set('Creating Item')
        self.LABEL2Variable.set('Select Item Type')

        self.LABEL5Variable.set('Item Name')

        self.LABEL1 = Label(self.f3, text=self.LABEL1Variable.get(), font=('Agency FB', 20, 'bold'), bd=3, relief=RIDGE)
        self.LABEL1.place(x=10, y=10, width=400, height=40)

        self.LABEL2 = Label(self.f3, text=self.LABEL2Variable.get(), font=('Agency FB', 15, 'bold'), bd=3, relief=RIDGE)
        self.LABEL2.place(x=10, y=60, width=150, height=30)

        def CheckItemType():
            self.ItemType = ItemTypecmb.get()
            if self.ItemType == 'Select':
                messagebox.showerror('Error', 'Select Item Type')
            else:
                Details()

        ItemType = itemTypeLists.itemType
        ItemType[0] = 'Select'
        ItemTypecmb = ttk.Combobox(self.f3, value=ItemType)
        ItemTypecmb.place(x=170, y=60, width=150, height=30)
        ItemTypecmb.current(0)
        Checkbtn = Button(self.f3, text="✔", font="lucida 10 bold", relief=RAISED, border=3, command=CheckItemType)
        Checkbtn.place(x=335, y=60, height=30)

        def Details():

            self.LABEL5 = Label(self.f3, text=self.LABEL5Variable.get(), font=('Agency FB', 15, 'bold'), bd=3,
                                relief=RIDGE)
            self.LABEL5.place(x=10, y=110, width=150, height=30)

            self.LABEL5ENTRY5 = Entry(self.f3, text=self.LABEL5ENTRY5Variable, font=('Agency FB', 15, 'bold'), bd=3,
                                      relief=RIDGE)
            self.LABEL5ENTRY5.place(x=170, y=110, width=150, height=30)

            self.SubmitBTN = Button(self.f3, text='Create Item', font=('Agency FB', 18, 'bold'), bd=3, relief=RIDGE,
                                    command=self.CreateItemFinal)
            self.SubmitBTN.place(x=460, y=160, width=390, height=40)

    def CreateItemFinal(self):
        if self.LABEL5ENTRY5Variable.get() == '':
            messagebox.showerror('Error', 'Enter Item Name')
        else:
            IT = self.ItemType
            I = self.LABEL5ENTRY5Variable.get()

            ItemHouse.createItem(IT, I)

    def ClearFrames(self):
        try:
            self.f3.destroy()
        except:
            pass

        self.BTN1.config(bg='SystemButtonFace')
        self.BTN2.config(bg='SystemButtonFace')
        self.BTN3.config(bg='SystemButtonFace')
        self.BTN4.config(bg='SystemButtonFace')
        self.BTN5.config(bg='SystemButtonFace')
        self.BTN6.config(bg='SystemButtonFace')
        self.BTN7.config(bg='SystemButtonFace')
        self.BTN8.config(bg='SystemButtonFace')

    def LogOut(self):
        self.BTN1.config(bg='SystemButtonFace')
        self.BTN2.config(bg='SystemButtonFace')
        self.BTN3.config(bg='SystemButtonFace')
        self.BTN4.config(bg='SystemButtonFace')
        self.BTN5.config(bg='SystemButtonFace')
        self.BTN6.config(bg='SystemButtonFace')
        self.BTN7.config(bg='SystemButtonFace')
        self.BTN8.config(bg='SystemButtonFace')
        self.LoginBTN.config(bg='SystemButtonFace')
        try:
            self.f4.destroy()
            self.f3.destroy()
            self.f2.destroy()
        except:
            self.f2.destroy()

    def a(self):
        pass


if __name__ == '__main__':
    root = Tk()
    obj = InventoryManagement(root)
    root.overrideredirect(1)
    root.mainloop()
