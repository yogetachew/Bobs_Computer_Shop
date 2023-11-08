import bobs_computers_app

class Bobs_Computer_Menu:

    def MenuMaker(dictionary:dict, inputprompt:str, errormessage:str):
        """handles majority of menu making"""
        inputValidadator = bobs_computers_app.inputValidation()
        
        dictionarylen = len(dictionary)

        while True:
            print(FormatMenu(dictionary))

            keysbad = dictionary.keys()
            keygood = []


            for key in keysbad:
                 keygood.append(key)

            userinput = int(inputValidadator.validateNumRange(inputprompt, [1,dictionarylen]))-1

            """item = dictionary.get(userinput, errormessage)"""
            item = list(dictionary.values())[userinput]
            if item != errormessage:
                    return [keygood[userinput], item], item
            
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