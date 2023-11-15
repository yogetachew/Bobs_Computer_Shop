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
                print("\n#----------------------------------------------------------------------------#")
                print(f"DISASTER HAS STRUCK:\n You chose {colorchoosen[0]} but somehow you ended up with {newcasecolor}")
                print("#----------------------------------------------------------------------------#\n")
                return [newcasecolor, newcaseprice], newcaseprice
            
        return colorchoosen, colorchoosen[1]
    