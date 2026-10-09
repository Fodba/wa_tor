from classes.poisson import Poisson
from classes.requin import Requin

# Classe représentant la grille de la simulation
class Grille:
    def __init__(self, size: int) -> None:
        self.surface:list[list[str]] = self.creer_grille(size)
        

    def creer_grille(self,size):
        grille = []
        for position_horizontale in range(0,size):
            ligne = []
            for position_verticale in range(0,size):
                ligne.append(" ")
            grille.append(ligne)
        self.taille_grille = size
        return grille


    def afficher(self, population: list[Poisson]):
        for fish in population:
            # Lancer pour chaque fish la méthode mouvement()



            # Le caractère sur la grille correspond au caractère ou l'image 
            # utilisé pour représenter le poisson ou le requin 
            self.surface[fish.position_X][fish.position_Y] = fish.image

        for position_horizontale in range(self.taille_grille):
            ligne = "|"
            for position_verticale in range(self.taille_grille):
                ligne += self.surface[position_horizontale][position_verticale] # pour afficher cahque caractère de la surface.
                ligne += "|"
            print(ligne)


