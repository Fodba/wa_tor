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

    def get_contenu_cellule(self,position_x,position_y):
        cellule = self.surface[position_x][position_y]
        if cellule == " ":
            return cellule, "Vide"
        if cellule == "X":
            return cellule, "Requin"
        if cellule == "O":
            return cellule, "Poisson"
        return cellule

    def get_positions_voisines(self,position_x,position_y):
        haut = ((position_x - 1) % self.taille_grille[0], position_y)
        bas = ((position_x + 1) % self.taille_grille[0], position_y)
        gauche = (position_x, (position_y - 1) % self.taille_grille[1])
        droite = (position_x, (position_y + 1) % self.taille_grille[1],)
        # pass
        return haut, bas, gauche, droite

    def afficher(self, population: list[Poisson]):
        self.surface:list[list[str]] = self.creer_grille(
            self.taille_grille[0],
            self.taille_grille[1]
        )
        for poisson in population:
            # Le caractère sur la grille correspond au caractère ou l'image
            # utilisé pour représenter le poisson ou le requin
            self.surface[poisson.position_X][poisson.position_Y] = poisson.image

        for position_horizontale in range(self.taille_grille[0]):
            ligne = "|"
            for position_verticale in range(self.taille_grille[1]):
                # pour afficher chaque caractère de la surface.
                ligne += self.surface[position_horizontale][position_verticale] 
                ligne += "|"
            print(ligne)
