# parking garage
import os
clear = lambda: os.system('cls')
from time import sleep
clear()
license_plate = input("What is your license plate?\n\n")
has_ticket = {}
has_ticket[license_plate] = False

class ParkingGarage(): # Jordan - Made class
    def __init__(self, l_plate, all_tickets = 50, parking_spaces = 50, currentTicket = {}):
        self.all_tickets = all_tickets
        self.parking_spaces = parking_spaces
        self.currentTicket = currentTicket
        self.l_plate = l_plate

    def takeTicket(self): # Jordan - Made takeTicket method
        clear()
        if self.all_tickets and self.parking_spaces != 0:
            self.all_tickets - 1
            self.parking_spaces - 1
            self.currentTicket[self.l_plate] = False
            has_ticket[self.l_plate] = True
            print(f"You took a ticket.\n")
            sleep(3)
        else :
            print("The parking garage is full.")
            sleep(3)

    def payForParking(self, amount): # Tapiwa - Created the pay for parking method
        clear()
        self.currentTicket[self.l_plate] = True
        print(f"You paid ${amount} for parking.")
        sleep(3)

    def leavegarage(self): # Andy - created leave garage
        clear()
        print("Thank you, have a nice day!")
        self.all_tickets + 1
        self.parking_spaces + 1
        del self.currentTicket[self.l_plate]

    def isPaid(self):
        if self.currentTicket[self.l_plate]:
            return True
        else:
            return False


parking_garage = ParkingGarage(license_plate)

p_data = parking_garage.__dict__

while True:
    clear()
    if has_ticket[license_plate]: # Jordan - Added check for paid ticket
        res = input("What would you like to do?\n\nPay - Pay for your parking\nLeave - Leave the garage\n\n")
    else:
        res = input("What would you like to do?\n\nPark - Take a ticket and find a spot\nPay - Pay for your parking\nLeave - Leave the garage\n\n").lower()
    if res == "park": # Jordan - Added park condition
        parking_garage.takeTicket()
    elif res== "pay":
        clear()
        has_paid = parking_garage.isPaid()
        if has_paid:
            print("You already paid for parking.")
            sleep(3)
        else:
            amount = input("How much are you paying for the ticket?\n\n") # Tapiwa created the conditional statements for the pay for parking method
            if amount != False and amount != " " and amount.isdigit():
                parking_garage.payForParking(amount)
            else:
                clear()
                print("Please input a valid digit amount")
                sleep(3)
    elif res == "leave":# Andy created leave condition
        clear()
        ticket_paid = parking_garage.isPaid() # check if paid
        if ticket_paid:
            parking_garage.leavegarage()
            has_ticket[license_plate] = False
            sleep(3)
            break
        else:
            clear()
            print("Seems like your ticket was not paid, please pay for the ticket\n")
            amount = input("How much are you paying for the ticket?\n\n")
            if amount != False and amount != " " and amount.isdigit():
                print(f"Your ticket has been paid for the amount of {amount}")
                parking_garage.leavegarage()
                sleep(3)
                break
            else:
                clear()
                print("Please input a valid digit amount")
                sleep(3)
    else:
        print(f"{res} is not a valid option.")
        sleep(3)




# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1


# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True

# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)