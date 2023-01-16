from tkinter import *

class loanCal:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.configure(background="orange")

        Label(window, font='robotomono 12 bold', bg='orange',text='Annual Interest Rate').grid(row=1, column=1, sticky=W)
        Label(window, font='robotomono 12 bold', bg='orange',text='Number of Years').grid(row=2, column=1, sticky=W)
        Label(window, font='robotomono 12 bold', bg='orange',text='Loan Amount').grid(row=3, column=1, sticky=W)
        Label(window, font='robotomono 12 bold', bg='orange',text='Monthly Payment').grid(row=4, column=1, sticky=W)
        Label(window, font='robotomono 12 bold', bg='orange',text='Total Payment').grid(row=5, column=1, sticky=W)

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2)
        
        self.numberofYearVar = StringVar()
        Entry(window, textvariable=self.numberofYearVar, justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, font='robotomono 12 bold', bg='orange', textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)
       
        self.totalPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, font='robotomono 12 bold', bg='orange', textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        btComputePayment = Button(window, text='Compute Payment', bg='red', fg='white', font='robotomono 14 bold', command=self.computePayment).grid(row=6, column=2, sticky=E)
        btClear = Button(window, text='Clear', bg='blue', fg='white', font='robotomono 14 bold', command=self.delete_all).grid(row=6, column=8, padx=20, pady=20, sticky=E)       

        window.mainloop()


    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get())/1200,
            int(self.numberofYearVar.get())
        )

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get())*12 \
            *int(self.numberofYearVar.get())


        self.totalPaymentVar.set(format(totalPayment, '10.2f'))


    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberofYears):
        monthlyPayment = loanAmount*monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(numberofYears*12))
        return monthlyPayment

    
    def delete_all(self):
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberofYearVar.set("")
        self.totalPaymentVar.set("")

loanCal()
        