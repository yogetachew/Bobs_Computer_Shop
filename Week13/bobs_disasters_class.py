import random

class Disasters:
    def __init__(self) -> None:
        pass

    def ShipIncorrectColor(self, colors, colorchoosen):
        disasterchance = random.randint(1, 2)

        if disasterchance == 1:
            randomcolor = random.randint(0,len(colors)-1)


            keysbad = colors.keys()
            keygood = []

            for key in keysbad:
                    keygood.append(key)

            newcasecolor = keygood[randomcolor]
            newcaseprice = colors.get(newcasecolor)


            if colorchoosen[0] != newcasecolor:
                print("\n#--------------------------------------------------------------------------------------------#")
                print(f"DISASTER HAS STRUCK:\n You chose {colorchoosen[0]} but somehow you ended up with {newcasecolor}")
                print("#----------------------------------------------------------------------------------------------#\n")
                return [newcasecolor, newcaseprice], newcaseprice
            
        return colorchoosen, colorchoosen[1]
    
    def failedDelivery(self, premium_shipping, warranty):
        if warranty == "n":
            if premium_shipping == "n":
                river = random.randint(1,10)
                if river <= 3:
                    return("Uh Oh!, the UPS Driver drove into a river and destroyed your PC")
                else:
                    return("Your package was properly shipped")
            elif premium_shipping == "y":
                river = random.randint(1,10)
                if river == 1:
                    return("Uh Oh!, the UPS Driver drove into a river and destroyed your PC")
                else:
                    return("Your package was properly shipped")
        else:
            return("Your package was properly shipped")