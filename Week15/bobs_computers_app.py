"""
  Name: bobs_computers_app.py
  Created: 10/11/23
  Purpose: Main application file for menu and accessing objects
"""

# TODO: import class file
import Bobs_computers_class
import bobs_computers_Business
import bobs_disasters_class

# Class for input validation
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
        # Validate user input as a number
        while True:        
            try:
                userinput = int(input(prompt))
                return userinput
            except:
                print("\nThat wasnt right! try again:")
            
    def validateYorN(self, prompt:str):
        # Validate user input as 'y' or 'n'
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
    # create disaster object
    disasters = bobs_disasters_class.Disasters()


    while True:

        # Display title
        computer.title()

        # Initialize running total
        runningtotal = 0

        # Menu for computer components
        runningtotal += computer.ComputerCaseMenu()

        runningtotal += computer.MotherboardTypeMenu()

        runningtotal += computer.cpuTypeMenu()

        CPUbrand = computer.CPUVendor()

        if CPUbrand == "AMD":
            CPUbrand = "AMD"
        else:
            CPUbrand = "Intel"

        runningtotal += computer.cpuCoolerMenu()

        runningtotal += computer.gpuTypeMenu()

        runningtotal += computer.storageTypeMenu()

        runningtotal += computer.memoryoptionMenu()

        # Prompt for extra accessories
        accessories = inputValidadator.validateYorN("\nThat concludes all the nessesary things when building a tower, do you want to add extra accessories (y/n): ").lower()
        # TODO: shipping and warrenty
        if accessories == "y":
            runningtotal += computer.RGBLightsMenu()
            runningtotal -= computer.preinstallWindows()
            print(f"current total: ${runningtotal}")
            warranty_cost = computer.warranty(runningtotal)
            if warranty_cost > 0:
                warranty = "y"
                runningtotal += warranty_cost
            else:
                warranty = "n"

         # print final bill
        print(f"\nYour final bill for your {CPUbrand} computer is ${runningtotal}.")

        #the recipt doesnt respect this number yet :)
        computer.quantity = (int(inputValidadator.validateNum("How many copies of this computer are you going to buy?: ")))
        # Get number of computers from user
        # set quantity to object

        # determine if user wants premium shipping or not
        shipping = computer.shipping()
        if shipping > 0:
            premium_shipping = "y"
        else: 
            premium_shipping = "n"

        # Get computer quantity from object
        quantity = computer.quantity

        print(f"\n You ordered {quantity} computer(s), costing ${runningtotal} each. plus shipping of ${shipping}")
        print(f" TOTAL COST: ${quantity * runningtotal + shipping}")


        # wrong order disaster
        print(disasters.WrongStorageOption(premium_shipping, warranty))


        # shipping disaster
        print(disasters.failedDelivery(premium_shipping, warranty))


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

    computer.printlist()

if __name__ == "__main__":
    main()