from classes.monde import Monde
import random as r

HAUTEUR_GRILLE = 14
LARGEUR_GRILLE = 32
POPULATION_GLOBALE = 300

def main():
    print("hello world")
    world = Monde(HAUTEUR_GRILLE, LARGEUR_GRILLE, POPULATION_GLOBALE)
    world.boucle()


if __name__ == "__main__":
    main()