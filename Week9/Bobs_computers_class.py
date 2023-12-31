"""
    Name: Bobs_computers_class.py
    Author: Aidan Newberry
    Created: 10/11/2023
    Purpose: Use @property Pythoic way of accessing attrabutes
"""

class Computer:
    # create init
    def __init__(self):
        self.CaseColors = {
            "Black":100,
            "White":115,
            "Red":120
        }

        self.Motherboards = {
            "Regular":120,
            "Wifi":145
        }

        self.cpuOptions = {
            "4-Core":100,
            "8-Core":200,
            "16-Core":500
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
    
    """Define getter with @property decorator"""
    @property
    def quantity(self):
        return self._quantity
    
    """Define setter with @property.setter decorator"""
    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity

    memory_options = {
    "8GB": 49.99,
    "16GB": 99.99,
    "32GB": 199.99,
    "64GB": 349.99,
    }


    storageType = {
        "HDD 1TB": 49.99,
        "HDD 2TB": 79.99,
        "SSD 256GB": 69.99,
        "SSD 512GB": 119.99,
        "SSD 1TB": 219.99,
    }
    


    def display_storageType(choices):
        print("List of storage types: ")
        for choice, price in choices.items():
            print(f"Your choice was {choice}: ${price}")

#ComputerCase (Probbly jsut let the choose the color to make it simpler)
    def ComputerCaseMenu(self) -> int:
        print("When making building a computer you can choose the color of the case. Here are your options to choose from: ")
        
        inputprompt = "Enter name of the color that tickles your fancy: "
        errormessage = "That input wasnt a case color we have in stock! \ntry again:"

        return Menu(self.CaseColors, inputprompt, errormessage)

#MotherboardType (Maby just let the choose if they want wifi or not at a $30 dollar discount if they dont to make it simpler)
    def MotherboardTypeMenu(self) -> int:
        print("Additionally You can pick whether or not you need your motherboard to support wifi. Here are your options to choose from: ")

        inputprompt = "Enter name of the motherboard that tickles your fancy: "
        errormessage = "That input wasnt a Motherboard we have in stock! \ntry again:"
        
        return Menu(self.Motherboards, inputprompt, errormessage)
    
#CPU(could do a specific SKU or just simplify and calculate cost baised on per core basis)
    def cpuTypeMenu(self) -> int:
        print("Here are the options for your CPU: ")

        inputprompt = "Enter the name of the CPU you want: "
        errormessage = "That input is not a cpu we have in stock! \nTry again: "

        return Menu(self.cpuOptions, inputprompt, errormessage)

#GPU(Could do a specific SKU or just simplify and calculate cost baised on ram they want/need)
    def gpuTypeMenu(self) -> int:
        print("Here are the options for your GPU: ")

        inputprompt = "Enter the name of the GPU you want: "
        errormessage = "That input is not a GPU we have in stock! \nTry again: "

        return Menu(self.gpuOptions, inputprompt, errormessage)

#StorageType(the user can choose what type of storage they want)
    def storageTypeMenu(self) -> int:
        print("Here are the options for your storage: ")

        inputprompt = "Enter the type of storage you want: "
        errormessage = "That input is not a storagr type we have in stock! \nTry again: "

        return Menu(self.storageoptions, inputprompt, errormessage)

#memoryoption(the user can choose what type of memory they want)
    def memoryoptionMenu(self) -> int:
        print("Here are the options for your memory: ")

        inputprompt = "Enter the type of memory you want: "
        errormessage = "That input is not a memory type we have in stock! \nTry again: "

        return Menu(self.memoryoptions, inputprompt, errormessage)

def Menu(dictionary:dict, inputprompt:str, errormessage:str):
    """handles majority of menu making"""
    while True:
        print(FormatMenu(dictionary))

        userinput = int(input(inputprompt))-1

        """item = dictionary.get(userinput, errormessage)"""
        item = list(dictionary.values())[userinput]
        if item != errormessage:
                return item
        
        print(errormessage)



def FormatMenu(input:dict) -> str:
    """
        takes in dictionary
        splits into index #, key and value
        returns formatted menu
    """
    """makes a formatted menu when passed a dictionary"""
    menustr = ""

    for index, (key, value) in enumerate(input.items(), start=1):
        menustr += f"[{index}]: {key}: ${value:.2f} \n"
    return menustr
        


#
#(HHD, SSD, NVME) (just do this calculation baised on cost per gigabyte)
