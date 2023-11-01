
"""
    Name: bobs_computer_Business.py
    Created: 11/1/23
    Purpose: class file for tracking profit/loss/sales
"""
class Business:
    def __init__(self, sales=0, costs=0, profit=0):
        self.totalSales = 0
        self.totalCosts = 0
        self.totalProfit = 0

    #------------SALES--------------
    @property
    def trackSales(self):
        return self.totalSales
    
    @trackSales.setter
    def trackSales(self, runningTotal):
        self.totalSales += runningTotal     
    
    #---------------COSTS----------------
    @property
    def trackCosts(self):
        return self.totalCosts
    
    @trackCosts.setter
    def trackCosts(self, products:dict):
        self.totalCosts = (products.values() / 5)
    
    #--------------PROFIT--------------#
    @property
    def trackProfit(self):
        return(self.totalProfit)
    
    @trackProfit.setter
    def trackProfit(self):
        self.totalProfit = self.totalSales - self.totalCosts