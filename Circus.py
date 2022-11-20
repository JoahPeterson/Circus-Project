from Animal import animal

class circus:
    cName = ""
    animals = []
    clownCount = 0
    ringNum = 0

    def __init__(self):
        circus.animals = []
        circus.cName = "Crazy Circus"
        circus.clownCount = 7
        circus.ringNum = 3

    def AddAnimal(self, animal):
        self.animals.append(animal)


    def Parade(self):
        print(circus.cName + ", A " + str(circus.ringNum) + " Ring Circus")
        print("Staring a total of " + str(circus.clownCount) + " wacky clowns!")
        circus.animals.sort()
        for ani in circus.animals:
            print(ani)
            
