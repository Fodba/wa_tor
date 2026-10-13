from classes.poisson import Poisson
from classes.grille import Grille
from classes.requin import Requin
import time
import random as r


# Classe gérant la simulation
class Monde:
    # def __init__(self, grid: Grid) -> None:
    def __init__(self,largeur:int,hauteur:int, taille_pop: int) -> None:
    # def __init__(self) -> None:
        self.population = [] # Liste des entités (poisson et requin) présents sur la grille
        self.chronon = 0 # 
        self._largeur = largeur
        self._hauteur = hauteur
        self._ratio_pop_totale: int = 0
        self._ratio_shark_poisson: int = 0
        self.taille_pop = taille_pop
        self.initialisation(largeur,hauteur,taille_pop)


    # def ajuster_coordonnees(self, position_x, position_y):
    #     """Redéfini les coordonnées en coordonnées du monde torique

    #     Args:
    #         position_x (int): position horizontale de base sur la grille
    #         position_y (int): position verticale de base sur la grille

    #     Return:
    #         Le couple de coordonées (x, y) tenant compte du monde torique
    #     """
    #     # """Applique l'effet torique sur les coordonnées (position_x, position_y)"""
    #     x_torique = position_x % self.largeur
    #     y_torique = position_y % self.hauteur
    #     return x_torique, y_torique


    def initialisation(self, largeur: int, hauteur: int, quantite_pop: int) -> None:
        self.taille_grille = (largeur,hauteur)
        self.grille = Grille(largeur,hauteur)
        self.population: list[Poisson] = []
        for i in range(quantite_pop):
            # temps_reproduction_poisson = 5
            x = r.randint(0,self.taille_grille[0]-1)
            y = r.randint(0,self.taille_grille[1]-1)
            # nouveau_poisson = Poisson(x,y,temps_reproduction_poisson)
            # self.population.append(nouveau_poisson)
            # nouveau_poisson = Requin(x,y,temps_reproduction_poisson)
            # self.population.append(nouveau_poisson)
        # for position_horizontale in range(self.taille_grille[0]):
        #     for position_verticale in range(self.taille_grille[1]):
            if r.randint(0,4) == 1:
                    temps_reproduction_requin = 5
                    nouveau_requin = Requin(x,y,temps_reproduction_requin)
                    self.population.append(nouveau_requin)
            # # elif r.randint(0,4) < 30:
            else:
                    temps_reproduction_poisson = 3
                    nouveau_poisson = Poisson(x,y,temps_reproduction_poisson)
                    self.population.append(nouveau_poisson)
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
        continuer = True

        while continuer:
            nouvelle_population = self.population.copy()
            count = 1
            for animal in self.population:
                # print(type(animal))
                print(f"compteur d'animaux: {count}")
                result = animal.mouvement(grille = self.grille,population=nouvelle_population)
                # if result[0] == "Déplacement":
                #     if self.check_reproduction():
                #         requin = Requin(result[1][0],result[1][1],5)
                #         nouvelle_population.append(requin)
                # if isinstance(result,Requin):
                #     nouvelle_population.append(result[1])
                count += 1

            # Affichage de la population
            # print(f"nouvelle population : {nouvelle_population}")
            # self.initialisation(self.taille_grille[0],self.taille_grille[1],self.taille_pop)
            self.population = nouvelle_population.copy()
            self.grille.afficher(self.population)

            # Défilement des chronons
            self.chronon += 1
            print(self.chronon)
            print()
            time.sleep(0.5)


    def genere_rapport(self):
        """Génère un rapport de données de la simulation
        """
        pass
