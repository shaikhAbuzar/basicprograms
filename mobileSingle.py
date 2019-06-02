class Mobile:
    ram=0
    storage=0
    os=''

class Samsung(Mobile):
    ui=''
    def getSamsung(self,useri,oprsys):
        self.ui=useri
        self.os=oprsys

class GalaxyS5(Samsung):
    def getSpecs(self,ram,storage):
        self.ram=ram
        self.storage=storage

    def displaySpecs(self):
        print('Ram:',self.ram,'GB')
        print('Storage:',self.storage,'GB')
        print('OS:',self.os)
        print('UI:',self.ui)

m = GalaxyS5()
m.getSamsung('OneUI','Android')
m.getSpecs(4,32)
m.displaySpecs()