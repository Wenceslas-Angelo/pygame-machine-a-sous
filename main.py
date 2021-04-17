import random
import numpy

print("Bienvenue sur la machine à sous GravenFruitiiii")

fruits = ["ananas", "cerise", "orange", "pasteque", "pomme_dore"]
proba_fruit= [0.2, 0.25, 0.4, 0.1, 0.05]
fruits_jetons = {
                    "ananas":50,
                    "cerise":15,
                    "orange":5,
                    "pasteque":150,
                    "pomme_dore":10000
                }

hasard = numpy.random.choice(fruits, 3, proba_fruit)

if hasard[0] == hasard[1] == hasard[2]:
    jetons = fruits_jetons[hasard[0]]
    print("{}: + {} jetons".format(hasard[0], jetons))