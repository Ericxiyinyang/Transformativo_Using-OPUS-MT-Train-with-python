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
    def stdforminput(self):
        userin = input()
        formatted_form = userin.lower()
        if formatted_form == "yo" or formatted_form == "i":
            return "I"
        elif formatted_form == "tu" or formatted_form == "you":
            return "You"
        elif formatted_form == "el":
            return "He"
        elif formatted_form == "ella":
            return "She"
        elif formatted_form == "usted":
            return "He"
        elif formatted_form == "nosotros" or formatted_form == "nosotras":
            return "We"
        elif formatted_form == "ellos" or formatted_form == "ellas":
            return "They"



