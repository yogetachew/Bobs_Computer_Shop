"""
    Name: Bobs_computers_class.py
    Author: Aidan Newberry
    Created: 10/11/2023
    Purpose: Use @property Pythoic way of accessing attrabutes
"""
import bobs_computers_app
import bobs_computers_Menu
import bobs_disasters_class

class Computer:
    # the Computer init makes a bunch of dictionaries that hold the information used to sell parts.
    def __init__(self):
        self.CaseColors = {
            "Black":100,
            "White":115,
            "Red":120
        }

        self.CPUVendors = ["AMD", "Intel"]

        self.Motherboards = {
            "Non-Wifi":120,
            "Wifi":145
        }

        self.cpuOptions = {
            "4-Core":100,
            "8-Core":200,
            "16-Core":500
        }

        self.cpuCoolerOptions = {
            "Stock Cooler":0,
            "Air Cooler": 50,
            "AiO":150,
            "Custom Liquid Loop":500
        }

        self.gpuOptions = {
            "GTX 1650":150,
            "GTX 1080":250,
            "RTX 2070 SUPER":500,
            "RTX 3080":900,
            "RTX 4090ti":2000
        }

        self.storageoptions = {
            "HDD 1TB": 50,
            "HDD 2TB": 80,
            "SSD 256GB": 70,
            "SSD 512GB": 120,
            "SSD 1TB": 220,
        }

        self.memoryoptions = {
            "8GB": 50,
            "16GB": 100,
            "32GB": 200,
            "64GB": 350,
        }

        #makes global object variables or accessing different modules
        self.inputValidadator = bobs_computers_app.inputValidation()
        self.menuPrinter = bobs_computers_Menu

        #Initialize a Items gotten list which will be used to store the parts for the computer
        self.ItemsGottenList = []
    
    """Define getter with @property decorator"""
    @property
    def quantity(self):
        return self._quantity
    
    """Define setter with @property.setter decorator"""
    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity

    #this mmethod literally just prints the title
    @staticmethod
    def title():
        print(" _____                          _____  ")
        print("|\____\    ________________    |\____\ ")
        print("| | o |   | Bob's Computer |   | | o | ")
        print("| | o |   |      Shop      |   | | o | ")
        print("| | o |   |________________|   | | o | ")
        print("\ |___|           /|\          \ |___| ")

#ComputerCase (Probbly jsut let the choose the color to make it simpler)
    def ComputerCaseMenu(self) -> int:
        """Each of the menu functions are set up the same, there is some variance for disasters but they always go like this:
            Print prompt,
            make a variable that stores the prompt the menu item is asking for such as: "Enter name of the color that tickles your fancy: "
            make a variable that stores the prompt for an incorrect choice
            make a self.(something) var in the init class to define the choices the user has to pick from.
            Use the menuMaker method to format and print the menu, it also handles error exceptions and askes again.
            Use the Disaster class to account for disasters if any can happen
            append the item user chose from the menu maker to the Items gotten list
            return the price of the item user choose.
        """
        print("\nWhen making building a computer you can choose the color of the case. Here are your options to choose from: ")

        inputprompt = "Enter name of the color that tickles your fancy: "
        errormessage = "That input wasnt a case color we have in stock! \ntry again:"

        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(self.CaseColors, inputprompt, errormessage)

        #disaster
        tempreceptitem, output = bobs_disasters_class.Disasters.ShipIncorrectColor(self, self.CaseColors, tempreceptitem)

        self.ItemsGottenList.append(tempreceptitem)

        return output

#MotherboardType (Maby just let the choose if they want wifi or not at a $30 dollar discount if they dont to make it simpler)
    def MotherboardTypeMenu(self) -> int:
        """Each of the menu functions are set up the same, there is some variance for disasters but they always go like this:
            Print prompt,
            make a variable that stores the prompt the menu item is asking for such as: "Enter name of the color that tickles your fancy: "
            make a variable that stores the prompt for an incorrect choice
            make a self.(something) var in the init class to define the choices the user has to pick from.
            Use the menuMaker method to format and print the menu, it also handles error exceptions and askes again.
            Use the Disaster class to account for disasters if any can happen
            append the item user chose from the menu maker to the Items gotten list
            return the price of the item user choose.
        """

        print("Additionally You can pick whether or not you need your motherboard to support wifi. Here are your options to choose from: ")

        inputprompt = "Enter name of the motherboard that tickles your fancy: "
        errormessage = "That input wasnt a Motherboard we have in stock! \ntry again:"
        
        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(self.Motherboards, inputprompt, errormessage)

        self.ItemsGottenList.append(tempreceptitem)

        return output

