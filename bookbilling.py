



from tkinter import*
import random
import time
import datetime
import pymysql

def connect():
    conn=pymysql.connect(host="localhost",user="root",password="",database="bill")
    cur=conn.cursor()
    return cur

def calcTotalCost():

    CostOfOrder()

    ref = txtRef.get()
    qntJava = txtJAVA.get()
    qntPython = txtPython.get()
    qntIPS = txtIPS.get()
    tempQntHomeDelivery = qntHomeDelivery.get()
    qntDateOfOrder = txtDateofOrder.get()

    cur=connect()
    print( "qntHomeDelivery"+txtHomeDelivery.get() )
    query="insert into bill_details(sales_ref,java,python,ips,home_delivery,order_date) values( '"\
    + ref +"'," + qntJava + "," + qntPython + "," + qntIPS + "," + tempQntHomeDelivery + ",'" + qntDateOfOrder + "')"

    print( "Query : "+query )
    cur.execute(query)
    row=cur.rowcount
    '''
    if row>0:
        op.config(text="Record Inserted", fg="green")

    else:
        op.config(text="Record not inserted", fg="red") '''   

        
width = 1350
height = 650
root = Tk()
root.geometry(str(width)+"x" + str(height) + "+0+0")
root.title("Book Billing Systems")

Tops = Frame(root, width=width,bg='#afaf99', height=100, bd=8,relief='raise')
Tops.pack(side=TOP)

#main-frame
f1 = Frame(root, width=900, height=650,bg='white',relief='raise')
f1.pack(side=LEFT)
f2 = Frame(root, width=450, height=650,bg='white',relief='raise')
f2.pack(side=LEFT)
#sub-frame
f1a = Frame(f1, width=900, height=330 ,bg='white',relief='raise')
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320,bg='white',relief='raise')
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=430,bg='white',relief='raise')
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430,bg='white',relief='raise')
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330,bg='white',relief='raise')
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330,bg='white',relief='raise')
f2ab.pack(side=LEFT)

lblInfo=Label(Tops, font=('italics',60,'bold'),text ="Books Billing system",bg='#09e6e6', bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

#calculator's screen
text_Input=StringVar()
operator=""

def btnClick(numbers):
	global operator
	operator = operator + str(numbers)
	text_Input.set(operator)

def btnClearDisplay():
	global operator
	operator=''
	text_Input.set('')

def btnEqualsInput():
	global operator
	sumup = str(eval(operator))
	text_Input.set(sumup)
	operator=''

#calculator's buttons
txtDisplay = Entry(f2,font=('italics',20,'bold'),bg='white', textvariable=text_Input,bd=30, insertwidth=6, justify='right')
txtDisplay.grid(columnspan=4)
#----------------------------------------------------
btn7 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='7',bg='#a7fffb',command=lambda:btnClick(7)).grid(row=1,column=0)
btn8 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='8',bg='#a7fffb',command=lambda:btnClick(8)).grid(row=1,column=1)
btn9 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='9',bg='#a7fffb',command=lambda:btnClick(9)).grid(row=1,column=2)
btnPlus = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='+',bg='#a7fffb',command=lambda:btnClick("+")).grid(row=1,column=3)
#----------------------------------------------------
btn4 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='4',bg='#a7fffb',command=lambda:btnClick(4)).grid(row=2,column=0)
btn5 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='5',bg='#a7fffb',command=lambda:btnClick(5)).grid(row=2,column=1)
btn6 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='6',bg='#a7fffb',command=lambda:btnClick(6)).grid(row=2,column=2)
btnSub = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='-',bg='#a7fffb',command=lambda:btnClick("-")).grid(row=2,column=3)
#----------------------------------------------------
btn1 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='1',bg='#a7fffb',command=lambda:btnClick(1)).grid(row=3,column=0)
btn2 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='2',bg='#a7fffb',command=lambda:btnClick(2)).grid(row=3,column=1)
btn3 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='3',bg='#a7fffb',command=lambda:btnClick(3)).grid(row=3,column=2)
btnMult = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='*',bg='#a7fffb',command=lambda:btnClick("*")).grid(row=3,column=3)
#----------------------------------------------------
btn0 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='0',bg='#a7fffb',command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='c',bg='#a7fffb',command=btnClearDisplay).grid(row=4,column=1)
btnEqual = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='=',bg='#a7fffb',command=btnEqualsInput).grid(row=4,column=2)
btnDiv = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='/',bg='#a7fffb',command=lambda:btnClick("/")).grid(row=4,column=3)

