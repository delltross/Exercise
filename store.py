#File: store.py
#Author: Ken Greenberg
#Date: 09/29/2019
#Section: 01
#Email: kgreen7@umbc.edu
#Description: A class of objects that represents a store that can be opened and
#closed. Used in the proj2.py file to represent when the registers can be
#manipulated. When the file starts, a store object is created and set to open.
class Store:
    def __init__(self):
        self.open = False
        self.door = "Locked"
        self.lights = "Off"
        self.sign = "Closed"
        
    def OpenShop(self):
        self.open = True
        self.door = "Unlocked"
        self.sign = "Open"
        self.lights = "On"
        
    def CloseShop(self):
        self.open = False
        self.door = "Locked"
        self.lights = "Off"
        self.sign = "Closed"
        
    def displayState(self):
        print("Doors: ", self.door)
        print("Lights: ", self.lights)
        print("Sign says: ", self.sign)


if __name__ == '__main__':
    store1 = Store()
    store1.OpenShop()
    while store1.open == True:
        print("The store is open for business")
        store1.open = False
        print("Store is now closed.")