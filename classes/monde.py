from classes.poisson import Poisson
from classes.grille import Grille
from classes.requin import Requin
import time
import random as r

# Classe gérant la simulation
class Monde:
    def __init__(self, largeur: int, hauteur: int, taille_pop: int) -> None:
        self.population = [] # Liste des entités (poisson et requin) présents sur la grille
        self.chronon = 0 #
        self._largeur = largeur
        self._hauteur = hauteur
        self._ratio_pop_totale: int = 0
        self._ratio_shark_poisson: int = 0
        self.taille_pop = taille_pop
        self.initialisation(largeur, hauteur, taille_pop)

    def initialisation(self, largeur: int, hauteur: int, quantite_pop: int) -> None:
        self.taille_grille = (largeur, hauteur)
        self.grille = Grille(largeur, hauteur)
        self.population: list[Poisson] = []

        if quantite_pop > largeur * hauteur:
            raise ValueError("Il y a plus d'animaux que de cases disponibles.")

        for i in range(quantite_pop):
            while True:
                x = r.randint(0, self.taille_grille[0] - 1)
                y = r.randint(0, self.taille_grille[1] - 1)

                case_occupee = any(
                    animal.position_X == x and animal.position_Y == y
                    for animal in self.population
                )

                if not case_occupee:
                    break

            if r.randint(0, 10) == 0:
                temps_reproduction_requin = 10
                nouveau_requin = Requin(x, y, temps_reproduction_requin)
                self.population.append(nouveau_requin)
            else:
                temps_reproduction_poisson = 3
                nouveau_poisson = Poisson(x, y, temps_reproduction_poisson)
                self.population.append(nouveau_poisson)

        self.grille.afficher(self.population)

  
    def boucle(self):
        continuer = True

        while continuer:
            nouvelle_population = self.population.copy()
            count = 1

            for animal in self.population.copy():

                # print(type(animal))
                print(f"compteur d'animaux: {count}")

                result = animal.mouvement(
                    grille=self.grille,
                    population=nouvelle_population
                )

                if isinstance(result, Poisson) and not isinstance(result, Requin):
                    nouvelle_population.append(result)

                count += 1

            # Affichage de la population
            # print(f"nouvelle population : {nouvelle_population}")
            self.population = nouvelle_population.copy()
            self.grille.afficher(self.population)

            # Défilement des chronons
            self.chronon += 1

            nombre_poissons = sum(
                1 for animal in self.population
                if isinstance(animal, Poisson)
                and not isinstance(animal, Requin)
            )

            nombre_requins = sum(
                1 for animal in self.population
                if isinstance(animal, Requin)
            )

            print(f"Chronon : {self.chronon}")
            print(f"Poissons : {nombre_poissons}")
            print(f"Requins : {nombre_requins}")
            print()

            if nombre_poissons == 0 or nombre_requins == 0:
                print(f"Fin de la coexistence au chronon {self.chronon}")
                continuer = False

            time.sleep(0.5)

    def genere_rapport(self):
        """Génère un rapport de données de la simulation
        """
        pass