
"""
    Name: bobs_computer_Business.py
    Created: 11/1/23
    Purpose: class file for tracking profit/loss/sales
"""
class Business:
    def __init__(self, sales=0, costs=0, profit=0):
        self.totalSales = sales
        self.totalCosts = costs
        self.totalProfit = profit

    #------------SALES--------------
    def returnSales(self):
        return self.totalSales
    
    def trackSales(self, runningTotal):
        self.totalSales += runningTotal     
    
    #---------------COSTS----------------
    def returnCosts(self):
        return self.totalCosts
    
    def trackCosts(self):
        self.totalCosts = (self.totalSales / 5)
    
    #--------------PROFIT--------------#
    def returnProfit(self):
        return(self.totalProfit)
    
    def trackProfit(self):
        self.totalProfit = self.totalSales - self.totalCosts

    