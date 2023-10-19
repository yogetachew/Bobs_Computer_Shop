"""
    Name: Bobs_computers_class.py
    Author: Aidan Newberry
    Created: 10/11/2023
    Purpose: Use @property Pythoic way of accessing attrabutes
"""

class Computer:
    # create init
    def __init__(self):
        pass
    
    """Define getter with @property decorator"""
    @property
    def quantity(self):
        return self._quantity
    
    """Define setter with @property.setter decorator"""
    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity

    def ComputerCaseMenu(self) -> int:
        print("When making building a computer you can choose the color of the case. Here are your options to choose from: ")

        colors = {
            "Black":100,
            "White":115,
            "Red":120
        }

        while True:
            print("(Black) $100 \n(White) $115 \n(Red) $120")
            userinput = input("Enter name of the color that tickles your fancy: ")
            
            casecolorprice = colors.get(userinput, f"{userinput}, wasnt a case color we have in stalk! \ntry again:")

            if casecolorprice != f"{userinput}, wasnt a case color we have in stalk! \ntry again:":
                return casecolorprice 

#ComputerCase (Probbly jsut let the choose the color to make it simpler)
#MotherboardType (Maby just let the choose if they want wifi or not at a $30 dollar discount if they dont to make it simpler)
#CPU(could do a specific SKU or just simplify and calculate cost baised on per core basis)
#GPU(Could do a specific SKU or just simplify and calculate cost baised on ram they want/need)
#MemoryAmmount
#StorageType(HHD, SSD, NVME) (just do this calculation baised on cost per gigabyte)