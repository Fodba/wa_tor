# Classe représentant un poisson dans la grille
import random as r

class Poisson:
    HAUT = (0, -1)
    BAS = (0, 1)
    DROITE = (1, 0)
    GAUCHE = (-1, 0)

    def __init__(self, position_x: int, position_y: int, temps_reproduction: int = 3) -> None:
        self.position_X = position_x
        self.position_Y = position_y
        self.image = "O"
        self.temps_reproduction = temps_reproduction
        self.compteur_reproduction = 0
        self.ancien_X = position_x
        self.ancien_Y = position_y

    def regarder(self, grille):
        # Récupérer les quatre cases voisines avec l'effet torique
        haut = ((self.position_X - 1) % grille.taille_grille[0], self.position_Y)
        bas = ((self.position_X + 1) % grille.taille_grille[0], self.position_Y)
        gauche = (self.position_X, (self.position_Y - 1) % grille.taille_grille[1])
        droite = (self.position_X, (self.position_Y + 1) % grille.taille_grille[1])

        return haut, bas, gauche, droite

    def mouvement(self, direction=None, grille=None, population=None):
        if grille is None:
            return None

        # Un chronon passe même si le poisson reste bloqué
        self.compteur_reproduction += 1

        cases_vides = []
        haut, bas, gauche, droite = self.regarder(grille)

        # Chercher les cases libres autour du poisson
        for nom, case in [
            ("haut", haut),
            ("bas", bas),
            ("gauche", gauche),
            ("droite", droite)
        ]:
            x, y = case

            # Ne pas choisir sa propre case
            if case == (self.position_X, self.position_Y):
                continue

            # Vérifier les animaux présents dans la population
            if population is not None:
                case_occupee = any(
                    animal.position_X == x and animal.position_Y == y
                    for animal in population
                )
            else:
                case_occupee = grille.surface[x][y] != " "

            if not case_occupee and (nom, case) not in cases_vides:
                cases_vides.append((nom, case))

        # Aucun déplacement possible
        if len(cases_vides) == 0:
            return None

        # Garder l'ancienne position
        self.ancien_X = self.position_X
        self.ancien_Y = self.position_Y

        # Choisir une direction
        if direction is not None:
            destinations = [
                case for nom, case in cases_vides
                if nom == direction
            ]

            if len(destinations) == 0:
                return None

            destination = destinations[0]
        else:
            destination = r.choice(cases_vides)[1]

        # Déplacer le poisson
        self.position_X = destination[0]
        self.position_Y = destination[1]

        # Mettre à jour la grille
        grille.surface[self.ancien_X][self.ancien_Y] = " "
        grille.surface[self.position_X][self.position_Y] = self.image

        # Reproduction après le déplacement
        if self.compteur_reproduction >= self.temps_reproduction:
            return self.se_reproduire(grille)

        return None

    def se_deplacer(self, direction):
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

        # Le bébé naît sur l'ancienne case du parent
        nouveau_poisson = Poisson(
            self.ancien_X,
            self.ancien_Y,
            self.temps_reproduction
        )

        grille.surface[self.ancien_X][self.ancien_Y] = nouveau_poisson.image

        # Recommencer le cycle de reproduction
        self.compteur_reproduction = 0

        return nouveau_poisson


if __name__ == "__main__":
    poisson = Poisson(2, 3, 3)
    print(f"poisson : {poisson}")