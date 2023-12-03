import bobs_computers_app

class Bobs_Computer_Menu:

    def MenuMaker(dictionary:dict, inputprompt:str, errormessage:str):
        """handles majority of menu making"""
        inputValidadator = bobs_computers_app.inputValidation()
        
        # Get the length of the dictionary
        dictionarylen = len(dictionary)

        while True:
            # Print the formatted menu
            print(FormatMenu(dictionary))

            # Get a list of dictionary keys
            keysbad = dictionary.keys()
            keygood = []

            for key in keysbad:
                 keygood.append(key)

            # Get user input within the valid range
            userinput = int(inputValidadator.validateNumRange(inputprompt, [1,dictionarylen]))-1

            """item = dictionary.get(userinput, errormessage)"""
            item = list(dictionary.values())[userinput]

            # Check if the item is not an error message
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
    
    # Initialize an empty string to store the formatted menu
    menustr = ""

    # Enumerate through the dictionary items, starting from index 1
    for index, (key, value) in enumerate(input.items(), start=1):
        menustr += f"[{index}]: {key}: ${value:.2f} \n"
    
    # Return the formatted menu string
    return menustr