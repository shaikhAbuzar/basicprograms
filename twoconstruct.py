class name:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def show(self):
        print('Welcome',self.fname,self.lname)

n=name('Abuzar','Shaikh')
n.show()