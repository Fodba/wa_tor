from classes.poisson import Poisson
from classes.requin import Requin

# Classe représentant la grille de la simulation
class Grille:
    def __init__(self, largeur: int, hauteur: int) -> None:
        self.surface:list[list[str]] = self.creer_grille(largeur,hauteur)
        self.taille_grille = (largeur,hauteur)

    def creer_grille(self, largeur: int, hauteur: int):
        grille = []
        for position_horizontale in range(0,largeur):
            ligne = []
            for position_verticale in range(0,hauteur):
                ligne.append(" ")
            grille.append(ligne)
        self.taille_grille = (largeur,hauteur)
        return grille

    def afficher(self, population: list[Poisson]):
        self.surface = self.creer_grille(self.taille_grille[0], self.taille_grille[1])

        for poisson in population:
            self.surface[poisson.position_X][poisson.position_Y] = poisson.image

        for position_horizontale in range(self.taille_grille[0]):
            ligne = "\033[48;2;0;120;180m"
            
            for position_verticale in range(self.taille_grille[1]):
                case = self.surface[position_horizontale][position_verticale]

                if case == "O":
                    ligne += "🐠"
                elif case == "X":
                    ligne += "🦈"
                else:
                    ligne += "🌊"

            print(ligne + "\033[0m")