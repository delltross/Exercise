"""
File: cashRegister.py
Author: Ken Greenberg
Date: 09/30/2019
Section: 01
Email: kgreen7@umbc.edu
Description: This file contains a class called CashRegister. This class has an 
three attributes: total, bills, and locked. Bills is a list of 4 integer values
that correspond to 4 denominations of dollars. Locked is a boolean value that 
when set to True, prevents any changes being made to bills or total. Total is a
value calculated from the denomination amounts in bills.
"""

class CashRegister:
    
    def __init__(self):
        self.__locked = True
        self.__bills = [0,0,0,0]
        self.__total = 0
        
#accessors
        
    def displayState(self, number):
        print("Register", number, ":")
        print("Lock status: ", end="")
        if self.__locked == True:
            print("Locked")
        else:
            print("Unlocked")
        print("Total $ amount: ", self.total)
        print("Ones: ", self.bills[0])
        print('Fives: ', self.bills[1])
        print('Tens: ', self.bills[2])
        print('Twenties: ', self.bills[3])
        
#mutators
    def lockOn(self):
        self.__locked = True
        
    def lockOff(self):
        self.__locked = False
        
    def calcTotal(self):
        self.__total = self.bills[0] + 5*self.bills[1] +\
        10*self.bills[2] + 20*self.bills[3]
    
    #a new list of values replaces the old one by iterating over the new list
    #and replacing the values in the old list
    def setBills(self, new, operation):
        if self.__locked == True: #error if register is locked
            print("Can't do that. Register is locked.")
        else:    
            for d in range(len(self.bills)):
                change = self.bills[d] - new[d] #if change is negative, two 
                #operations will not be performed
                if change < 0 and (operation == "remove" or operation == "transfer"):
                    print("Cannot transfer more bills than are in the register.")
                elif change > 0 and operation == "add":
                    print("Cannot add a negative number of bills.")
                else:
                    #assign the new values to the attribute bills
                    self.bills[d] = new[d]
        #re-calculate the total amount of money in the register
        self.calcTotal()
        
        
if __name__ == '__main__':
    registers = {}
    
    cash1 = CashRegister()
    cash1.displayState(1)
    registers[1] = cash1
    
    test_list = [1, 2, 3, 4]
    
    cash1.setBills(test_list, "")
    cash1.displayState(1)
    
    cash1.lockOff()
    cash1.setBills(test_list, "")
    cash1.displayState(1)
    
    newList = [4,5,6,7]
    cash1.setBills(newList, "")
    cash1.displayState(1)