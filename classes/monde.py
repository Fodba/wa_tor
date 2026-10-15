import matplotlib.pyplot as plt
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
        self.historique_chronons = []
        self.historique_poissons = []
        self.historique_requins = []
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

    #def check_reproduction(self, poisson: Poisson, reproduction_time: int):
        # Vérifie si le temps de reproduction est écoulé pour le poisson
        #if poisson.compteur_reproduction >= reproduction_time:
           # return True
        #else:
            #return False

    def action_poisson(self, poisson: Poisson):
        # le poisson observe son environnement
        # le poisson évalue sa destination
        # le poisson se déplace
        return poisson.mouvement(
            grille=self.grille, population=self.population
        )

    def boucle(self):
        continuer = True

        # Enregistrer la population initiale au chronon 0.
        self.compter_population()

# Activer la mise à jour du graphique pendant la simulation.
        plt.ion()
        figure, axes = plt.subplots()

        while continuer:
            nouvelle_population = self.population.copy()
            count = 1

            for animal in self.population.copy():
                if animal not in nouvelle_population:
                    continue

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


                        # Enregistrer les effectifs du tour terminé.
            self.compter_population()

            # Redessiner les deux courbes.
            axes.clear()

            axes.plot(
                self.historique_chronons,
                self.historique_poissons,
                label="Poissons",
                color="teal"
            )

            axes.plot(
                self.historique_chronons,
                self.historique_requins,
                label="Requins",
                color="coral"
            )

            axes.set_title("Évolution des populations")
            axes.set_xlabel("Chronons")
            axes.set_ylabel("Nombre d'animaux")
            axes.set_ylim(bottom=0)
            axes.legend()
            axes.grid(True)

            plt.pause(0.01)

            if nombre_poissons == 0 or nombre_requins == 0:
                print(f"Fin de la coexistence au chronon {self.chronon}")
                continuer = False

            time.sleep(0.5)

                    # Garder le graphique ouvert après la simulation.
        plt.ioff()
        plt.show()

    def compter_population(self) -> None:
        """Compte les poissons et les requins au chronon actuel."""

        nombre_poissons = 0
        nombre_requins = 0

        for animal in self.population:

            # Vérifier Requin avant Poisson, car Requin hérite de Poisson.
            if isinstance(animal, Requin):
                nombre_requins += 1

            elif isinstance(animal, Poisson):
                nombre_poissons += 1

        # Enregistrer les résultats après le comptage.
        self.historique_chronons.append(self.chronon)
        self.historique_poissons.append(nombre_poissons)
        self.historique_requins.append(nombre_requins)       

def genere_rapport(self):
    """Génère un rapport de données de la simulation
    """
    pass