from tkinter import *
import time
from tkinter import messagebox
password = "1234"
balance = 5000
root = Tk()
root.title("ATM")
root.resizable(False, False)



def onButtonClick(value):
    current = pdisplay.get()
    pdisplay.delete(0, END)
    pdisplay.insert(0, str(current) + str(value))

def widamt(amt):
    global balance
    withdraw_amount=int(pdisplay.get())
    pdisplay.delete(0, END)
    balance = amt - withdraw_amount
    messagebox.showwarning(title="Withdraw", message="Amount WithDraw "+str(withdraw_amount))
    messagebox.showinfo(title="Balance", message="Your Balance is "+str(balance))
    label.config(text="1 == balance \n2 == withdraw balance \n3 == deposit balance \n4 == exit")
    buttn_dep.grid_remove()
    buttn_wid.grid_remove()
    buttn_ok.grid_remove()
    buttn_sub.grid(row=3, column=3)



def depamt(amt):
    global balance
    deposit_amount=int(pdisplay.get())
    pdisplay.delete(0, END)
    balance = amt + deposit_amount
    messagebox.showinfo(title="Deposit", message="Ammount Deposit "+str(deposit_amount))
    messagebox.showinfo(title="Balance", message="Your Balance is "+str(balance))
    label.config(text="1 == balance \n2 == withdraw balance \n3 == deposit balance \n4 == exit")
    buttn_dep.grid_remove()
    buttn_wid.grid_remove()
    buttn_ok.grid_remove()
    buttn_sub.grid(row=3, column=3)



def func():
    option = int(pdisplay.get())
    if option == 1:
        pdisplay.delete(0, END)
        messagebox.showinfo(title="Balance", message="Your Balance is "+str(balance))

    elif option == 2:
        pdisplay.delete(0, END)
        label.config(text="Please Enter Withdraw_amount")
        buttn_sub.grid_remove()
        buttn_dep.grid_remove()
        buttn_wid.grid(row=3, column=3)

    elif option == 3:
        pdisplay.delete(0, END)
        label.config(text="Please Enter Deposit_amount")
        buttn_wid.grid_remove()
        buttn_sub.grid_remove()
        buttn_dep.grid(row=3, column=3)

    elif option == 4:
        pdisplay.delete(0, END)
        label.config(text="Please insert Your CARD")
        pdisplay.grid_remove()
        buttn_dep.grid_remove()
        buttn_wid.grid_remove()
        buttn_sub.grid_remove()
        buttn_ok.grid(row=3, column=3)

    




def Del():
    data = pdisplay.get()
    data = data[:-1]
    pdisplay.delete(0, END)
    pdisplay.insert(0, str(data))

def Clear():
    pdisplay.delete(0,END)

def insert():
    time.sleep(2)
    label.config(text="Enter your ATM Pin")
    pdisplay.grid(row=1, column=0, columnspan=4,  pady=10)

def pin():
    cpin = pdisplay.get()
    pdisplay.delete(0, END)
    if password == cpin:
        label.config(text="1 == balance \n2 == withdraw balance \n3 == deposit balance \n4 == exit")
        buttn_ok.grid_remove()
        buttn_sub.grid(row=3, column=3)

    else:
        messagebox.showerror(title="Error", message="Wrong Pin")
        time.sleep(2)
        label.config(text="Enter your ATM Pin")


    
myframe=Frame(root,width=40)
myframe.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

label = Label(myframe, text="Please insert Your CARD",font=("Helvetica",15))
label.grid(row=0,column=0,columnspan=4)
pdisplay = Entry(myframe, width=40, borderwidth=1, font=("Arial", 16))



buttn_1 = Button(root, width= 9, text="1", font=("Arial", 12),command=lambda:onButtonClick(1))
buttn_1.grid(row=1, column=0)
buttn_2 = Button(root, width= 9, text="2", font=("Arial", 12),command=lambda:onButtonClick(2))
buttn_2.grid(row=1, column=1)
buttn_3 = Button(root, width= 9, text="3", font=("Arial", 12),command=lambda:onButtonClick(3))
buttn_3.grid(row=1, column=2)
buttn_c = Button(root, width= 9, text="Clear", font=("Arial", 12), foreground="red",command=lambda:Clear())
buttn_c.grid(row=1, column=3)

buttn_4 = Button(root, width= 9, text="4", font=("Arial", 12),command=lambda:onButtonClick(4))
buttn_4.grid(row=2, column=0)
buttn_5 = Button(root, width= 9, text="5", font=("Arial", 12),command=lambda:onButtonClick(5))
buttn_5.grid(row=2, column=1)
buttn_6 = Button(root, width= 9, text="6", font=("Arial", 12),command=lambda:onButtonClick(6))
buttn_6.grid(row=2, column=2)
buttn_del = Button(root, width= 9, text="Del", font=("Arial", 12), foreground="green",command=lambda:Del())
buttn_del.grid(row=2, column=3)

buttn_7 = Button(root, width= 9, text="7", font=("Arial", 12),command=lambda:onButtonClick(7))
buttn_7.grid(row=3, column=0)
buttn_8 = Button(root, width= 9, text="8", font=("Arial", 12),command=lambda:onButtonClick(8))
buttn_8.grid(row=3, column=1)
buttn_9 = Button(root, width= 9, text="9", font=("Arial", 12),command=lambda:onButtonClick(9))
buttn_9.grid(row=3, column=2)
buttn_ok = Button(root, width= 9, text="Ok", font=("Arial", 12), foreground="green",command=lambda:pin())
buttn_ok.grid(row=3, column=3)
buttn_sub = Button(root, width= 9, text="Ok", font=("Arial", 12), foreground="green",command=lambda:func())
buttn_wid = Button(root, width= 9, text="Ok", font=("Arial", 12), foreground="green",command=lambda:widamt(balance))
buttn_dep = Button(root, width= 9, text="Ok", font=("Arial", 12), foreground="green",command=lambda:depamt(balance))


buttn_0= Button(root, width= 9, text="0", font=("Arial", 12),command=lambda:onButtonClick(0))
buttn_0.grid(row=4, column=1)
buttn_in= Button(root, width= 9, text="Insert Card", font=("Arial", 12),foreground="green",command=lambda:insert())
buttn_in.grid(row=4, column=3)



root.mainloop()

