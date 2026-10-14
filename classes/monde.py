from classes.poisson import Poisson
from classes.grille import Grille
from classes.requin import Requin
import time
import random as r


# Classe gérant la simulation
class Monde:
    def __init__(self,largeur:int,hauteur:int, taille_pop: int) -> None:
        self.population = [] # Liste des entités (poisson et requin) présents sur la grille
        self.chronon = 0 # 
        self._largeur = largeur
        self._hauteur = hauteur
        self._ratio_pop_totale: int = 0
        self._ratio_shark_poisson: int = 0
        self.taille_pop = taille_pop
        self.initialisation(largeur,hauteur,taille_pop)


    def initialisation(self, largeur: int, hauteur: int, quantite_pop: int) -> None:
        self.taille_grille = (largeur,hauteur)
        self.grille = Grille(largeur,hauteur)
        self.population: list[Poisson] = []
        for i in range(quantite_pop):
            x = r.randint(0,self.taille_grille[0]-1)
            y = r.randint(0,self.taille_grille[1]-1)
            if r.randint(0,10) == 0:
                temps_reproduction_requin = 5
                nouveau_requin = Requin(x,y,temps_reproduction_requin)
                self.population.append(nouveau_requin)
            else:
                temps_reproduction_poisson = 3
                nouveau_poisson = Poisson(x,y,temps_reproduction_poisson)
                self.population.append(nouveau_poisson)

    
    def check_reproduction(self,poisson: Poisson, reproduction_time: int):
        # Vérifie si le temps de reproduction est écoulé pour le poisson
        if poisson.temps_reproduction == 0:
            return True
        else: 
            return False


    def boucle(self):
        continuer = True

        while continuer:
            nouvelle_population = self.population.copy()
            count = 1
            for animal in self.population:
                animal.mouvement(grille = self.grille,population=nouvelle_population)
                count += 1

            # Affichage de la population
            self.population = nouvelle_population.copy()
            self.grille.afficher(self.population)

            # Défilement des chronons
            self.chronon += 1
            print(self.chronon)
            time.sleep(0.5)
