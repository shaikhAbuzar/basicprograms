from tkinter import *
class App(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        text1 = Label(self,text='Enter No 1: ').grid(row=0,column=0)
        self.no1 = Entry(self)
        self.no1.grid(row=0,column=1)
        
        text2 = Label(self,text='Enter No 2: ').grid(row=1,column=0)
        self.no2 = Entry(self)
        self.no2.grid(row=1,column=1)

        plus = Button(self,text='+',command=self.add).grid(row=2,column=0)
        minus = Button(self,text='-',command=self.sub).grid(row=2,column=1)
        mul = Button(self,text='*',command=self.mult).grid(row=3,column=0)
        div = Button(self,text='/',command=self.divi).grid(row=3,column=1)

    def add(self):
        ans = Label(self,text='Ans is {}'.format(int(self.no1.get()) + int(self.no2.get()))).grid(row=4)
    def sub(self):
        ans = Label(self,text='Ans is {}'.format(int(self.no1.get()) - int(self.no2.get()))).grid(row=4)
    def mult(self):
        ans = Label(self,text='Ans is {}'.format(int(self.no1.get()) * int(self.no2.get()))).grid(row=4)
    def divi(self):
        ans = Label(self,text='Ans is {}'.format(int(self.no1.get()) / int(self.no2.get()))).grid(row=4)

root = Tk()
root.title('Calc')
root.geometry('300x300')
a = App(root)
a.mainloop()