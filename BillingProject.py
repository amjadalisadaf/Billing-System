from tkinter import *
from tkinter import messagebox
import random
import os,sys
import tempfile
import subprocess
import smtplib
import tkinter as tk
from tkinter import ttk
from time import strftime



if not os.path.exists('bills'):
    os.mkdir('bills')

def pdfprint():
    if textarea.get(1.0, 'end') == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        file = tempfile.mktemp('.txt')
        with open(file, 'w') as f:
            f.write(textarea.get(1.0, 'end'))
        os.startfile(file, 'print')



def clear():
    meatEntry.delete(0, 'end')
    meatEntry.insert(0, 0)
    
    riceEntry.delete(0, 'end')
    riceEntry.insert(0, 0)
    
    bodyloationEntry.delete(0, 'end')
    bodyloationEntry.insert(0, 0)
    
    hairgelEntry.delete(0, 'end')
    hairgelEntry.insert(0, 0)
    
    hairwashEntry.delete(0, 'end')
    hairwashEntry.insert(0, 0)
    
    facewashEntry.delete(0, 'end')
    facewashEntry.insert(0, 0)
    
    facecreamEntry.delete(0, 'end')
    facecreamEntry.insert(0, 0)
    
    bathSopeEntry.delete(0, 'end')
    bathSopeEntry.insert(0, 0)
    
    TeaEntry.delete(0, 'end')
    TeaEntry.insert(0, 0)
    
    sugarEntry.delete(0, 'end')
    sugarEntry.insert(0, 0)
    
    oliEntry.delete(0, 'end')
    oliEntry.insert(0, 0)
    
    daadaEntry.delete(0, 'end')
    daadaEntry.insert(0, 0)
    
    rouhafzaEntry.delete(0, 'end')
    rouhafzaEntry.insert(0, 0)
    
    JamshareenEntry.delete(0, 'end')
    JamshareenEntry.insert(0, 0)
    
    fantaEntry.delete(0, 'end')
    fantaEntry.insert(0, 0)
    
    pasiEntry.delete(0, 'end')
    pasiEntry.insert(0, 0)
    
    cookaEntry.delete(0, 'end')
    cookaEntry.insert(0, 0)
    
    guloEntry.delete(0, 'end')
    guloEntry.insert(0, 0)
    
    nameEntry.delete(0, 'end')
    
    
    phoneEntry.delete(0, 'end')

    GEntry.delete(0,'end')
    GEntry.insert(0,0)

    fwEntry(0,'end')
    fwEntry.insert(0,0)
    
    cosmeticstaxEntry.delete(0, 'end')
    cosmeticstaxEntry.insert(0,0)
    
    drinktaxEntry.delete(0, 'end')
    drinktaxEntry.insert(0, 0)
    
    grotaxEntry.delete(0, 'end')
    grotaxEntry.insert(0, 0)
    
    
 


