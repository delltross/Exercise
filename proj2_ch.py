"""
File: proj2_ch.py
Author: Ken Greenberg
Section: 01
Email: kgreen7@umbc.edu
Date: 09/30/2019
Description: In this file, a store with two registers is simulated. The store
 and the registers are objects, that at the beginning of the program, are unlocked
 and the user may input values for the bill count for each denomination in the
 registers. The user has several options to perform various actions on the
 registers, involving moving and adding money to the registers, as well as
 closing down the store. The user may continue inputting actions for the
 registers until they decide to close the shop.
 File Preconditions:
"""
import cashRegister, store

MIN = 0
STORE = 's'
CLOSE = 'c'
LOCK = 'l'
UNLOCK = 'u'
DISPLAY = 'd'
TRANSFER = 't'
REMOVE = 'r'
ADD = 'a'
###############################################################################
#displayMenu() Prints a string list of options that the user can perform on 
#registers.
#Input:        None
#Output:       None
def displayMenu():
    print("A - Add money \n R - Remove money \n T - Transfer money \n \
L - Lock register \n U - Unlock register \n D - Display register state \n \
S - Display store state \n C - Close the store and quit")


###############################################################################
# validateNum() Checks user input of integers by checking if they are postive,
#               and if the user is entering a register number, the function
#               checks if it is a valid register number.
# Input:        prompt: string asking the user what their input is.
#               register: a Boolean value telling the function if the user is
#               entering a register number.
# Output:       number: an integer value
# Preconditions: The user must enter an integer.
def validateNum(prompt, register):
    number = int(input(prompt))
    if register == True:
        while number <= MIN or number > 2:
            print("You must select register 1 or register 2.")
            number = int(input(prompt))

    while number < MIN:
        print("The number of bills must be >= 0.")
        number = int(input(prompt))
    
    return number


##############################################################################
# validateLetter() Checks the user input to confirm it is a valid option by
#                  checking it against a list of possible one-letter strings.
# Input:           prompt: a string that asks the user what action they want to 
#                          perform.
# Output:          letter: a one-letter string.
# Preconditions:   The user must enter a string.
def validateLetter(prompt):
    letters = ['a', 'r', 't', 'l', 'u', 's', 'c']
    letter = (input(prompt)).lower()
    #letter = letter.lower()
    while letter not in letters:
        print("That is not a valid option. Try again")
        letter = (input(prompt)).lower()
        #letter = letter.lower()

    return letter
    
    
###############################################################################
# createList(): User inputs the number of bills of each denomination that is in 
#              a register.
# Input:       number: an integer corresponding to one of two registers.
# Output:      bills: a list of integers corresponding to the number of bills
#                     for each denomination.
# Preconditions: None
def createList(number):
    bills = []
    print("What's in register #", str(number), "?")
    
    ones = validateNum("\tOnes: ", False)
    bills.append(ones)
    
    fives = validateNum("\tFives: ", False)
    bills.append(fives)
    
    tens = validateNum("\tTens: ", False)
    bills.append(tens)
    
    twenties = validateNum("\tTwenties: ", False)
    bills.append(twenties)
    
    return bills
    
    
###############################################################################
# closeShop(): Sets the store object to closed and each register to locked when
#              user wants to quit the program.
# Input:       None
# Output:      None
# Preconditions: None
def closeShop():
    store1.CloseShop()
    register1.lockOn()
    register2.lockOn()
    register1.displayState(1)
    register2.displayState(2)


###############################################################################
# toggleLock(): Changes the attribute of one register to locked or unlocked.
# Input:        action: a string that is created when the user chooses in main.
# Output:       None
# Preconditions: None
def toggleLock(action):
    prompt = ("Enter register number: ")
    choice = validateNum(prompt, True)
    if action == LOCK:
        if choice == 1:
            register1.lockOn()
        elif choice == 2:
            register2.lockOn()
            
    elif action == UNLOCK:
        if choice == 1:
            register1.lockOff()
        elif choice == 2:
            register2.lockOff()


###############################################################################
if __name__ == '__main__':
    store1 = store.Store() #create the store1 object
    store1.OpenShop() #set the store attribute to open
    
    print("The store is now open. Initializing the registers...")
    register1 = cashRegister.CashRegister() #create both register objects
    register2 = cashRegister.CashRegister()
    
    register1.lockOff() #unlock both registers
    register2.lockOff()
    
    #initialize lists, will be turned into list of the number of each bills, in 
    #order ones, fives, tens, twenties
    bills1 = [] 
    bills2 = []
    
    #user inputs initial values for each register, and method createList places 
    #them in bills1 and bills2
    bills1 = createList(1) 
    bills2 = createList(2)
    
    #sets the attribute bills for each register as the lists created in main
    register1.setBills(bills1, "") 
    register2.setBills(bills2, "")
    
    #create two dictionaries that pair the integer values 1 and 2 to the
    #register objects of the same number, as well as the corresponding bill 
    #lists. User will input integer values when prompted for which register they
    #wish to manipulate
    registers = {1:register1, 2:register2}
    bills = {1:bills1, 2:bills2}
    
    print("Register 1")
    register1.displayState(1)
    print("\n")
    print("Register 2")
    register2.displayState(2)
    
    while store1.open == True:
        displayMenu()
        prompt = "What do you want to do? Type the corresponding letter: "
        action = validateLetter(prompt)
        
        if action == CLOSE: #close the store and set each register to locked
            closeShop()
            
        elif action == LOCK: #lock a register
            toggleLock(LOCK)
                
        elif action == UNLOCK: #unlock a register
            toggleLock(UNLOCK)
                
        elif action == DISPLAY: #show all the attributes of both registers
            register1.displayState(1)
            print()
            register2.displayState(2)
            
        elif action == STORE: #display state of store
            store1.displayState()
            
        elif action == REMOVE: #remove money from a register
            prompt = ("Enter register number: ")
            num = validateNum(prompt, True)
            
            if num in registers.keys():
                old_total = registers[num].total #keep a copy of old total
                new_bills = createList(num) #ask for new bill amounts
                registers[num].setBills(new_bills, 'remove') #set register to new bills
                new_total = registers[num].total #calculated by change method
                difference = old_total - new_total
                print("Total amount removed: ", difference)
           
        elif action == ADD: #add money to a register
            prompt = ("Enter register number: ")
            num = validateNum(prompt, True)
            if num in registers.keys():
                old_total = register1.total #keep a copy of old total
                new_bills = createList(1) #ask for new bill amounts
                register1.setBills(new_bills, 'add') #set register to new bills
                new_total = registers[num].total #calculated by change method
                difference =  new_total - old_total
                print("Total amount added: ", difference)
                
        elif action == TRANSFER: #move money from one register to another
            prompt("Enter which register you want to transfer from: ")
            num = validateNum(prompt, True)
            #ask the user for which register they want to take money from, then
            #the other register is set to num2
            if num == 1:
                num2 = 2
            else:
                num2 = 1
            
            if num in registers.keys():
                old_total = registers[num].total #record old total
                new_bills = createList(num) #ask user for new bills totals
                transfer = []

                """
                create a list 'transfer' of the changes to each denomination. 
                To the bills list being added to, add each number from transfer
                to the appropriate denomination. For the list being removed
                from, subtract the same amount. The new totals are
                re-calculated, and the difference is displayed.
                """
            for d in range(len(bills[num])):
                    transfer.append(new_bills[d] - bills[num][d])
                    bills[num][d] - transfer[d]
                    bills[num2][d] += transfer[d]
                new_total = registers[num].total
                transfer_amount = old_total - new_total
                print("Amount transfer: ", transfer_amount)