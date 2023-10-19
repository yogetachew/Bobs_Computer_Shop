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

#ComputerCase (Probbly jsut let the choose the color to make it simpler)
#MotherboardType (Maby just let the choose if they want wifi or not at a $30 dollar discount if they dont to make it simpler)
#CPU(could do a specific SKU or just simplify and calculate cost baised on per core basis)
#GPU(Could do a specific SKU or just simplify and calculate cost baised on ram they want/need)
#MemoryAmmount
#StorageType(HHD, SSD, NVME) (just do this calculation baised on cost per gigabyte)
