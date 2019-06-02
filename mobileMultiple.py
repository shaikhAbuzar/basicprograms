class Mobile:
    ram=0
    storage=0
    os=''

class Samsung(Mobile):
    ui=''
    def getSamsung(self,useri,oprsys):
        self.ui=useri
        self.os=oprsys

class Nokia(Mobile):
    ui=''
    def getNokia(self,useri,oprsys):
        self.ui=useri
        self.os=oprsys

class GalaxyS5(Samsung):
    name=''
    def getGalaxySpecs(self,ram,storage,name):
        self.ram=ram
        self.storage=storage
        self.name=name

    def displayGalaxySpecs(self):
        print('Name:',self.name)
        print('Ram:',self.ram,'GB')
        print('Storage:',self.storage,'GB')
        print('OS:',self.os)
        print('UI:',self.ui)

class Lumia625(Nokia):
    name=''
    def getLumiaSpecs(self,ram,storage,name):
        self.ram=ram
        self.storage=storage
        self.name=name

    def displayLumiaSpecs(self):
        print('Name:',self.name)
        print('Ram:',self.ram,'GB')
        print('Storage:',self.storage,'GB')
        print('OS:',self.os)
        print('UI:',self.ui)

s = GalaxyS5()
n = Lumia625()
print('======SAMSUNG======')
s.getSamsung('OneUI','Android')
s.getGalaxySpecs(4,32,'Galaxy S5')
s.displayGalaxySpecs()
print('\n======NOKIA======')
n.getNokia('Windows','Windows10')
n.getLumiaSpecs(3,64,'Lumia 625')
n.displayLumiaSpecs()