#==============
# ORDER's INFO
#==============
PaymentRef=StringVar()
JAVA=StringVar()
Python=StringVar()
IPS=StringVar()
HomeDelivery=StringVar()

JAVA.set(0)
Python.set(0)
IPS.set(0)
HomeDelivery.set(0)

global txtRef, txtJAVA, txtPython, txtIPS, qntHomeDelivery, txtDateofOrder

lblRef = Label(f1aa,font=('arial',16,'bold'),text='Sales Reference',bg='white',bd=16,justify='left')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1aa,font=('arial',16,'bold'),textvariable=PaymentRef,bg='white',bd=10,insertwidth=2,justify='left')
txtRef.grid(row=0,column=1)

lblJAVA = Label(f1aa,font=('arial',16,'bold'),text='JAVA',bd=16,bg='white',justify='left')
lblJAVA.grid(row=1,column=0)
txtJAVA=Entry(f1aa,font=('arial',16,'bold'),textvariable=JAVA,bd=10,bg='white',insertwidth=2,justify='left')
txtJAVA.grid(row=1,column=1)

lblPython = Label(f1aa,font=('arial',16,'bold'),text='Python',bd=16,bg='white',justify='left')
lblPython.grid(row=2,column=0)
txtPython=Entry(f1aa,font=('arial',16,'bold'),textvariable=Python,bd=10,bg='white',insertwidth=2,justify='left')
txtPython.grid(row=2,column=1)

lblIPS = Label(f1aa,font=('arial',16,'bold'),text='IPS',bd=16,bg='white',justify='left')
lblIPS.grid(row=3,column=0)
txtIPS=Entry(f1aa,font=('arial',16,'bold'),textvariable=IPS,bd=10,bg='white',insertwidth=2,justify='left')
txtIPS.grid(row=3,column=1)

lblHomeDelivery= Label(f1aa,font=('arial',16,'bold'),text='Home Delivery',bd=16,bg='white',justify='left')
lblHomeDelivery.grid(row=4,column=0)
txtHomeDelivery=Entry(f1aa,font=('arial',16,'bold'),textvariable=HomeDelivery,bd=10,bg='white',insertwidth=2,justify='left')
txtHomeDelivery.grid(row=4,column=1)
qntHomeDelivery = txtHomeDelivery


#==============
# ORDER's COST
#==============
DateofOrder=StringVar()
CostofJAVA=StringVar()
CostofPython=StringVar()
CostofIPS=StringVar()
CostofHomeDelivery=StringVar()

DateofOrder.set(time.strftime("%d/%m/%y"))

lblDateofOrder = Label(f1ab,font=('arial',16,'bold'),text='Order Date',bd=16,bg='white',anchor='w')
lblDateofOrder.grid(row=0,column=0)
txtDateofOrder=Entry(f1ab,font=('arial',16,'bold'),textvariable=DateofOrder,bd=10,bg='white',insertwidth=2,justify='left')
txtDateofOrder.grid(row=0,column=1)

lblCostofJAVA = Label(f1ab,font=('arial',16,'bold'),text='JAVA',bg='white',bd=16,anchor='w')
lblCostofJAVA.grid(row=1,column=0)
txtCostofJAVA=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostofJAVA,bd=10,bg='white',insertwidth=2,justify='left')
txtCostofJAVA.grid(row=1,column=1)


lblCostofPython = Label(f1ab,font=('arial',16,'bold'),text='Python',bg='white',bd=16,anchor='w')
lblCostofPython.grid(row=2,column=0)
txtCostofPython=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostofPython,bd=10,bg='white',insertwidth=2,justify='left')
txtCostofPython.grid(row=2,column=1)

lblCostofIPS = Label(f1ab,font=('arial',16,'bold'),text='IPS',bg='white',bd=16,anchor='w')
lblCostofIPS.grid(row=3,column=0)
txtCostofIPS=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostofIPS,bd=10,bg='white',insertwidth=2,justify='left')
txtCostofIPS.grid(row=3,column=1)

lblHomeDelivery= Label(f1ab,font=('arial',16,'bold'),text='Delivery Cost ',bd=16,bg='white',anchor='w')
lblHomeDelivery.grid(row=4,column=0)
txtHomeDelivery=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostofHomeDelivery,bd=10,bg='white',insertwidth=2,justify='left')
txtHomeDelivery.grid(row=4,column=1)

