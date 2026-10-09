from wa_tor.classes.poisson import Poisson
from wa_tor.classes.grille import Grille
from classes.requin import Requin
from wa_tor.classes.monde import Monde
import random as r

TAILLE_GRILLE = 15

def main():
    print("hello world")
    world = Monde(25,25)
    world.initialisation(25,25)
    world.boucle()


if __name__ == "__main__":
    main()