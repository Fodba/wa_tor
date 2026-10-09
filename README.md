## Points à trancher

* Toutes les valeurs des paramètres ne sont pas fixés définitivement et évolueront en fonction des simulations


## Points validés

* La langue utilisée pour nommer les variables et les fonctions est le français.
* Les paramètres sont réglables pendant la simulation grace à des boutons (pour l'interface graphique)
* Au lancement du programme, seul les poissons peuvent se reproduire une fois atteint le temps de reproduction.
* Les requins ne démarrent leur reproduction qu'après un certains temps (ex: après 5 chronons).
* La reproduction est gérée par les entités (Poisson, Requin)
* Le world organise le déroulement d'un tour.
* Un tour/chronon correspond au temps qu'il faut pour que chaque entité effectue son action sur la grille
* Les déplacements se font uniquement sur les axes horizontaux et verticaux, une case par tour (selon les conditions de l'entité)
* les déplacements sont gérés par les entités (Poisson, Requin)
* Le déplacement des poissons ne se font que si une case vide est disponible
* La quantité d'énergie est pour les requins.
* Les temps de reproduction est fixé en chronons pour les poissons et pour les requins s'ils ont assez d'énergie


## Paramètres réglables

* Temps de reproduction (requin et poisson)
* Taille de la grille
* Proportion d'espèces/grille (taille de la population)
* Répartition des espèces (Poisson/Requin)
* La durée d'un chronon / Vitesse de la simulation
* L'énergie gagné par la consommation d'un poisson
* L'énergie des requins (fixé par défaut à 5)
* Les temps de reproduction des 2 espèces (fixé par défaut à 3 pour les poissons, à 5 pour les requins)