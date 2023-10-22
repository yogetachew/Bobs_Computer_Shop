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
    still_running = "y"
    while still_running =="y":
        # Get number of computers from user
        # set quantity to object
        computer.quantity = (int(input(" How many computers: ")))

        runningtotal = 0

        runningtotal += computer.ComputerCaseMenu()

        runningtotal += computer.MotherboardTypeMenu()

        runningtotal += computer.cpuTypeMenu()

        runningtotal += computer.gpuTypeMenu()

        # Get computer quantity from object
        quantity = computer.quantity
        print(f" You ordered {quantity} computers, costing ${runningtotal} each")
        print(f" TOTAL COST: {quantity * runningtotal}")

        # input to ask if user wants program to keep running
        still_running = input("Do you wish to run again? [Y/N]: ").lower




if __name__ == "__main__":
    main()