def sendEmail():
    def sendGEmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com')  # Fix the SMTP server address
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = emailTextarea.get(1.0, 'end-1c')  # Fix the syntax for getting the message from Text widget
            ob.sendmail(senderEntry.get(), reciverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Email is successfully sent')  # Remove 'Bill' from the success message
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror('Error', 'Your Password or Email is not correct or not registered')
        root1.destroy()
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        root1 = Toplevel()
        root1.grab_current()
        root1.title('Send Email')
        root1.config(bg='gray20')
        root1.resizable(0, 0)
        

        senderFrame = LabelFrame(root1, text='SENDER EMAIL', font=('arial', 12, 'bold'), bd=6, bg='gray20', fg='White', relief=GROOVE)
        senderFrame.grid(row=0, column=0, padx=40, pady=20)

        gmailIdlabel = Label(senderFrame, text='Send Email', font=('arial', 12, 'bold'), bd=6, bg='gray20', fg='gold', relief=GROOVE)
        gmailIdlabel.grid(row=0, column=0, padx=10, pady=8)


        senderEntry = Entry(senderFrame, font=('arial', 12, 'bold'), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordlabel = Label(senderFrame, text='Passward', font=('arial', 12, 'bold'), bd=6, bg='gray20', fg='gold', relief=GROOVE)
        passwordlabel.grid(row=1, column=0, padx=10, pady=8)


        passwordEntry = Entry(senderFrame, font=('arial', 12, 'bold'), bd=2, width=23, relief=RIDGE, show='**')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        ricipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 12, 'bold'), bd=6, bg='gray20', fg='White', relief=GROOVE)
        ricipientFrame.grid(row=1, column=0, padx=40, pady=20)

        reciverLabel = Label(ricipientFrame, text='Send Email', font=('arial', 12, 'bold'), bd=6, bg='gray20', fg='gold', relief=GROOVE)
        reciverLabel.grid(row=0, column=0, padx=10, pady=8)


        reciverEntry = Entry(ricipientFrame, font=('arial', 12, 'bold'), bd=2, width=23, relief=RIDGE)
        reciverEntry.grid(row=0, column=1, padx=10, pady=8)

        massagelabel = Label(ricipientFrame, text='Massage', font=('arial', 12, 'bold'), bd=6, bg='gray20', fg='gold', relief=GROOVE)
        massagelabel.grid(row=1, column=0, padx=10, pady=8)


        massageEntry = Entry(ricipientFrame, font=('arial', 12, 'bold'), bd=2, width=23, relief=RIDGE)
        massageEntry.grid(row=1, column=1, padx=10, pady=8)

        textMassageFrame = LabelFrame(root1, text='Text Massage', font=('arial', 12, 'bold'), bd=6, bg='gray20', fg='White', relief=GROOVE)
        textMassageFrame.grid(row=2, column=0, padx=40, pady=20)

        Textarealable = Label(textMassageFrame, text='Bill', font=('arial', 12, 'bold'), bd=6, bg='gray20', fg='gold', relief=GROOVE)
        Textarealable.grid(row=0, column=0, padx=10, pady=8)

        emailTextarea=Text(textMassageFrame,font=('arial', 12, 'bold'),bd=2, relief=SUNKEN, width=42,height=11 )
        emailTextarea.grid(row=2, column=0, columnspan=2)
        emailTextarea.delete(1.0,END)
        emailTextarea.insert(END,textarea.get(1.0, END).replace('=','').replace('.',''))


        sendButten=Button(root1,text='SEND BILL',font=('arial', 12, 'bold'),width=20,command=sendGEmail)
        sendButten.grid(row=4,column=0, pady=20)
        
  


                                              



def searchBill():
    bill_number = billEntry.get().strip()  # Strip any leading or trailing whitespace

    if not bill_number:
        messagebox.showerror('Error', 'Please enter a bill number')
        return

    found = False
    for i in os.listdir('bills/'):
        if i.split('.')[0] == bill_number:
            found = True
            with open(f'bills/{i}', 'r') as file:
                textarea.delete(1.0, END)
                for data in file:
                    textarea.insert(END, data)
            break

    if not found:
        messagebox.showerror('Error', 'Invalid bill number')

def my_time():
    time_string = now.strftime("%d/%m/%Y %H:%M:%S")  # time format 
    l1.config(text=now.time_string)
    l1.after(1000, my_time)  # time delay of 1000 milliseconds 

my_font = ('times', 52, 'bold')  # display size and style

# my_w = tk.Tk()

def saveBill():
    global bill_number
    result = messagebox.askyesno('Confirm', 'Do you want to save the Bill')
    if result:
        billContent = textarea.get(1.0, END)
        file = open(f'bills/{bill_number}.txt', 'w')
        file.write(billContent)
        file.close()  # Make sure to call close() to properly close the file
        messagebox.showinfo('Success', f'{bill_number} Bill is saved successfully')
        bill_number =random.randint(500,1000)
        
  
 #total Bill area
bill_number =random.randint(500,1000) # Replace this with your actual bill number or retrieve it from your program logic

