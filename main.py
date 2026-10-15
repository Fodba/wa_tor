from classes.poisson import Poisson
from classes.grille import Grille
from classes.requin import Requin
from classes.monde import Monde
import random as r

HAUTEUR_GRILLE = 32
LARGEUR_GRILLE = 14
POPULATION_GLOBALE = 300

def main():
    print("hello world")
    world = Monde(LARGEUR_GRILLE, HAUTEUR_GRILLE, POPULATION_GLOBALE)
    # world.initialisation(LARGEUR_GRILLE,HAUTEUR_GRILLE)
    world.boucle()


if __name__ == "__main__":
    main()

 

    
