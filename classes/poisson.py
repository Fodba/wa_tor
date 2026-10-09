# Classe représentant un poisson dans la grille
class Poisson:
    def __init__(
            self, 
            position_x: int, 
            position_y: int, 
            temps_reproduction: int
        ) -> None:
        self.position_X = position_x
        self.position_Y = position_y
        self.image = "O"


    def regarder(self):
        """Permet au poisson de savoir ce qui se trouve dans les cases de son entourage"""
        pass


    def peut_se_reproduire(self):
        """Verifie si le poisson est en mesure de se reproduire à l'instant T"""
        pass


    def mouvement(self, direction: str = None):
        # se déplace aléatoirement (ou non) sur les axes horizontaux et verticaux
        # if direction: (Si une direction est fournie)
        #   Le poisson suit cette direction
        # else:
        #   Si un requin est présent sur une case voisine:
        #       Le poisson se déplace dans la direction opposé au requin
        #   Sinon:
        #       Le poisson se déplace aléatoirement sur l'une des cases vides présentes.
        pass


    def se_reproduire(self):
        # vérification du temps de reproduction
        # Vérification des cases à proximité
        pass