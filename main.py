from Animal import animal
from Circus import circus


animal4 = animal("Ellie", 3, "Elephant")
animal2 = animal("Manny", 6, "Elephant")
animal7 = animal("Dumbo", 81, "Elephant")
animal1 = animal("Simba", 6, "Lion")
animal5 = animal("Scar", 6, "Lion")
animal6 = animal("Melvin", 4, "Giraffe")
animal3 = animal("Spots", 8, "Giraffe")


myCircus = circus()

myCircus.AddAnimal(animal1)
myCircus.AddAnimal(animal2)
myCircus.AddAnimal(animal3)
myCircus.AddAnimal(animal4)
myCircus.AddAnimal(animal5)
myCircus.AddAnimal(animal6)
myCircus.AddAnimal(animal7)


myCircus.Parade()