#CPU(could do a specific SKU or just simplify and calculate cost baised on per core basis)
    def cpuTypeMenu(self) -> int:
        """Each of the menu functions are set up the same, there is some variance for disasters but they always go like this:
            Print prompt,
            make a variable that stores the prompt the menu item is asking for such as: "Enter name of the color that tickles your fancy: "
            make a variable that stores the prompt for an incorrect choice
            make a self.(something) var in the init class to define the choices the user has to pick from.
            Use the menuMaker method to format and print the menu, it also handles error exceptions and askes again.
            Use the Disaster class to account for disasters if any can happen
            append the item user chose from the menu maker to the Items gotten list
            return the price of the item user choose.
        """

        print("Here are the options for your CPU: ")

        inputprompt = "Enter the CPU you want: "
        errormessage = "That input is not a cpu we have in stock! \nTry again: "

        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(self.cpuOptions, inputprompt, errormessage)

        self.ItemsGottenList.append(tempreceptitem)

        return output

#CPUVendor, give the user the illusion of choice when picking a cpu/motherboard, if they pick AMD they will get an AMD CPU
    
    def CPUVendor(self) -> str:
        """This function is just a very complicated way to ask if the user prefers one CPU vendor over the other.
        It only returns "AMD" or "Intel" Because those are the only brands we sell
        """

        print("When choosing a motherboard it is crucial for us to know what Vendor of CPU you will be using. Here are you options of vendors we carry: ")

        inputprompt = "Enter number of the Vendor you like best, if you dont know just choose the color you like best. Intel is blue, AMD is red: "
        errormessage = "That input wasnt a CPU vendor we carry! \ntry again:"

        for i in range(len(self.CPUVendors)):
            print(f"[{i+1}]: {self.CPUVendors[i]}")

        while True:
            cpuBrand = int(self.inputValidadator.validateNumRange(inputprompt,[1,len(self.CPUVendors)]))

            if cpuBrand == 1 or cpuBrand == 2:
                
                if cpuBrand == 1:
                    self.ItemsGottenList[1][0] = f"AMD {self.ItemsGottenList[1][0]}"
                    self.ItemsGottenList[2][0] = f"AMD {self.ItemsGottenList[2][0]}"
                elif cpuBrand ==2:
                    self.ItemsGottenList[1][0] = f"Intel {self.ItemsGottenList[1][0]}"
                    self.ItemsGottenList[2][0] = f"Intel {self.ItemsGottenList[2][0]}"

                return self.CPUVendors[cpuBrand-1]

#CPU COOLER
    def cpuCoolerMenu(self) -> int:
        """Each of the menu functions are set up the same, there is some variance for disasters but they always go like this:
            Print prompt,
            make a variable that stores the prompt the menu item is asking for such as: "Enter name of the color that tickles your fancy: "
            make a variable that stores the prompt for an incorrect choice
            make a self.(something) var in the init class to define the choices the user has to pick from.
            Use the menuMaker method to format and print the menu, it also handles error exceptions and askes again.
            Use the Disaster class to account for disasters if any can happen
            append the item user chose from the menu maker to the Items gotten list
            return the price of the item user choose.
        """

        print("Pick which CPU cooler you want from the options below: ")

        inputprompt = "Enter the CPU cooler you want: "
        errormessage = "That input is not a cooler we have available"

        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(self.cpuCoolerOptions, inputprompt, errormessage)

        self.ItemsGottenList.append(tempreceptitem)

        return output


