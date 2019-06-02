class Truck:
    noOfContainers=0
    truckManufacture=''
    truckId=0      

class Car:
    noOfDoors=0  
    carManufacture=''
    carId=0
    def putCar(self):
        print('No. of doors for car:',self.noOfDoors)

class Bike:
    saddleHeight=0
    bikeManufacture=''
    bikeId=0
    def putBike(self):
        print('The saddle height of bike is:',self.saddleHeight,'inches')

class TransportationVehicle(Truck):
    loadCapacity = 0
    def getTransportVehicle(self, capacity,containers):
        self.loadCapacity = capacity
        self.noOfContainers = containers

    def putTransportVehicle(self):
        print('No. of Conatiners:',self.noOfContainers)
        print('Load Capacity of Vehicle is:',self.loadCapacity,'Tonns')

class PassengerVehicle(Car,Bike):
    noOfPassengers=0
    def getPassenger(self,passenger,doors,height):
        self.noOfPassengers = passenger
        self.noOfDoors = doors
        self.saddleHeight = height

    def putPassenger(self):
        print('Passenger Capacity is:',self.noOfPassengers)

class Vehicle(TransportationVehicle,PassengerVehicle):
    def getIdDetails(self,tId,cId,bId):
        self.truckId = tId
        self.carId = cId
        self.bikeId = bId

    def getmanufacturer(self,truck,car,bike):
        self.truckManufacture = truck
        self.carManufacture = car
        self.bikeManufacture = bike

    def putDetails(self):
        print('Truck Manufacturer is {} and ID is {}'.format(self.truckManufacture,self.truckId))
        print('Car Manufacturer is {} and ID is {}'.format(self.carManufacture,self.carId))
        print('Bike Manufacturer is {} and ID is {}'.format(self.bikeManufacture,self.bikeId))

v = Vehicle()
v.getIdDetails(123,321,231)
v.getPassenger(2,4,50)
v.getTransportVehicle(70,100)
v.getmanufacturer('Mahindra','Hyundai','Pulsar')
print('\n===========TRANSPORT VEHICLE===========')
v.putTransportVehicle()
print('=======================================')
print('\n===========PASSENGER VEHICLE===========')
v.putBike()
v.putCar()
v.putPassenger()
print('=======================================')
print('\n============GENREAL DETAILS============')
v.putDetails()
print('=======================================')