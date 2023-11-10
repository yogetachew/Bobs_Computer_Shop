"""
  Name: bobs_computers_app.py
  Created: 10/11/23
  Purpose: Main application file for menu and accessing objects
"""

# TODO: import class file
import Bobs_computers_class
import bobs_computers_Business

class inputValidation():
    def __init__(self):
        pass

    def validateList(self, prompt:str, ValidInputs:list):
        print(f"{prompt} and {ValidInputs}")
        while True:
            userinput = input(prompt)
            
            if userinput in ValidInputs:
                return userinput
            
    def validateNum(self, prompt:str):
        while True:        
            try:
                userinput = int(input(prompt))
                return userinput
            except:
                print("\nThat wasnt right! try again:")
            
    def validateYorN(self, prompt:str):
        while True:
            userinput = input(prompt)

            if userinput == "y" or userinput == "Y" or userinput == "n" or userinput == "N":
                return userinput
            
    def validateNumRange(self, prompt:str, range:list):
        """Validates a input if its a number and inside a range provided ex [0,23]"""
        while True:
            try:
                userinput = int(input(prompt))
                if userinput >= range[0] and userinput <= range[1]:
                    return userinput
            except:
                print("That wasnt right! try again:")
            
            


# TODO: create main
def main():
    # Create computer object
    computer = Bobs_computers_class.Computer()
    # Call menu function, pass reference to computer object
    menu(computer)

# TODO: create menu function
def menu(computer):
    CPUbrand=""
    inputValidadator = inputValidation()
    # Create business object
    business = bobs_computers_Business.Business()
    while True:

        computer.title()

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

        accessories = inputValidadator.validateYorN("\nThat concludes all the nessesary things when building a tower, do you want to add extra accessories (y/n): ").lower()

        if accessories == "y":
            runningtotal += computer.RGBLightsMenu()
            runningtotal -= computer.preinstallWindows()

        print(f"\nYour final bill for your {CPUbrand} computer is ${runningtotal}.")

        computer.quantity = (int(inputValidadator.validateNum("How many copies of this computer are you going to buy?: ")))
        # Get number of computers from user
        # set quantity to object

        # Get computer quantity from object
        quantity = computer.quantity
        print(f"\n You ordered {quantity} computer(s), costing ${runningtotal} each")
        print(f" TOTAL COST: ${quantity * runningtotal}")

        # track total sale in business class
        total_sale = quantity * runningtotal
        business.trackSales(total_sale)

        # return total sales FOR TESTING
        print(f" TOTAL SALES: ${business.returnSales()}")

        # track total costs
        business.trackCosts()
        # track total profit
        business.trackProfit()
        
        # input to ask if user wants program to keep running
        run_again = inputValidadator.validateYorN("Do you wish to run again? [Y/N]: ").lower()
        if run_again != "y":
            break
    
    print("hellow?")
    computer.printlist()

if __name__ == "__main__":
    main()