class Bobs_Computer_Menu:
    
    def Menu(dictionary:dict, inputprompt:str, errormessage:str):
        """handles majority of menu making"""
        while True:
            print(FormatMenu(dictionary))

            userinput = int(input(inputprompt))-1

            """item = dictionary.get(userinput, errormessage)"""
            item = list(dictionary.values())[userinput]
            if item != errormessage:
                    return item
            
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