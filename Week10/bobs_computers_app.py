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
    CPUbrand=""
    while True:
        runningtotal = 0

        runningtotal += computer.ComputerCaseMenu()

        CPUbrand = computer.CPUVendor()

        if CPUbrand == "AMD":
            CPUbrand = "AMD"
        else:
            CPUbrand = "Intel"

        runningtotal += computer.MotherboardTypeMenu()

        runningtotal += computer.cpuTypeMenu()

        runningtotal += computer.cpuCoolerMenu()

        runningtotal += computer.gpuTypeMenu()

        runningtotal += computer.storageTypeMenu()

        runningtotal += computer.memoryoptionMenu()

        accessories = input("\nThat concludes all the nessesary things when building a tower, do you want to add extra accessories (y/n): ")

        if accessories == "y" or accessories == "Y":
            runningtotal += computer.RGBLightsMenu()

        print(f"\nYour final bill for your {CPUbrand} computer is ${runningtotal}.")

        computer.quantity = (int(input("How many copies of this computer are you going to buy?: ")))
        # Get number of computers from user
        # set quantity to object

        # Get computer quantity from object
        quantity = computer.quantity
        print(f" You ordered {quantity} computer(s), costing ${runningtotal} each")
        print(f" TOTAL COST: ${quantity * runningtotal}")

        # input to ask if user wants program to keep running
        run_again = input("Do you wish to run again? [Y/N]: ").lower()
        if run_again != "y":
            break




if __name__ == "__main__":
    main()