#GPU(Could do a specific SKU or just simplify and calculate cost baised on ram they want/need)
    def gpuTypeMenu(self) -> int:
        """Each of the menu functions are set up the same, there is some variance for disasters but they always go like this:
            Print prompt,
            make a variable that stores the prompt the menu item is asking for such as: "Enter name of the color that tickles your fancy: "
            make a variable that stores the prompt for an incorrect choice
            make a self.(something) var in the init class to define the choices the user has to pick from.
            Use the menuMaker method to format and print the menu, it also handles error exceptions and askes again.
            Use the Disaster class to account for disasters if any can happen
            append the item user chose from the menu maker to the Items gotten list
            return the price of the item user choose.
        """

        print("Here are the options for your GPU: ")

        inputprompt = "Enter the name of the GPU you want: "
        errormessage = "That input is not a GPU we have in stock! \nTry again: "

        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(self.gpuOptions, inputprompt, errormessage)

        self.ItemsGottenList.append(tempreceptitem)

        return output

#StorageType(the user can choose what type of storage they want)
    def storageTypeMenu(self) -> int:
        """Each of the menu functions are set up the same, there is some variance for disasters but they always go like this:
            Print prompt,
            make a variable that stores the prompt the menu item is asking for such as: "Enter name of the color that tickles your fancy: "
            make a variable that stores the prompt for an incorrect choice
            make a self.(something) var in the init class to define the choices the user has to pick from.
            Use the menuMaker method to format and print the menu, it also handles error exceptions and askes again.
            Use the Disaster class to account for disasters if any can happen
            append the item user chose from the menu maker to the Items gotten list
            return the price of the item user choose.
        """

        print("Here are the options for your storage: ")

        inputprompt = "Enter the type of storage you want: "
        errormessage = "That input is not a storagr type we have in stock! \nTry again: "

        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(self.storageoptions, inputprompt, errormessage)

        self.ItemsGottenList.append(tempreceptitem)

        return output

#memoryoption(the user can choose what type of memory they want)
    def memoryoptionMenu(self) -> int:
        """Each of the menu functions are set up the same, there is some variance for disasters but they always go like this:
            Print prompt,
            make a variable that stores the prompt the menu item is asking for such as: "Enter name of the color that tickles your fancy: "
            make a variable that stores the prompt for an incorrect choice
            make a self.(something) var in the init class to define the choices the user has to pick from.
            Use the menuMaker method to format and print the menu, it also handles error exceptions and askes again.
            Use the Disaster class to account for disasters if any can happen
            append the item user chose from the menu maker to the Items gotten list
            return the price of the item user choose.
        """

        print("Here are the options for your memory: ")

        inputprompt = "Enter the type of memory you want: "
        errormessage = "That input is not a memory type we have in stock! \nTry again: "
        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(self.memoryoptions, inputprompt, errormessage)

        self.ItemsGottenList.append(tempreceptitem)

        return output

    def printlist(self):
        print(self.ItemsGottenList)


#----------------------------
#accessories start here

    """For each of the accessory functions all that is needed is to ask a yes or no question and add the result to the items gotten list, 
    these are all the same in from and return just the price of the choice the user choose
    """
    def RGBLightsMenu(self) -> int:
        rgb = self.inputValidadator.validateYorN("Do you want $40 worth of RGB leds installed inside your case? Y/N: ").lower()
        if rgb == "y":
            self.ItemsGottenList.append(["RGB",40])
            return 40
        else:
            return 0
        
    def preinstallWindows(self) -> int:
        windows = self.inputValidadator.validateYorN("Do you want your PC to come with Windows 11 Preinstalled? (-$100 if no) Y/N: ").lower()
        if windows == "y":
            return 0
        else: 
            self.ItemsGottenList.append(["no windows", -100])
            return 100
        
    def warranty(self, currenttotal) -> int:
        warranty = self.inputValidadator.validateYorN(f"Do you want to purchase warranty for your computer?\nIt is 10% of the total cost of the system  Y/N: ").lower()
        if warranty == "n":
            return 0
        else: 
            self.ItemsGottenList.append(["Warranty", .10*currenttotal])
            return .10*currenttotal

    def shipping(self) -> int:
        premium_shipping = self.inputValidadator.validateYorN(f"Do you wish to purchase the premium shipping plan?\nIt is $10 per each pc ordered [Y/N]: ").lower()
        if premium_shipping == "n":
            return 0
        else:
            self.ItemsGottenList.append(["Premium Shipping", 10 * self.quantity])
            return 10*self.quantity
