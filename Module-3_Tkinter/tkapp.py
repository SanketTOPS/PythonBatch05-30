import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox

screen=tkinter.Tk()

screen.title("FirstApp")
screen.geometry("500x600")
screen.config(bg='gold')

#tkinter.Label(text="Firstname:").pack()
#tkinter.Label(text="Lastname:").pack()

#tkinter.Label(text="Firstname:",bg='gold',fg='red',font='Candara 15 bold').place(x=0,y=0)
#tkinter.Label(text="Lastname:",bg='gold',fg='red',font='Candara 15 bold').place(x=0,y=30)

tkinter.Label(text="Firstname:",bg='gold',fg='red',font='Candara 15 bold').grid(row=0,column=0,sticky='W')
tkinter.Label(text="Lastname:",bg='gold',fg='red',font='Candara 15 bold').grid(row=1,column=0,sticky='W')

tkinter.Entry().grid(row=0,column=1)
tkinter.Entry().grid(row=1,column=1)

tkinter.Radiobutton(value=0,text='Male',bg='gold',fg='red',font='Candara 15 bold').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=1,text='Female',bg='gold',fg='red',font='Candara 15 bold').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text='Python',bg='gold',fg='red',font='Candara 15 bold').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text='iOS',bg='gold',fg='red',font='Candara 15 bold').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text='JAVA',bg='gold',fg='red',font='Candara 15 bold').grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text='Android',bg='gold',fg='red',font='Candara 15 bold').grid(row=6,column=0,sticky='W')

city=['Ahmedabad','Rajkot','Baroda','Surat','Jamnagar','Bhavnagar','Junagadh']

Combobox(values=city).grid(row=7,column=0,sticky='W')

#tkinter.Button(text='Submit',font='Candara 15 bold').grid(row=8,column=0,sticky='W')

def btnclick():
    #print("This is button!")
    #messagebox.showerror("Error","Somthing went wrong...Try again!")
    messagebox.showinfo("Warning","Your disk is full!")

tkinter.Button(text='Submit',font='Candara 15 bold',command=btnclick).place(x=210,y=280)
tkinter.mainloop()