def billArea():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error', 'Customer Details Are Required')
    elif cosmeticsEntry.get() == '' and GEntry.get() == '' and fwEntry.get() == '':
        messagebox.showerror('Error', 'No Products are selected')
    elif cosmeticsEntry.get() == '0' and GEntry.get() == '0' and fwEntry.get() == '0':
        messagebox.showerror('Error', 'No Products are selected')
    else:
        # Get the current time using my_time function
        current_time = my_time()
        
        # Update the textarea with customer details and current time
        textarea.delete(1.0, END)
        textarea.insert(END, '\t\t**Welcome Customer**\n')
        textarea.insert(END, f'\nBill Name: {bill_number}')
        textarea.insert(END, f'\nTime & Date: {current_time}')  # Call my_time function
        textarea.insert(END,F'\nCustomer Name:{nameEntry.get()}')
        textarea.insert(END,F'\nPhone Number:{phoneEntry.get()}')
        textarea.insert(END,f'\n=======================================================')
        textarea.insert(END,F'\nProduct\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,f'\n=======================================================')
        if bathSopeEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t\t{bathSopeEntry.get()}\t\t\t{bathSopeValue} Rs')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamEntryValue} Rs')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace wash\t\t\t{facewashEntry.get()}\t\t\t{facewashValue} Rs')
        if hairwashEntry.get()!='0':
            textarea.insert(END,f'\nHair Wash\t\t\t{hairwashEntry.get()}\t\t\t{hairwashValue} Rs')
        if hairgelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelhValue} Rs')
        if bodyloationEntry.get()!='0':
            textarea.insert(END,f'\nBody Loation\t\t\t{bodyloationEntry.get()}\t\t\t{bodyloationValue} Rs')
        textarea.insert(END,f'\n=======================================================')
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice Basmati\t\t\t{riceEntry.get()}\t\t\t{riceValue} Rs')
        if meatEntry.get()!='0':
            textarea.insert(END,f'\nMeat Muttan\t\t\t{meatEntry.get()}\t\t\t{meatValue} Rs')
        if daadaEntry.get()!='0':
            textarea.insert(END,f'\nDaalda \t\t\t{daadaEntry.get()}\t\t\t{daadaValue} Rs')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar \t\t\t{sugarEntry.get()}\t\t\t{suGarValue} Rs')
        if TeaEntry.get()!='0':
            textarea.insert(END,f'\nTapal Tea\t\t\t{TeaEntry.get()}\t\t\t{teaValue} Rs')
        textarea.insert(END,f'\n=======================================================')
        if rouhafzaEntry.get()!='0':
            textarea.insert(END,f'\nRouh Afza\t\t\t{rouhafzaEntry.get()}\t\t\t{rouhafzaValue} Rs')
        if JamshareenEntry.get()!='0':
            textarea.insert(END,f'\nJamshareen\t\t\t{JamshareenEntry.get()}\t\t\t{JamshareenValue} Rs') 
        if fantaEntry.get()!='0':
            textarea.insert(END,f'\nRouh Afza\t\t\t{fantaEntry.get()}\t\t\t{fantaValue} Rs')  
        if pasiEntry.get()!='0':
            textarea.insert(END,f'\nGormay\t\t\t{pasiEntry.get()}\t\t\t{paspiValue} Rs')  
        if cookaEntry.get()!='0':
            textarea.insert(END,f'\nRCoCa Kola\t\t\t{cookaEntry.get()}\t\t\t{CoookeValue} Rs')
        if guloEntry.get()!='0':
            textarea.insert(END,f'\nGula Ganda\t\t\t{guloEntry.get()}\t\t\t{gulooValue} Rs')   
        textarea.insert(END,f'\n=======================================================')
        if cosmeticstaxEntry.get()!='0':
            textarea.insert(END,f'\nCosmetics Tax\t\t\t\t\t{cosmeticstaxEntry.get()} Rs')
        if grotaxEntry.get()!='0':
            textarea.insert(END,f'\nGrosery Tax\t\t\t\t\t{grotaxEntry.get()} Rs')
        if drinktaxEntry.get()!='0':
            textarea.insert(END,f'\nGST Tax\t\t\t\t\t{drinktaxEntry.get()} Rs')
        textarea.insert(END,f'\n=======================================================')
        textarea.insert(END,f'\nTotal Bill\t\t\t\t\t {totalbill} Rs')
        
        

    saveBill()
        
              

