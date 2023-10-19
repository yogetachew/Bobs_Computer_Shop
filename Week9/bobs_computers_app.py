"""
  Name: bobs_computers_app.py
  Created: 10/11/23
  Purpose: Main application file for menu and accessing objects
"""

# TODO: import class file
import Bobs_computers_class

# TODO: create main
def main():
    # Create computer object
    computer = Bobs_computers_class.Computer()
    # Call menu function, pass reference to computer object
    menu(computer)

# TODO: create menu function
def menu(computer):
    while True:
        # Get number of computers from user
        # set quantity to object
        computer.quantity = (int(input(" How many computers: ")))

        runningtotal = 0

        runningtotal += computer.ComputerCaseMenu()

        runningtotal += computer.MotherboardTypeMenu()

        # Get computer quantity from object
        quantity = computer.quantity
        print(f" You ordered {quantity} computers, ='ing ${runningtotal}")



if __name__ == "__main__":
    main()