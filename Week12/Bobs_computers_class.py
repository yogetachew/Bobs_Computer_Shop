"""
    Name: Bobs_computers_class.py
    Author: Aidan Newberry
    Created: 10/11/2023
    Purpose: Use @property Pythoic way of accessing attrabutes
"""
import bobs_computers_app
import bobs_computers_Menu

class Computer:
    # create init
    def __init__(self):
        self.CaseColors = {
            "Black":100,
            "White":115,
            "Red":120
        }

        self.CPUVendors = ["AMD", "Intel"]

        self.Motherboards = {
            "Regular":120,
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

        self.inputValidadator = bobs_computers_app.inputValidation()
        self.menuPrinter = bobs_computers_Menu

        self.ItemsGottenList = []
    
    """Define getter with @property decorator"""
    @property
    def quantity(self):
        return self._quantity
    
    """Define setter with @property.setter decorator"""
    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity

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
        print("\nWhen making building a computer you can choose the color of the case. Here are your options to choose from: ")
        
        CaseColors = {
            "Black":100,
            "White":115,
            "Red":120
        }

        inputprompt = "Enter name of the color that tickles your fancy: "
        errormessage = "That input wasnt a case color we have in stock! \ntry again:"

        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(CaseColors, inputprompt, errormessage)

        self.ItemsGottenList.append(tempreceptitem)

        return output

#CPUVendor, give the user the illusion of choice when picking a cpu/motherboard, if they pick AMD they will get an AMD CPU
    
    def CPUVendor(self) -> str:
        print("When choosing a motherboard it is crucial for us to know what Vendor of CPU you will be using. Here are you options of vendors we carry: ")

        inputprompt = "Enter number of the Vendor you like best, if you dont know just choose the color you like best. Intel is blue, AMD is red: "
        errormessage = "That input wasnt a CPU vendor we carry! \ntry again:"

        for i in range(len(self.CPUVendors)):
            print(f"[{i+1}]: {self.CPUVendors[i]}")

        while True:
            cpuBrand = int(self.inputValidadator.validateNumRange(inputprompt,[1,len(self.CPUVendors)]))

            if cpuBrand == 1 or cpuBrand == 2:
                return self.CPUVendors[cpuBrand-1]
        


#MotherboardType (Maby just let the choose if they want wifi or not at a $30 dollar discount if they dont to make it simpler)
    def MotherboardTypeMenu(self) -> int:

        print("Additionally You can pick whether or not you need your motherboard to support wifi. Here are your options to choose from: ")

        inputprompt = "Enter name of the motherboard that tickles your fancy: "
        errormessage = "That input wasnt a Motherboard we have in stock! \ntry again:"
        
        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(self.Motherboards, inputprompt, errormessage)

        self.ItemsGottenList.append(tempreceptitem)

        return output
    
#CPU(could do a specific SKU or just simplify and calculate cost baised on per core basis)
    def cpuTypeMenu(self) -> int:
        print("Here are the options for your CPU: ")

        inputprompt = "Enter the CPU you want: "
        errormessage = "That input is not a cpu we have in stock! \nTry again: "

        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(self.cpuOptions, inputprompt, errormessage)

        self.ItemsGottenList.append(tempreceptitem)

        return output

#CPU COOLER
    def cpuCoolerMenu(self) -> int:
        print("Pick which CPU cooler you want from the options below: ")

        inputprompt = "Enter the CPU cooler you want: "
        errormessage = "That input is not a cooler we have available"

        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(self.cpuCoolerOptions, inputprompt, errormessage)

        self.ItemsGottenList.append(tempreceptitem)

        return output


#GPU(Could do a specific SKU or just simplify and calculate cost baised on ram they want/need)
    def gpuTypeMenu(self) -> int:
        print("Here are the options for your GPU: ")

        inputprompt = "Enter the name of the GPU you want: "
        errormessage = "That input is not a GPU we have in stock! \nTry again: "

        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(self.gpuOptions, inputprompt, errormessage)

        self.ItemsGottenList.append(tempreceptitem)

        return output

#StorageType(the user can choose what type of storage they want)
    def storageTypeMenu(self) -> int:
        print("Here are the options for your storage: ")

        inputprompt = "Enter the type of storage you want: "
        errormessage = "That input is not a storagr type we have in stock! \nTry again: "

        tempreceptitem, output = self.menuPrinter.Bobs_Computer_Menu.MenuMaker(self.storageoptions, inputprompt, errormessage)

        self.ItemsGottenList.append(tempreceptitem)

        return output

#memoryoption(the user can choose what type of memory they want)
    def memoryoptionMenu(self) -> int:
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