#total amout area 
def total():
    global rouhafzaValue,JamshareenValue,fantaValue,paspiValue,CoookeValue,gulooValue,bathSopeValue,facecreamEntryValue,facewashValue,hairwashValue,hairgelhValue,bodyloationValue,riceValue,meatValue,oliValue,teaValue,daadaValue,suGarValue
    global totalbill,fwtax1,grocerytax,cosmeticstax
    bathSopeValue =int(bathSopeEntry.get())*50
    facecreamEntryValue =int(facecreamEntry.get())*50
    facewashValue =int(facewashEntry.get())*50
    hairwashValue =int(hairwashEntry.get())*50
    hairgelhValue =int(hairgelEntry.get())*50
    bodyloationValue =int(bodyloationEntry.get())*50
    
    cosmeticsPrice =bathSopeValue+facecreamEntryValue+facewashValue+hairwashValue+hairgelhValue+bodyloationValue
    allprice=bathSopeValue+facecreamEntryValue+facewashValue+hairwashValue+hairgelhValue+bodyloationValue
    cosmeticsEntry.delete(0,END)
    cosmeticsEntry.insert(0,allprice)


    cosmeticstaxEntry.delete(0,END)
    cosmeticstax = cosmeticsPrice*0.5
    cosmeticstaxEntry.insert(0,cosmeticstax)
    
    
    riceValue =int(riceEntry.get())*10
    meatValue =int(meatEntry.get())*10
    oliValue =int(oliEntry.get())*50
    daadaValue = int(daadaEntry.get())*50
    suGarValue=int(sugarEntry.get())*15
    teaValue =int(TeaEntry.get())*50

    groceryprice=riceValue+meatValue+oliValue+teaValue+daadaValue+suGarValue

    gallprice=riceValue+meatValue+oliValue+teaValue+daadaValue+suGarValue
    GEntry.delete(0,END)
    GEntry.insert(0,gallprice)
    
    #tax vlue
    grotaxEntry.delete(0,END)
    grocerytax=groceryprice*0.5
    grotaxEntry.insert(0,grocerytax)
   


    rouhafzaValue =int(rouhafzaEntry.get())*150
    JamshareenValue =int(JamshareenEntry.get())*150
    fantaValue =int(fantaEntry.get())*150
    paspiValue =int(pasiEntry.get())*150
    CoookeValue =int(cookaEntry.get())*150
    gulooValue =int(guloEntry.get())*90

    drinktaxPrice=rouhafzaValue+JamshareenValue+fantaValue+paspiValue+CoookeValue+gulooValue
    dallprice=rouhafzaValue+JamshareenValue+fantaValue+paspiValue+CoookeValue+gulooValue
    fwEntry.delete(0,END)
    fwEntry.insert(0,dallprice)
    
    drinktaxEntry.delete(0,END)
    fwtax1 = drinktaxPrice*0.2
    drinktaxEntry.insert(0,fwtax1)
    
    
    totalbill=cosmeticsPrice+groceryprice+drinktaxPrice+fwtax1+grocerytax+cosmeticstax

    
def my_time():
    time_string = strftime('%H:%M:%S %p')  # time format 
    l1.config(text=time_string)
    l1.after(1000, my_time)  # time delay of 1000 milliseconds 

my_font = ('times', 20, 'bold')  # display size and style


#GUI
root=Tk()
root.title('Billing System Created by Amjad Ali')
root.geometry('1270x685')
# root.iconbitmap('icon.ico')

headinLabel = Label(root,text='Retail Billing System', font=('TIMES NEW ROMAN' , 30,'bold') ,bg='gray20',fg='gold', bd=12,relief=GROOVE)
headinLabel.pack(fill='x' ,pady=10)

customer_details_frame = LabelFrame(root, text='Coustmar Detail', font=('times new roman', 15,'bold'), bg='gray20',fg='gold', bd=8,relief=GROOVE)
customer_details_frame.pack(fill='x')

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15, 'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0 , column=0,padx=20)

