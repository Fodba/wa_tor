from wa_tor.classes.poisson import Poisson
from wa_tor.classes.grille import Grille
from classes.requin import Requin
from wa_tor.classes.monde import Monde
import random as r

LARGEUR_GRILLE = 25
HAUTEUR_GRILLE = 25

def main():
    print("hello world")
    world = Monde(LARGEUR_GRILLE,HAUTEUR_GRILLE)
    world.initialisation(LARGEUR_GRILLE,HAUTEUR_GRILLE)
    world.boucle()


if __name__ == "__main__":
    main()