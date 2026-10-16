# Classe représentant un poisson dans la grille
import random as r

#Classe parent qui contient les éléments communs.
#Pour les poissons et les requins de notre écosystème marin.
class Poisson:
    """Représente un poisson et sert aussi de classe parent pour le requin."""

    def __init__(self, position_x: int, position_y: int, temps_reproduction: int = 3) -> None:
        """Crée un poisson avec sa position et son temps de reproduction."""

        #On enregistre la position du poisson sur la grille.
        self.position_X = position_x
        self.position_Y = position_y
        
        #Le O représente le poisson dans la grille.
        self.image = "O"

        #Nombre de chronons nécessaires pour se reproduire.
        self.temps_reproduction = temps_reproduction

        #Ce compteur augmente à chaque tour de chronons.
        self.compteur_reproduction = 0

        #On garde l'ancienne position du poisson.
        self.ancien_X = position_x
        self.ancien_Y = position_y

    def regarder(self, grille) -> tuple:
        """Donne les 4 positions autour du poisson."""

        # Récupérer les quatre cases voisines avec l'effet torique
        #Le % permet de ce déplacer d'un bord à un autre.
        haut = ((self.position_X - 1) % grille.taille_grille[0], self.position_Y)
        bas = ((self.position_X + 1) % grille.taille_grille[0], self.position_Y)
        gauche = (self.position_X, (self.position_Y - 1) % grille.taille_grille[1])
        droite = (self.position_X, (self.position_Y + 1) % grille.taille_grille[1])

        return haut, bas, gauche, droite

    def mouvement(self, grille=None, population=None) -> tuple:

        """Déplace le poisson d'une case libre et peut se reproduire."""

        if grille is None:
            return None

        # Un chronon passe même si le poisson reste sur place.
        self.compteur_reproduction += 1

        #On crée une liste pour stocker les cases libre autour du poisson.
        cases_vides = []

        #On récupère les 4 cases voisines avec la méthode regarder.
        haut, bas, gauche, droite = self.regarder(grille)

        # On vérifie les cases une par une.
        for nom, case in [
            ("haut", haut),
            ("bas", bas),
            ("gauche", gauche),
            ("droite", droite)
        ]:
            #On récupère les coordonnées de la position.
            x, y = case

            #On ignore la case de la position actuel du poisson.
            if case == (self.position_X, self.position_Y):
                continue
            #Le continue sert à passer à une autre case.

            #On reprend la liste , et on regarde dedans si cette case est déjà occupé ou non.
            if population is not None:
                case_occupee = any(
                    animal.position_X == x and animal.position_Y == y
                    for animal in population
                )

            #Sinon, nous regardons dans la grille une case vide.
            else:
                case_occupee = grille.surface[x][y] != " "

            #Si une case se retrouve vide alors elle s'ajoute à la liste.
            if not case_occupee and (nom, case) not in cases_vides:
                cases_vides.append((nom, case))

        #Si la liste reste vide, dans ce cas le poisson reste sur place.
        if len(cases_vides) == 0:
            return None

        # Garder l'ancienne position avant le déplacement.
        self.ancien_X = self.position_X
        self.ancien_Y = self.position_Y

        #random choice en fonction de ce que reçoit la liste.
        #Le [1] permet de récupèrer les coordonées du poisson, sans avoir le nom de la direction.
        destination = r.choice(cases_vides)[1]

        # On récupère les coordonnées de la case choisie, et on donne la nouvelle position qu'aura le poisson.
        self.position_X = destination[0]
        self.position_Y = destination[1]

        #On met à jour la grille parès avoir fait le déplacement, et l'ancienne case devient vide.
        grille.surface[self.ancien_X][self.ancien_Y] = " "

        #On place le poisson à sa nouvelle position.
        grille.surface[self.position_X][self.position_Y] = self.image

        #On vérifie si le poisson à atteint assez de chronons pour pouvoir se reproduire.
        if self.compteur_reproduction >= self.temps_reproduction:
            return self.se_reproduire(grille)

        #Si il ne peut pas se reproduire dans ce cas il ne renvoie rien.
        return None

    def se_reproduire(self, grille=None):
        """Création d'un poisson à l'ancienne position du parent poisson."""

        #Sans la grille, le nouveau poisson ne peut pas être placer.
        if grille is None:
            return None

        #On crée le nouveau poisson, et on le met à l'ancienne position du poisson parent.
        nouveau_poisson = Poisson(self.ancien_X,self.ancien_Y,self.temps_reproduction)

        #On place le nouveau poisson crée à l'ancienne position du poisson parent.
        grille.surface[self.ancien_X][self.ancien_Y] = nouveau_poisson.image

        #Une fois le cycle atteint, on le retourne à 0 pour recommencer la reproduction suivante.
        self.compteur_reproduction = 0

        #On renvoie le nouveau poisson dans le monde pour qu'il puisse être ajouter à la liste des animaux.
        return nouveau_poisson