nameEntry = Entry(customer_details_frame,font=('time new roman',15), bd=7,width=18)
nameEntry.grid(row=0 ,column=1,padx=8)


phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15, 'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0 , column=2,padx=20)

phoneEntry = Entry(customer_details_frame,font=('time new roman',15), bd=7,width=18)
phoneEntry.grid(row=0 ,column=3,padx=8)

billLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15, 'bold'),bg='gray20',fg='white')
billLabel.grid(row=0 , column=4,columnspan=2, padx=20)

billEntry = Entry(customer_details_frame,font=('time new roman',15), bd=7,width=18)
billEntry.grid(row=0 ,column=5,padx=8)

searchButton=Button(customer_details_frame, text='Search', font=('arial',12,'bold'),bd=10,bg='blue',fg='white', width= 8, command= searchBill )
searchButton.grid(row=0,column=6,padx=20,pady=20)

l1 = ttk.Label(customer_details_frame, font=my_font, background='black', foreground='cyan')
l1.grid(row=0, column=7)


productFrame=Frame(root)
productFrame.pack(pady=10)

cosmeticsFrame = LabelFrame(productFrame, text='Cosmetics', font=('times new roman', 15,'bold'), bg='gray20',fg='gold', bd=8,relief=GROOVE)
cosmeticsFrame.grid(row=0, column=0)

