class inputProcessor:
    def __init__(self):
        pass

    def stdlanginput(self):
        userin = input()
        if userin[:2].lower() == "en":
            return "en"
        elif userin[:2].lower() == "fr":
            return "fr"
        elif userin[:2].lower() == "sp" or userin[:2].lower() == "es":
            return "es"
        elif userin[:2].lower() == "ch":
            return "zh"
        else:
            print("Invalid language, please try again.")
            self.stdlanginput()
