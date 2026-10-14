
# Classe représentant un poisson dans la grille
import random as r

class Poisson:
    HAUT = (0,-1)
    BAS = (0,1)
    DROITE = (1,-1)
    GAUCHE = (-1,-1)

    def __init__(
            self, 
            position_x: int, 
            position_y: int, 
            temps_reproduction: int
        ) -> None:
        self.position_X = position_x
        self.position_Y = position_y
        self.image = "O"
        self.temps_reproduction = temps_reproduction
        # Compter les chronons depuis la dernière reproduction
        self.compteur_reproduction = 0


    def regarder(self, grille):

        #Variable des coordonnées des 4 cases voisines du poisson.
            # +1 ou -1 permet de regarder une seule case à la fois.
            #Comme c'est un monde torique le % permet de passer d'un bord à l'autre de la grille.
        haut = ((self.position_X - 1) % grille.taille_grille[0], self.position_Y)
        bas = ((self.position_X + 1) % grille.taille_grille[0], self.position_Y)
        gauche = (self.position_X, (self.position_Y - 1) % grille.taille_grille[1])
        droite = (self.position_X, (self.position_Y + 1) % grille.taille_grille[1],)
        
        return haut, bas, gauche, droite


    def mouvement(self, direction: str = None, grille = None, population=None):
        # se déplace aléatoirement (ou non) sur les axes horizontaux et verticaux

        if grille is None:

            return
        cases_vides = []

        haut, bas, gauche, droite = self.regarder(grille)

        if grille.surface[haut[0]][haut[1]] == " ":
            cases_vides.append(("haut", haut))

        if grille.surface[bas[0]][bas[1]] == " ":
            cases_vides.append(("bas", bas))

        if grille.surface[gauche[0]][gauche[1]] == " ":
            cases_vides.append(("gauche", gauche))

        if grille.surface[droite[0]][droite[1]] == " ":
            cases_vides.append(("droite", droite))

        if len(cases_vides) == 0:
            return

        if direction:

            for case in cases_vides:
                if case[0] == direction:
                    self.position_X = case[1][0]
                    self.position_Y = case[1][1]
                    break

        else:

            case = r.choice(cases_vides)


            self.position_X = case[1][0]
            self.position_Y = case[1][1]

        

        # On diminue le temps avant la reproduction
        if self.compteur_reproduction <= self.temps_reproduction:
            self.compteur_reproduction += 1

        if self.compteur_reproduction >= self.temps_reproduction:
            self.se_reproduire(grille)


    def se_deplacer(self,direction):
        if direction == "haut":
            self.position_X -= 1
        if direction == "bas":
            self.position_X += 1
        if direction == "gauche":
            self.position_Y -= 1
        if direction == "droite":
            self.position_Y += 1


    def se_reproduire(self, grille=None):
            if grille is None:
                return None

            # On cherche les cases vides autour du poisson
            cases_vides = []

            haut, bas, gauche, droite = self.regarder(grille)

            if grille.surface[haut[0]][haut[1]] == " ":
                cases_vides.append(haut)

            if grille.surface[bas[0]][bas[1]] == " ":
                cases_vides.append(bas)

            if grille.surface[gauche[0]][gauche[1]] == " ":
                cases_vides.append(gauche)

            if grille.surface[droite[0]][droite[1]] == " ":
                cases_vides.append(droite)

            if len(cases_vides) == 0:
                return None


            """ pas aléatoire mais se reproduit à l'ancienne position du poisson."""
            # # On crée un bébé poisson dans une case vide
            # case = r.choice(cases_vides)

            # nouveau_poisson = Poisson(case[0], case[1], 3)

            # grille.surface[case[0]][case[1]] = nouveau_poisson.image

            # self.temps_reproduction = 3

            # return nouveau_poisson
            
            


if __name__ == "__main__":
    poisson = Poisson(2,3,3)
    print(f"poisson : {poisson}")

    poisson.mouvement()

