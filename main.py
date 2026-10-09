from classes.poisson import Poisson
from classes.grille import Grille
from classes.requin import Requin
from classes.monde import Monde
import random as r

LARGEUR_GRILLE = 5
HAUTEUR_GRILLE = 5

def main():
    print("hello world")
    world = Monde(LARGEUR_GRILLE,HAUTEUR_GRILLE)
    world.initialisation(LARGEUR_GRILLE,HAUTEUR_GRILLE)
    world.boucle()


if __name__ == "__main__":
    main()