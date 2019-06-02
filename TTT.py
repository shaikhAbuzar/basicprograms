from tkinter import *

class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.button_clicks=0
        self.create_widgets()
        self.a=0
        self.b=0
        self.c=0
        self.d=0
        self.e=0
        self.f=0
        self.g=0
        self.h=0
        self.i=0

    def create_widgets(self):
        Label(self,text="TIC-TAC-TOW").grid(row=0,column=0)
        

        self.button1=Button(self)
        self.button1["command"]=self.update_count1
        self.button1.grid(row=1,column=0)
        
        self.button2=Button(self)
        self.button2["command"]=self.update_count2
        self.button2.grid(row=1,column=1)
        
        self.button3=Button(self)
        self.button3["command"]=self.update_count3
        self.button3.grid(row=1,column=2)

        self.button4=Button(self)
        self.button4["command"]=self.update_count4
        self.button4.grid(row=2,column=0)

        self.button5=Button(self)
        self.button5["command"]=self.update_count5
        self.button5.grid(row=2,column=1)

        self.button6=Button(self)
        self.button6["command"]=self.update_count6
        self.button6.grid(row=2,column=2)

        self.button7=Button(self)
        self.button7["command"]=self.update_count7
        self.button7.grid(row=3,column=0)

        self.button8=Button(self)
        self.button8["command"]=self.update_count8
        self.button8.grid(row=3,column=1)

        self.button9=Button(self)
        self.button9["command"]=self.update_count9
        self.button9.grid(row=3,column=2)
        
        self.result=Text(self,width=20,height=2,wrap=WORD)
        self.result.grid(row=4,column=0,columnspan=3)



    def update_count1(self):
        
        self.button_clicks += 1
        if self.button_clicks%2==0 :
            self.button1["text"]="X"
            self.a=1
            self.check()
        if self.button_clicks%2==1 :
            self.button1["text"]="O"
            self.a=2
            self.check()
    def update_count2(self):
        self.button_clicks += 1
        if self.button_clicks%2==0 :
            self.button2["text"]="X"
            self.b=1
            self.check()
        if self.button_clicks%2==1 :
            self.button2["text"]="O"
            self.b=2
            self.check()
            
    def update_count3(self):
        self.button_clicks += 1
        if self.button_clicks%2==0 :
            self.button3["text"]="X"
            self.c=1
            self.check()
        if self.button_clicks%2==1 :
            self.button3["text"]="O"
            self.c=2
            self.check()

    def update_count4(self):
        self.button_clicks += 1
        if self.button_clicks%2==0 :
            self.button4["text"]="X"
            self.d=1
            self.check()
        if self.button_clicks%2==1 :
            self.button4["text"]="O"
            self.d=2
            self.check()

    def update_count5(self):
        self.button_clicks += 1
        if self.button_clicks%2==0 :
            self.button5["text"]="X"
            self.e=1
            self.check()
        if self.button_clicks%2==1 :
            self.button5["text"]="O"
            self.e=2
            self.check()

    def update_count6(self):
        self.button_clicks += 1
        if self.button_clicks%2==0 :
            self.button6["text"]="X"
            self.f=1
            self.check()
        if self.button_clicks%2==1 :
            self.button6["text"]="O"
            self.f=2
            self.check()

    def update_count7(self):
        self.button_clicks += 1
        if self.button_clicks%2==0 :
            self.button7["text"]="X"
            self.g=1
            self.check()
        if self.button_clicks%2==1 :
            self.button7["text"]="O"
            self.g=2
            self.check()

    def update_count8(self):
        self.button_clicks += 1
        if self.button_clicks%2==0 :
            self.button8["text"]="X"
            self.h=1
            self.check()
        if self.button_clicks%2==1 :
            self.button8["text"]="O"
            self.h=2
            self.check()

    def update_count9(self):
        self.button_clicks += 1
        if self.button_clicks%2==0 :
            self.button9["text"]="X"
            self.i=1
            self.check()
        if self.button_clicks%2==1 :
            self.button9["text"]="O"
            self.i=2
            self.check()

    def check(self):
        if (self.a==1 and self.b==1 and self.c==1 ):
            self.delete()
            self.result.insert(0.0,"X has won")
            self.clear()
        elif (self.a==1 and self.d==1 and self.g==1 ):
            self.delete()
            self.result.insert(0.0,"X has won")
            self.clear()
        elif (self.a==1 and self.e==1 and self.i==1 ):
            self.delete()
            self.result.insert(0.0,"X has won")
            self.clear()
        elif (self.c==1 and self.e==1 and self.g==1 ):
            self.delete()
            self.result.insert(0.0,"X has won")
            self.clear()
        elif (self.d==1 and self.e==1 and self.f==1 ):
            self.delete()
            self.result.insert(0.0,"X has won")
            self.clear()
        elif (self.g==1 and self.h==1 and self.i==1 ):
            self.delete()
            self.result.insert(0.0,"X has won")
            self.clear()
        elif (self.c==1 and self.f==1 and self.i==1):
            self.delete()
            self.result.insert(0.0,"X has won")
            self.clear()
        elif (self.b==1 and self.e==1 and self.h==1):
            self.delete()
            self.result.insert(0.0,"X has won")
            self.clear()
        elif (self.a==2 and self.b==2 and self.c==2 ):
            self.delete()
            self.result.insert(0.0,"O has won")
            self.clear()
        elif (self.a==2 and self.d==2 and self.g==2 ):
            self.delete()
            self.result.insert(0.0,"O has won")
            self.clear()
        elif (self.a==2 and self.e==2 and self.i==2 ):
            self.delete()
            self.result.insert(0.0,"O has won")
            self.clear()
        elif (self.c==2 and self.e==2 and self.g==2 ):
            self.delete()
            self.result.insert(0.0,"O has won")
            self.clear()
        elif (self.d==2 and self.e==2 and self.f==2 ):
            self.delete()
            self.result.insert(0.0,"O has won")
            self.clear()
        elif (self.g==2 and self.h==2 and self.i==2 ):
            self.delete()
            self.result.insert(0.0,"O has won")
            self.clear()
        elif (self.c==2 and self.f==2 and self.i==2):
            self.delete()
            self.result.insert(0.0,"O has won")
            self.clear()
        elif (self.b==2 and self.e==2 and self.h==2):
            self.delete()
            self.result.insert(0.0,"O has won")
            self.clear()
        elif self.button_clicks>=9 :
            self.delete()
            self.result.insert(0.0,"its a tie ... please play again")
            self.clear()

    def delete(self):
        self.result.delete(0.0,END)

    def clear(self):
        self.button1["text"]=""
        self.button2["text"]=""
        self.button3["text"]=""
        self.button4["text"]=""
        self.button5["text"]=""
        self.button6["text"]=""
        self.button7["text"]=""
        self.button8["text"]=""
        self.button9["text"]=""
        self.button_clicks=0
        self.a=0
        self.b=0
        self.c=0
        self.d=0
        self.e=0
        self.f=0
        self.g=0
        self.h=0
        self.i=0



root = Tk()
root.title("Hello World")
root.geometry("600x600")

Application(root)
root.mainloop()
