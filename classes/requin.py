import random as r #pour avoir la direction aléatoire

from classes.poisson import Poisson



# Classe représentant un requin, qui hérite de Poisson
class Requin(Poisson):
    def __init__(
            self,
            position_x: int,
            position_y: int,
            temps_reproduction: int = 5
        ) -> None:

        # Récupérer les attributs communs de Poisson
        super().__init__(
            position_x,
            position_y,
            temps_reproduction
        )

        self.image = "X"
        self.just_born = True

        # Chaque requin commence avec 5 points d'énergie
        self.energie = 8

        # Compter les chronons depuis la dernière reproduction
        self.compteur_reproduction = 0

    def perte_energie(self) -> None:
        """Retire un point d'énergie après un déplacement."""

        self.energie -= 1

    def recuperation_energie(self) -> None:
        """Ajoute un point d'énergie après un repas."""

        self.energie += 1

    def mourir(self, population: list[Poisson]):
        """Retire le requin si son énergie est égale à zéro."""

        if self.energie == 0:

            if self in population:
                population.remove(self)

            return True

        else:
            return False

    def manger(
            self,
            poisson: Poisson,
            population: list[Poisson]
        ) -> None:
        """Supprime le poisson mangé et récupère un point d'énergie."""

        # Le déplacement est déjà effectué dans mouvement().
        # Ne pas retirer un deuxième point d'énergie ici.
        population.remove(poisson)

        self.recuperation_energie()

    def se_reproduire(
            self,
            ancien_x: int,
            ancien_y: int,
            population: list[Poisson]
        ) -> None:
        """Crée un nouveau requin dans la case de départ du requin-parent."""

        # Vérifier si le temps de reproduction est arrivé
        if self.compteur_reproduction < self.temps_reproduction:
            return

        # Le parent doit être vivant pour se reproduire.
        if self.energie < 1:
            return

        # Vérifier que la case de départ est libre.
        for animal in population:
            if (
                animal.position_X == ancien_x
                and animal.position_Y == ancien_y
            ):
                return

        # Créer un nouveau requin : son énergie sera automatiquement égale à 5.
        nouveau_requin = Requin(
            ancien_x,
            ancien_y,
            self.temps_reproduction
        )
        # nouveau_requin.image = "P"

        population.append(nouveau_requin)

        # Recommencer le compteur après la naissance.
        self.compteur_reproduction = 0

        return nouveau_requin

    def mouvement(
            self, 
            direction=None, 
            grille=None, 
            population=None,
            nouvelle_population=None
        ):
        """Cherche un poisson en priorité, sinon une case vide."""
        # print("mouvement")


        # if self.just_born:
        #     print("just born")
        #     self.just_born = False
        #     return
        # else:
            # self.image = "X"
        
        # Le monde doit fournir la grille et sa liste d'animaux.
        if grille is None or population is None:
            print("grille is None")
            # print(grille)
            # print(population)
            return False

        # Un animal rétiré ne bouge plus
        if self not in population:
            print("self not in population")
            return False

        # À zéro énergie, le requin meurt.
        if self.energie == 0:
            self.mourir(population)
            
            print("self.mourir")
            return False

        # Avec un point le requin peut se déplacer
        if self.energie >= 1:
            print("self.energie >=1")

            # Un appel correspond à un chronon.
            self.compteur_reproduction += 1

            # Utiliser regarder(), hérité de Poisson.
            haut, bas, gauche, droite = self.regarder(grille)

            # Préparer la liste des cases
            cases_voisines = []
            # cases_voisines = [haut, bas, gauche, droite]

            for case in [haut, bas, gauche, droite]:

                # Ne pas ajouter sa propre case.
                if case != (self.position_X, self.position_Y):
                    if case not in cases_voisines:
                        cases_voisines.append(case)

            # Chaque case sera vérifiée une seule fois dans un ordre aléatoire
            r.shuffle(cases_voisines)

            cases_vides = []
            destination = None
            poisson_trouve = None

            # Boucle for pour examiner les cases 
            for x, y in cases_voisines:

                requin_present = False
                poisson_case = None

                # Boucle for pour vérifier qui est dans la case
                for animal in population:

                    if (
                        animal.position_X == x
                        and animal.position_Y == y
                    ):

                        # Vérifier Requin avant Poisson,car Requin hérite de Poisson.
                        if isinstance(animal, Requin):
                            requin_present = True

                        elif isinstance(animal, Poisson):
                            poisson_case = animal
                            break

                # Une autre requin bloque la case.
                if requin_present:
                    print("requin présent")
                    continue

                # Si un poisson est dans la case choisir cette case
                if poisson_case is not None:
                    poisson_trouve = poisson_case
                    destination = (x, y)
                    # print("poisson présent")
                    break

                else:
                    # print("case vide")
                    # si la case est vide  la mémoriser et continuer à chercher un poisson
                    cases_vides.append((x, y))

            # Si un poisson n'est pas trouvé choisir une case vide.
            if destination is None:

                if len(cases_vides) > 0:
                    destination = r.choice(cases_vides)
                    # print(f"cases vides: {cases_vides}")
                    # print(f"destination: {destination}")

                else:
                    # Toutes les cases sont bloquées.
                    # Aucun déplacement, aucune perte d'énergie.
                    # La reproduction attend.
                    return False

            # Garder les coordonnées de départ pour un nouveau requin
            ancien_x = self.position_X
            ancien_y = self.position_Y

            # Se déplacer d'une seule case.
            self.position_X = destination[0]
            self.position_Y = destination[1]

            # Chaque déplacement diminue énergie
            self.perte_energie()

            # Si la destination contient un poisson, le manger.
            if poisson_trouve is not None:
                self.manger(poisson_trouve, population)

            # Vérifier la mort après le déplacement et le repas.
            if self.mourir(population):
                return True
            # else:
            #     nouvelle_population.append(self)

            # Le parent vivant peut laisser un noveau requin dans sa case de départ.
            # nouvelle_population.append(self.se_reproduire(ancien_x, ancien_y, population))
            self.se_reproduire(ancien_x, ancien_y, population)


            print(f"energie : {self.energie}")
            print(f"temps de reproduction : {self.temps_reproduction}")
            # print(f"nouvelle population : {nouvelle_population}")

            return True

        else:
            print("energie epuisee")
            return False