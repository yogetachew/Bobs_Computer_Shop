
"""
    Name: bobs_computer_Business.py
    Created: 11/29/23
    Purpose: class file for tracking profit/loss/sales
"""
class Business:
    def __init__(self, sales=0, costs=0, profit=0): # set default values to 0
        self.totalSales = sales
        self.totalCosts = costs
        self.totalProfit = profit

    #------------SALES--------------
        # sales getter
    def returnSales(self):
        return self.totalSales
    
        # sales setter
    def trackSales(self, runningTotal):
        self.totalSales += runningTotal     # add running total to total sales 
    
    #---------------COSTS----------------
        # costs getter
    def returnCosts(self):
        return self.totalCosts
    
        #costs setter
    def trackCosts(self):
        self.totalCosts = (self.totalSales / 5) #costs are total sales / 5
    
    #--------------PROFIT--------------#
        # profit getter
    def returnProfit(self):
        return(self.totalProfit)

        # profit setter
    def trackProfit(self):
        self.totalProfit = self.totalSales - self.totalCosts # profit is total sales