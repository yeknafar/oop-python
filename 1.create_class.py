class human():

    def __init__(self, name, famil):
        
        print("a new object created")
        self.w = 74
        self.h = 1.92
        self.country = "iran"
        self.name = name
        self.famil = famil
        
    def walking(self):
        pass

    def writing(self):
        pass

    def eating(self):
        pass

    def introducing(self):
        print("My name is {} {}".format(self.name, self.famil))

hasanShamaeizade = human("hasan", "shamaizadeh")
hasanShamaeizade.introducing()