

class Duck:
    def __init__(self):
        self.legs = 2
        self.eyes = 2
        self.color = "white"
        self.isInfernal = False

    def make_infernal(self):
        self.isInfernal = True
        print("YOUR DUCK HAS BECOME A DEMON FROM YOUR DEEPEST NIGHTMARES\nBEWARE AND RUN")

    def __str__(self):
        res = f"The duck has {self.legs} legs and {self.eyes} eyes and its {self.color}. Currently it is "
        if (not self.isInfernal):
            res += "not "
        return res + "infernal."