from tkinter import *

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.grid()
        self.op1=0
        self.op2=0
        self.oper=" "
        self.counter=0
        self.create_widgets()
        self.ans=0
        self.memory=0

        
    def operate(self):
        
        if self.oper=="+":
            self.ans=self.op1+self.op2
            self.result.insert(0.0,str(self.op1)+str(self.oper)+str(self.op2)+"="+str(self.ans))
            
        
        elif self.oper=="-":
            self.ans=self.op1-self.op2
            self.result.insert(0.0,str(self.op1)+str(self.oper)+str(self.op2)+"="+str(self.ans))
            
            
        elif self.oper=="*":
            self.ans=self.op1*self.op2
            self.result.insert(0.0,str(self.op1)+str(self.oper)+str(self.op2)+"="+str(self.ans))
            
            
        elif self.oper=="/":
            self.ans=self.op1/self.op2
            self.result.insert(0.0,str(self.op1)+str(self.oper)+str(self.op2)+"="+str(self.ans))
            
    
    def create_widgets(self):
        self.result=Text(self,height=2,width=30,wrap=WORD)
        self.result.grid(row=0,column=1,columnspan=5)
        
        self.button7=Button(self,text="7",command=self.update_count7)
        self.button7.grid(row=1,column=1)
        
        self.button8=Button(self,text="8",command=self.update_count8)
        self.button8.grid(row=1,column=2)
        
        self.button9=Button(self,text="9",command=self.update_count9)
        self.button9.grid(row=1,column=3)
        
        self.button0=Button(self,text="0",command=self.update_count0)
        self.button0.grid(row=1,column=4)
        
        self.buttondiv=Button(self,text="/",command=self.update_count_div)
        self.buttondiv.grid(row=1,column=5)
        
        self.button4=Button(self,text="4",command=self.update_count4)
        self.button4.grid(row=2,column=1)
        
        self.button5=Button(self,text="5",command=self.update_count5)
        self.button5.grid(row=2,column=2)
        
        self.button6=Button(self,text="6",command=self.update_count6)
        self.button6.grid(row=2,column=3)
        
        self.buttonplus=Button(self,text="+",command=self.update_count_plus)
        self.buttonplus.grid(row=2,column=4)
        
        self.buttonmul=Button(self,text="*",command=self.update_count_mul)
        self.buttonmul.grid(row=2,column=5)
        
        self.button1=Button(self,text="1",command=self.update_count1)
        self.button1.grid(row=3,column=1)
        
        self.button2=Button(self,text="2",command=self.update_count2)
        self.button2.grid(row=3,column=2)
        
        self.button3=Button(self,text="3",command=self.update_count3)
        self.button3.grid(row=3,column=3)
        
        self.buttonmin=Button(self,text="-",command=self.update_count_min)
        self.buttonmin.grid(row=3,column=4)
        
        self.buttoneq=Button(self,text="=",command=self.update_count_eq)
        self.buttoneq.grid(row=3,column=5)

        self.buttonM_plus=Button(self,text="M+",command=self.M_plus).grid(row=4,column=1)

        self.buttonM_minus=Button(self,text="M-",command=self.M_minus).grid(row=4,column=2)

        self.M_clear=Button(self,text="MC",command=self.M_clear).grid(row=4,column=3)

        self.M_read=Button(self,text="MR",command=self.M_read).grid(row=4,column=4)
        
        self.buttonclear=Button(self,text="Clear",command=self.clr_in).grid(row=5,column=2)
        
        self.buttonback=Button(self,text="Back", command=self.go_back).grid(row=5,column=3)
        
        
    def update_count0(self):
        if self.oper==' ':
            self.op1=self.op1*10+0
            self.delete()  
            self.result.insert(END,self.op1)
        else:
            self.op2=self.op2*10+0
            self.delete()  
            self.result.insert(END,self.op2)
        
    def update_count1(self):
        if self.oper==' ':
            self.op1=self.op1*10+1
            self.delete()  
            self.result.insert(END,self.op1)
        else:
            self.op2=self.op2*10+1
            self.delete()  
            self.result.insert(END,self.op2)
        
    def update_count2(self):
        if self.oper==' ':
            self.op1=self.op1*10+2
            self.delete()  
            self.result.insert(END,self.op1)
        else:
            self.op2=self.op2*10+2
            self.delete()  
            self.result.insert(END,self.op2)
    
    def update_count3(self):
        if self.oper==' ':
            self.op1=self.op1*10+3
            self.delete()  
            self.result.insert(END,self.op1)
        else:
            self.op2=self.op2*10+3
            self.delete()  
            self.result.insert(END,self.op2)
        
    def update_count4(self):
        if self.oper==' ':
            self.op1=self.op1*10+4
            self.delete()  
            self.result.insert(END,self.op1)
        else:
            self.op2=self.op2*10+4
            self.delete()  
            self.result.insert(END,self.op2)
        
    def update_count5(self):
        if self.oper==' ':
            self.op1=self.op1*10+5
            self.delete()  
            self.result.insert(END,self.op1)
        else:
            self.op2=self.op2*10+5
            self.delete()  
            self.result.insert(END,self.op2)
    
    def update_count6(self):
        if self.oper==' ':
            self.op1=self.op1*10+6
            self.delete()  
            self.result.insert(END,self.op1)
        else:
            self.op2=self.op2*10+6
            self.delete()  
            self.result.insert(END,self.op2)
    
    def update_count7(self):
        if self.oper==' ':
            self.op1=self.op1*10+7
            self.delete()  
            self.result.insert(END,self.op1)
        else:
            self.op2=self.op2*10+7
            self.delete()  
            self.result.insert(END,self.op2)
            
    def update_count8(self):
        if self.oper==' ':
            self.op1=self.op1*10+8
            self.delete()  
            self.result.insert(END,self.op1)
        else:
            self.op2=self.op2*10+8
            self.delete() 
            self.result.insert(END,self.op2)
    
    def update_count9(self):
        if self.oper==' ':
            self.op1=self.op1*10+9
            self.delete()  
            self.result.insert(END,self.op1)
        else:
            self.op2=self.op2*10+9
            self.delete()  
            self.result.insert(END,self.op2)
        
    def update_count_plus(self):
        self.result.insert(END,"+")
        self.oper="+"
        
    def update_count_min(self):
        self.result.insert(END,"-")
        self.oper="-"
        
    def update_count_mul(self):
        self.result.insert(END,"*")    
        self.oper="*"
        
    def update_count_div(self):
        self.result.insert(END,"/")
        self.oper="/" 
        
    def update_count_eq(self):
        self.result.insert(END,"=")
        self.delete() 
        self.operate()
        self.oper='='
    
    def go_back(self):
        if self.oper==' ':
            self.op1=int(self.op1/10)
            self.delete()
            self.result.insert(END,self.op1)
        else:
            self.op2=int(self.op2/10)
            self.delete()
            self.result.insert(END,self.op2)
                    
    def clr_in(self):
        self.clear()

    def M_plus(self):
        if self.oper==' ':
            self.memory=self.op1+self.memory
        elif self.oper=='=':
            self.memory=self.ans+self.memory
        else:
            self.memory=self.op2+self.memory
        self.delete()
        self.result.insert(END,self.memory)

    def M_minus(self):
        if self.oper==' ':
            self.memory=self.op1-self.memory
        elif self.oper=='=':
            self.memory=self.ans-self.memory
        else:
            self.memory=self.op2-self.memory
        self.delete()
        self.result.insert(END,self.memory)

    def M_read(self):
        if self.oper==' ':
            self.memory=self.op1
        elif self.oper=='=':
            self.memory=self.ans
        else:
            self.memory=self.op2

        self.delete()
        self.result.insert(END,self.memory)

    def M_clear(self):
        self.memory=0
        self.delete()
        self.result.insert(END,self.memory)

    def delete(self):
        self.result.delete(0.0,END)

    def clear(self):
        self.counter=0
        self.op1=0
        self.op2=0
        self.oper=" "
        self.ans=0
        self.delete()

root=Tk()
root.title("CALCULATOR")
root.geometry("300x300")
Application(root)
root.mainloop()