bathSopeLabel=Label(cosmeticsFrame, text='Bath Sope', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
bathSopeLabel.grid(row=0, column=0, pady=9 , padx=10, sticky='w')

bathSopeEntry =Entry(cosmeticsFrame, font=('arial',12), bg='white',bd=7,width=10)
bathSopeEntry.grid(row=0,column=1,pady=9, padx=10)
bathSopeEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame, text='facecream', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

facecreamEntry =Entry(cosmeticsFrame, font=('arial',12), bg='white',bd=7,width=10)
facecreamEntry.grid(row=1,column=1,pady=9, padx=10, sticky='w')
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame, text='Face Wash', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

facewashEntry =Entry(cosmeticsFrame, font=('arial',12), bg='white',bd=7,width=10)
facewashEntry.grid(row=2,column=1,pady=9, padx=10, sticky='w')
facewashEntry.insert(0,0)

hairwashLabel=Label(cosmeticsFrame, text='Hair Wash', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
hairwashLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

hairwashEntry =Entry(cosmeticsFrame, font=('arial',12), bg='white',bd=7,width=10)
hairwashEntry.grid(row=3,column=1,pady=9, padx=10, sticky='w')
hairwashEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame, text='Hair Gel', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
hairgelLabel.grid(row=4, column=0, pady=9, padx=10 , sticky='w')

hairgelEntry =Entry(cosmeticsFrame, font=('arial',12), bg='white',bd=7,width=10)
hairgelEntry.grid(row=4,column=1,pady=9, padx=10, sticky='w')
hairgelEntry.insert(0,0)

bodyloationLabel=Label(cosmeticsFrame, text='Body loation', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
bodyloationLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

bodyloationEntry =Entry(cosmeticsFrame, font=('arial',12), bg='white',bd=7,width=10)
bodyloationEntry.grid(row=5,column=1,pady=9)
bodyloationEntry.insert(0,0)

GFrame = LabelFrame(productFrame, text='Groscry', font=('times new roman', 15,'bold'), bg='gray20',fg='gold', bd=8,relief=GROOVE)
GFrame.grid(row=0, column=1)

riceLabel=Label(GFrame, text='Rice', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
riceLabel.grid(row=0, column=0, pady=9 , padx=10, sticky='w')

riceEntry =Entry(GFrame, font=('arial',12), bg='white',bd=7,width=10)
riceEntry.grid(row=0,column=1,pady=9, padx=10)
riceEntry.insert(0,0)

meatLabel=Label(GFrame, text='meat', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
meatLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

meatEntry =Entry(GFrame, font=('arial',12), bg='white',bd=7,width=10)
meatEntry.grid(row=1,column=1,pady=9, padx=10, sticky='w')
meatEntry.insert(0,0)

oliLabel=Label(GFrame, text='oil', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
oliLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

oliEntry =Entry(GFrame, font=('arial',12), bg='white',bd=7,width=10)
oliEntry.grid(row=2,column=1,pady=9, padx=10, sticky='w')
oliEntry.insert(0,0)

daadaLabel=Label(GFrame, text='Daalda', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
daadaLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

daadaEntry =Entry(GFrame, font=('arial',12), bg='white',bd=7,width=10)
daadaEntry.grid(row=3,column=1,pady=9, padx=10, sticky='w')
daadaEntry.insert(0,0)

sugarLabel=Label(GFrame, text='sugar', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
sugarLabel.grid(row=4, column=0, pady=9, padx=10 , sticky='w')

sugarEntry =Entry(GFrame, font=('arial',12), bg='white',bd=7,width=10)
sugarEntry.grid(row=4,column=1,pady=9, padx=10, sticky='w')
sugarEntry.insert(0,0)


TeaLabel=Label(GFrame, text='Tea', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
TeaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

TeaEntry =Entry(GFrame, font=('arial',12), bg='white',bd=7,width=10)
TeaEntry.grid(row=5,column=1,pady=9)
TeaEntry.insert(0,0)


drankFrame = LabelFrame(productFrame, text='Cold Drink', font=('times new roman', 15,'bold'), bg='gray20',fg='gold', bd=8,relief=GROOVE)
drankFrame.grid(row=0, column=2)

rouhaLabel=Label(drankFrame, text='Rouhafza', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
rouhaLabel.grid(row=0, column=0, pady=9 , padx=10, sticky='w')

rouhafzaEntry =Entry(drankFrame, font=('arial',12), bg='white',bd=7,width=10)
rouhafzaEntry.grid(row=0,column=1,pady=9, padx=10)
rouhafzaEntry.insert(0,0)

JamshareenLabel=Label(drankFrame, text='Jamshareen', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
JamshareenLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

JamshareenEntry =Entry(drankFrame, font=('arial',12), bg='white',bd=7,width=10)
JamshareenEntry.grid(row=1,column=1,pady=9, padx=10, sticky='w')
JamshareenEntry.insert(0,0)

fantaLabel=Label(drankFrame, text='Fanta', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
fantaLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

fantaEntry =Entry(drankFrame, font=('arial',12), bg='white',bd=7,width=10)
fantaEntry.grid(row=2,column=1,pady=9, padx=10, sticky='w')
fantaEntry.insert(0,0)

pasiLabel=Label(drankFrame, text='Paspips', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
pasiLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

pasiEntry =Entry(drankFrame, font=('arial',12), bg='white',bd=7,width=10)
pasiEntry.grid(row=3,column=1,pady=9, padx=10, sticky='w')
pasiEntry.insert(0,0)

coookLabel=Label(drankFrame, text='coooke', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
coookLabel.grid(row=4, column=0, pady=9, padx=10 , sticky='w')

cookaEntry =Entry(drankFrame, font=('arial',12), bg='white',bd=7,width=10)
cookaEntry.grid(row=4,column=1,pady=9, padx=10, sticky='w')
cookaEntry.insert(0,0)

guloLabel=Label(drankFrame, text='guloo', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
guloLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

guloEntry =Entry(drankFrame, font=('arial',12), bg='white',bd=7,width=10)
guloEntry.grid(row=5,column=1,pady=9)
guloEntry.insert(0,0)

billFrame=Frame(productFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0 , column=3)

billareaLabel=Label(billFrame, text='Label Area', font=('times new roman',15, 'bold'))
billareaLabel.pack()


scrollbar = Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill='y')
textarea=Text(billFrame, height=18, width=55,yscrollcommand=scrollbar.set)
textarea.pack(fill='x')
scrollbar.config(command=textarea.yview)

billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15,'bold'), bg='gray20',fg='gold', bd=8,relief=GROOVE)
billmenuFrame.pack(pady=10)

cosmeticsPrice=Label(billmenuFrame, text='Cosmetics Price', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
cosmeticsPrice.grid(row=0, column=0, pady=9 , padx=10, sticky='w')

cosmeticsEntry =Entry(billmenuFrame, font=('arial',12), bg='white',bd=7,width=10)
cosmeticsEntry.grid(row=0,column=1,pady=9, padx=10)
cosmeticsEntry.insert(0,0)

GLabel=Label(billmenuFrame, text='Grocery Price', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
GLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

GEntry =Entry(billmenuFrame, font=('arial',12), bg='white',bd=7,width=10)
GEntry.grid(row=1,column=1,pady=9, padx=10, sticky='w')
GEntry.insert(0,0)

fwLabel=Label(billmenuFrame, text='Cold Drink Price', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
fwLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

fwEntry =Entry(billmenuFrame, font=('arial',12), bg='white',bd=7,width=10)
fwEntry.grid(row=2,column=1,pady=9, padx=10, sticky='w')
fwEntry.insert(0,0)

cosmeticstaxPrice=Label(billmenuFrame, text='Cosmetics Tax', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
cosmeticstaxPrice.grid(row=0, column=3, pady=9 , padx=10, sticky='w')

cosmeticstaxEntry =Entry(billmenuFrame, font=('arial',12), bg='white',bd=7,width=10)
cosmeticstaxEntry.grid(row=0, column=4, pady=9, padx=10)
cosmeticstaxEntry.insert(0,0)

CerytaxPrice=Label(billmenuFrame, text='Grocery Tax', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
CerytaxPrice.grid(row=1, column=3, pady=9 , padx=10, sticky='w')

grotaxEntry =Entry(billmenuFrame, font=('arial',12), bg='white',bd=7,width=10)
grotaxEntry.grid(row=1, column=4, pady=9, padx=10)
grotaxEntry.insert(0,0)

drinktaxPrice=Label(billmenuFrame, text='Drink Tax', font=('times new roman',15, 'bold'),bg='gray20',fg='white')
drinktaxPrice.grid(row=2, column=3, pady=9 , padx=10, sticky='w')

drinktaxEntry =Entry(billmenuFrame, font=('arial',12), bg='white',bd=7,width=10)
drinktaxEntry.grid(row=2, column=4, pady=9, padx=10)
drinktaxEntry.insert(0,0)

buttonFrame=Frame(billmenuFrame,bd=8, relief=GROOVE)
buttonFrame.grid(row=0 , column=5,rowspan=3)

totalButton=Button(buttonFrame, text='Total', font=('arial', 16, 'bold'),bg='gray20', fg='white',bd=5, width=8, pady=10, command= total)
totalButton.grid(row=0, column=0, pady=20, padx=5 )

buttonFrame=Frame(billmenuFrame,bd=8, relief=GROOVE)
buttonFrame.grid(row=0 , column=6,rowspan=3 )

billButton=Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'),bg='gray20', fg='white',bd=5, width=8, pady=10, command= billArea )
billButton.grid(row=0, column=0, pady=20, padx=5)

buttonFrame=Frame(billmenuFrame,bd=8, relief=GROOVE)
buttonFrame.grid(row=0 , column=7,rowspan=3 )

EmailButton=Button(buttonFrame, text='Email', font=('arial', 16, 'bold'),bg='gray20', fg='white',bd=5, width=8, pady=10, command=sendEmail )
EmailButton.grid(row=0, column=0, pady=20, padx=5)

buttonFrame=Frame(billmenuFrame,bd=8, relief=GROOVE)
buttonFrame.grid(row=0 , column=8,rowspan=3 )

PrintButton=Button(buttonFrame, text='Print', font=('arial', 16, 'bold'),bg='gray20', fg='white',bd=5, width=8, pady=10, command=pdfprint)
PrintButton.grid(row=0, column=0, pady=20, padx=5)


buttonFrame=Frame(billmenuFrame,bd=8, relief=GROOVE)
buttonFrame.grid(row=0 , column=9,rowspan=3 )

ClearButton=Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'),bg='gray20', fg='white',bd=5, width=8, pady=10, command=clear)
ClearButton.grid(row=0, column=0, pady=20, padx=5)

my_time()  



root.mainloop()