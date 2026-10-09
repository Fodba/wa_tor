from classes.poisson import Poisson
from classes.grille import Grille
from classes.requin import Requin
import time
import random as r


# Classe gérant la simulation
class Monde:
    # def __init__(self, grid: Grid) -> None:
    def __init__(self,largeur:int,hauteur:int) -> None:
    # def __init__(self) -> None:
        self.population = [] # Liste des entités (poisson et Shark) présents sur la grille
        self.chronon = 0 # 
        self._largeur = largeur
        self._hauteur = hauteur
        self._ratio_pop_totale: int = 0
        self._ratio_shark_poisson: int = 0
        self.initialisation(largeur,hauteur)


    def ajuster_coordonnees(self, position_x, position_y):
        """Redéfini les coordonnées en coordonnées du monde torique

        Args:
            position_x (int): position horizontale de base sur la grille
            position_y (int): position verticale de base sur la grille

        Return:
            Le couple de coordonées (x, y) tenant compte du monde torique
        """
        # """Applique l'effet torique sur les coordonnées (position_x, position_y)"""
        x_torique = position_x % self.largeur
        y_torique = position_y % self.hauteur
        return x_torique, y_torique


    def initialisation(self, largeur: int, hauteur: int) -> None:
        self.taille_grille = (largeur,hauteur)
        self.grille = Grille(largeur)
        # self.grille.initialisation(largeur,hauteur)
    
    def check_reproduction(self,poisson: Poisson, reproduction_time: int):
        # Vérifie si le temps de reproduction est écoulé pour le poisson
        if poisson.temps_reproduction == 0:
            return True
        else: 
            return False
        pass

    def action_poisson(self,poisson: Poisson):
        # le poisson observe son environnement
        # le poisson évalue sa destination
        # le poisson se déplace 
        resultat = poisson.regarder()
        poisson.mouvement(resultat)
        poisson.reproduction()


    def boucle(self):
        population_totale:list[Poisson] = []
        nouvelle_population:list[Poisson] = []
        continuer = True

        while continuer:
            # Création et placement de la population
            for position_horizontale in range(self.taille_grille[0]):
                for position_verticale in range(self.taille_grille[1]):
                    if r.randint(0,100) < 10:
                        temps_reproduction_requin = 5
                        nouveau_requin = Requin(position_horizontale,position_verticale,temps_reproduction_requin)
                        nouvelle_population.append(nouveau_requin)
                        # if self.check_reproduction(new_shark,shark_reproduction_time):
                        #     new_shark.mouvement()
                        #     new_shark2 = Shark(position_horizontale,position_verticale,shark_reproduction_time)
                        #     new_population.append(new_shark2)

                    elif r.randint(0,100) < 30:
                        temps_reproduction_poisson = 3
                        nouveau_poisson = Poisson(position_horizontale,position_verticale,temps_reproduction_poisson)
                        nouvelle_population.append(nouveau_poisson)
                    

            # Affichage de la population
            self.grille.afficher(nouvelle_population)

            # Défilement des chronons
            self.chronon += 1
            print(self.chronon)
            print()
            time.sleep(0.5)


    def genere_rapport(self):
        """Génère un rapport de données de la simulation
        """
        pass
