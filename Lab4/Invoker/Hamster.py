


class Hamster:
    def __init__(self):
        self.legs = 4
        self.eyes = 2
        self.color = "orange"
        self.wealth = 100000000
        self.isCriminal = False

    def make_criminal(self):
        self.isCriminal = True
        print("HAMSTER HAMSTER HAMSTER CRIMINAL!!!\n"
              "HAMSTER HAMSTER HAMSTER CRIMINAL!!!\n"
              "HAMSTER HAMSTER HAMSTER CRIMINAL!!!\n")

    def inflation(self):
        self.wealth = 2
        print("HAMSTER LISTED... NO MONEY")

    def __str__(self):
        res = f"The hamster has {self.legs} legs and {self.eyes} eyes and its {self.color}. It has {self.wealth} USD$ in HMSTR.  Currently it is "
        if (not self.isCriminal):
            res += "not "
        return res + "criminal."