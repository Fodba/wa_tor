from classes.poisson import Poisson
from classes.grille import Grille
from classes.requin import Requin
from classes.monde import Monde
import random as r

LARGEUR_GRILLE = 32
HAUTEUR_GRILLE = 14
POPULATION_GLOBALE = 220

def main():
    print("hello world")
    world = Monde(LARGEUR_GRILLE, HAUTEUR_GRILLE, POPULATION_GLOBALE)
    # world.initialisation(LARGEUR_GRILLE,HAUTEUR_GRILLE)
    world.boucle()


if __name__ == "__main__":
    main()

    # taille_grille = 10
    # grille = Grille(taille_grille,taille_grille)
    # x = r.randint(0,taille_grille-1)
    # y = r.randint(0,taille_grille-1)
    # poisson = Poisson(x,y,3)
    # # grille.surface[5][5] = poisson.image

    # ancien_X = poisson.position_X
    # ancien_Y = poisson.position_Y

    # #afficher la position actuel du poisson.
    # print("Position actuel :", ancien_X, ancien_Y)

    # #Déplacer du poisson
    # poisson.mouvement(grille=grille)

    # print(" déplacement effectué :", poisson.position_X, poisson.position_Y)

    # #Vérifié si le déplacement c'est bien effectué.
    # difference_X = (poisson.position_X - ancien_X) % grille.taille_grille[0]
    # difference_Y = (poisson.position_Y - ancien_Y) % grille.taille_grille[1]

    # if (difference_X != 0 and difference_Y == 0) or \
    #     (difference_Y != 0 and difference_X == 0): 
        

    #     print("Le poisson s'est déplacé d'une case.")
    # else:
    #     print("Le poisson ne s'est pas déplacé d'une case.") 

    