#=================
# ORDER's SUMMARY
#=================
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()

lblPaidTax = Label(f2aa,font=('arial',16,'bold'),text='Paid Tax',bd=8,bg='white',anchor='w')
lblPaidTax.grid(row=2,column=0)
txtPaidTax = Entry(f2aa,font=('arial',16,'bold'),textvariable=PaidTax,bd=8,bg='white',insertwidth=2,justify='left')
txtPaidTax.grid(row=2,column=1)

lblSubTotal = Label(f2aa,font=('arial',16,'bold'),text='Sub Total',bg='white',bd=8,anchor='w')
lblSubTotal.grid(row=3,column=0)
txtSubTotal = Entry(f2aa,font=('arial',16,'bold'),textvariable=SubTotal,bd=8,bg='white',insertwidth=2,justify='left')
txtSubTotal.grid(row=3,column=1)

lblTotalCost = Label(f2aa,font=('arial',16,'bold'),text='Total Cost',bd=8,bg='white',anchor='w')
lblTotalCost.grid(row=4,column=0)
txtTotalCost = Entry(f2aa,font=('arial',16,'bold'),textvariable=TotalCost,bd=8,bg='white',insertwidth=2,justify='left')
txtTotalCost.grid(row=4,column=1)


#=====================
# ORDER's INFO BUTTONS
#=====================
from tkinter import messagebox

def iExit():
	qExit = messagebox.askyesno("Billing system","Do you want to exit the system?")
	if qExit > 0:
		root.destroy()
		return

def Reset():
	PaymentRef.set("")
	JAVA.set(0)
	Python.set(0)
	IPS.set(0)
	HomeDelivery.set(0)
	PaidTax.set("")
	SubTotal.set("")
	TotalCost.set("")
	CostofJAVA.set("")
	CostofPython.set("")
	CostofIPS.set("")
	CostofHomeDelivery.set("")

def PayReference():
	x = random.randint(10034,699812)
	randomRef = str(x)
	PaymentRef.set("BILL"+randomRef)

def CostOfOrder():
	JAVAPrice = float(JAVA.get())
	PythonPrice = float(Python.get())
	IPSPrice = float(IPS.get())
	DeliveryCost = float(HomeDelivery.get())
	
	JAVACost = "Rs." + str("%.2f"%((JAVAPrice*560.00)))
	CostofJAVA.set(JAVACost)
	
	PythonCost = "Rs." + str("%.2f"%((PythonPrice*799.00)))
	CostofPython.set(PythonCost)
	
	IPSCost = "Rs." + str("%.2f"%((IPSPrice*999.00)))
	CostofIPS.set(IPSCost)
	
	Delivery = "Rs." + str("%.2f"%((DeliveryCost*10.00)))
	CostofHomeDelivery.set(Delivery)
	
	ToC = "Rs." + str("%.2f"%((JAVAPrice*560.00)+(PythonPrice*799.00)+(IPSPrice*999.00)+(DeliveryCost*10.00)))
	SubTotal.set(ToC)
	
	Tax = "Rs." + str("%.2f"%(((JAVAPrice*15.49)+(PythonPrice*7.49)+(IPSPrice*5.50)+(DeliveryCost*10.00))*0.2))
	PaidTax.set(Tax)
	
	TaxPay = (((JAVAPrice*560.00)+(PythonPrice*799.00)+(IPSPrice*999.00)+(DeliveryCost*10.00))*0.2)
	Cost = (((JAVAPrice*560.00)+(PythonPrice*799.00)+(IPSPrice*999.00)+(DeliveryCost*10.00)))
	CostofItems = "Rs." + str("%.2f"%(TaxPay+Cost))
	TotalCost.set(CostofItems)
	
	x=random.randint(10034,699812)
	randomRef=str(x)
	PaymentRef.set("BILL"+randomRef)
		

btnTotal=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),bg='#1bf13d',width=15,text='Total Cost', command=calcTotalCost).grid(row=0,column=0)

btnRefer=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),bg='#1bf13d',width=15,text='Sales Reference', command=PayReference).grid(row=0,column=1)

btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),bg='#1bf13d',width=15,text='Reset',command=Reset).grid(row=1,column=0)

btnExit=Button(f2ab,padx=16,pady=16,bd=8,fg='black',font=('arial',16,'bold'),bg='#1bf13d',width=15,text='Exit',command=iExit).grid(row=1,column=1)



root.mainloop()
