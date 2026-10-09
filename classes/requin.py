from classes.poisson import Poisson

# Classe représentant un requin, hérite des caractéristiques de Poisson
class Requin(Poisson):
    def __init__(
            self, 
            position_x: int, 
            position_y: int, 
            temps_reproduction: int
        ) -> None:
        self.position_X = position_x
        self.position_Y = position_y
        self.energie = 5 # énergie de départ
        self.temps_reproduction = temps_reproduction
        self.image = "X"


    def perte_energie(self):
        # défini la perte d'energie
        pass


    def récupération_energie(self):
        # défini la récupération d'énergie
        pass


    def mouvement(self):
        # le requin regarde autour de lui
        # Si poisson à proximité, se déplace vers le poisson
        # sinon se déplace aléatoirement (appel à la méthode parent).
        # Perds un point à chaque déplacement
        super().mouvement("haut")
        pass

    def manger(self,poisson):
        # supprimer le poisson
        # se déplacer à la position du poisson
        # récupère un point d'énergie
        pass


    def se_reproduire(self):
        # Vérification de l'énergie restante
        # vérification du temps de reproduction
        # Vérification des cases à proximité
        pass



    vide = 0
    