from tkinter import *

class App(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.val1=0
        self.val2=0
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.no1=Label(self,text='Enter No1: ').grid(row=1,column=0)
        self.val1=Entry(self,width=10)
        self.val1.grid(row=1,column=1)
        self.no2=Label(self,text='Enter No2: ').grid(row=2,column=0)
        self.val2=Entry(self,width=10)
        self.val2.grid(row=2,column=1)
        self.addButton=Button(self,text='+',command=self.add).grid(row=3,column=0)
        self.subButton=Button(self,text='-',command=self.sub).grid(row=3,column=1)
        self.mulButton=Button(self,text='*',command=self.mul).grid(row=4,column=0)
        self.divButton=Button(self,text='/',command=self.div).grid(row=4,column=1)


    def add(self):
        a=self.val1.get()
        b=self.val2.get()
        self.result = Label(self, text='Ans is {}'.format(int(a)+int(b))).grid(row=5, column=0)
    def sub(self):
        a = self.val1.get()
        b = self.val2.get()
        self.result = Label(self, text='Ans is {}'.format(int(a) - int(b))).grid(row=5, column=0)
    def mul(self):
        a = self.val1.get()
        b = self.val2.get()
        self.result = Label(self, text='Ans is {}'.format(int(a) * int(b))).grid(row=5, column=0)
    def div(self):
        a = self.val1.get()
        b = self.val2.get()
        self.result = Label(self, text='Ans is {}'.format(int(a) / int(b))).grid(row=5, column=0)

root=Tk()
root.title('Simple math calculator')
root.geometry('200x200')
App(root)
root.mainloop()