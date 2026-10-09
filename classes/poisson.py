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

    def mouvement(self, direction: str = None):
        # se déplace aléatoirement (ou non) sur les axes horizontaux et verticaux
        # if direction:
        # else:
        pass

    def se_reproduire(self):
        # vérification du temps de reproduction
        # Vérification des cases à proximité
        pass