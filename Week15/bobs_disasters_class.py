import random

class Disasters:
    def __init__(self) -> None: # empty __init__ function
        pass

    def ShipIncorrectColor(self, colors, colorchoosen):
        disasterchance = random.randint(1, 2) # generate random chance for disaster

        if disasterchance == 1:
            randomcolor = random.randint(0,len(colors)-1) #if disaster chance is 1: set random case color to random color


            keysbad = colors.keys() # assign keysbad to the keys of the colors
            keygood = [] # empty keygood list

            for key in keysbad: # loop to add the keys to the keygood list
                    keygood.append(key)

            newcasecolor = keygood[randomcolor] #set new case color to randomly chosen new color
            newcaseprice = colors.get(newcasecolor) # set case price to price for the new case color


            if colorchoosen[0] != newcasecolor: # if the randomly chosen case color is not the new case color
                # display that the wrong color was chosen
                print("\n#--------------------------------------------------------------------------------------------#")
                print(f"DISASTER HAS STRUCK:\n You chose {colorchoosen[0]} but somehow you ended up with {newcasecolor}")
                print("#----------------------------------------------------------------------------------------------#\n")
                return [newcasecolor, newcaseprice], newcaseprice # return new case color/price
            
        return colorchoosen, colorchoosen[1] # return  original color if random disaster chance doesn't happen
    
    # determine if the item is properly shipped to the user, or if the delivery failes (UPS driver drives into river)
    # rates are extremely bad, because it is funny
    def failedDelivery(self, premium_shipping, warranty): 
        if warranty == "n":
            if premium_shipping == "n": # no warranty or premium shipping
                river = random.randint(1,10)
                if river <= 3: # 30% chance for failed delivery
                    return("Uh Oh!, the UPS Driver drove into a river and destroyed your PC")
                else:
                    return("Your package was properly shipped")
            elif premium_shipping == "y": # no warranty, but has premium shipping
                river = random.randint(1,10)
                if river == 1: # 10% chance for failed delivery
                    return("Uh Oh!, the UPS Driver drove into a river and destroyed your PC")
                else:
                    return("Your package was properly shipped")
        else: # if they have warranty, the package ships properly
            return("Your package was properly shipped")
        
    def WrongStorageOption(self, premium_shipping, warranty):
        # If the user buys a warranty then the user will be safe from the disaster
        if warranty == "n":
            
            # The user will still be safe if they choose premium shipping
            if premium_shipping == "n":
                intern_mistake = random.randint(1,10)

                # If no warrenty or premiun shipment was choosen the user will have
                # 50% of getting the wrong storage order
                if intern_mistake <= 5:
                    return("\nOops, sorry the new intern messed up your storage order choice.\n")
                else:
                    return("")
                
            elif premium_shipping == "y":
                    return("")
            
        else:
            return("")