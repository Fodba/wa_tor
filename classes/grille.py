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
        self.surface:list[list[str]] = self.creer_grille(self.taille_grille[0],self.taille_grille[1])
        for poisson in population:
            # Lancer pour chaque fish la méthode regarder()
            # Lancer pour chaque fish la méthode mouvement()



            # Le caractère sur la grille correspond au caractère ou l'image 
            # utilisé pour représenter le poisson ou le requin 
            self.surface[poisson.position_X][poisson.position_Y] = poisson.image

        for position_horizontale in range(self.taille_grille[0]):
            ligne = "|"
            for position_verticale in range(self.taille_grille[1]):
                ligne += self.surface[position_horizontale][position_verticale] # pour afficher chaque caractère de la surface.
                ligne += "|"
            print(ligne)


