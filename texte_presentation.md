WA-TOR

Écosystème simulé de requins et poissons

Projet Python en programmation orientée objet

---
Kateryna
---
Équipe :
Objectif du projet

Comment des règles simples font-elles évoluer une population ?

• Simuler les interactions entre poissons et requins.
• Observer l’évolution des populations.
• Modifier les paramètres pour comparer les scénarios.
• Rechercher les conditions favorables à leur coexistence.
Le monde de la simulation

Le monde est une grille composée de cases.

Chaque case contient :
• Un poisson : O
• Un requin : X
• Ou de l’eau : une case vide

Un chronon représente un tour de simulation.

---
Mauro
---
Une grille toroïdale

Les bords opposés de la grille sont reliés.

• Un animal qui dépasse le bord droit réapparaît à gauche.
• Un animal qui dépasse le bord inférieur réapparaît en haut.
• Les déplacements sont uniquement horizontaux ou verticaux.

Le modulo % permet de calculer les coordonnées.

Exemple : (4 + 1) % 5 = 0

---
Benjamin
---
Le comportement des poissons

À chaque chronon, le poisson :

• Observe les quatre cases voisines.
• Choisit une case vide au hasard.
• Se déplace d’une case si une place est disponible.

Temps de reproduction : 3 chronons.

Lors de la reproduction, le bébé reste dans la case de départ du parent.

---
Kateryna
----
Le comportement des requins

Le requin cherche un poisson en priorité.

Examiner les cases voisines dans un ordre aléatoire.
Ignorer les cases occupées par un autre requin.
Mémoriser les cases vides et poursuivre la recherche.
Si un poisson est trouvé, se déplacer et le manger.
Sinon, choisir une case vide avec random.choice().

Si aucune destination n’est disponible, le requin reste sur place.
La gestion de l’énergie

Chaque requin commence avec 5 points d’énergie.

• Un déplacement coûte 1 point.
• Un poisson mangé rend 1 point.
• Un requin immobile ne dépense pas d’énergie.
• À 0 énergie, le requin meurt.

Sans repas : 5 − 1 = 4
Avec repas : 5 − 1 + 1 = 5

La mort se vérifie après le déplacement et le repas.

----
Kateryna
---
La reproduction des requins

Temps de reproduction : 5 chronons.

Pour se reproduire, le requin doit :

• Avoir atteint le temps de reproduction.
• Posséder au moins 1 point d’énergie.
• Avoir effectué un déplacement.
• Laisser une case de départ libre.

Le bébé naît avec 5 points d’énergie.

Il commence à agir au chronon suivant.

---
Mauro
---
L’architecture du programme

POISSON
Position, observation des voisins, déplacement et reproduction.

REQUIN HÉRITE DE POISSON
Chasse, énergie, alimentation, reproduction et mort.

GRILLE
Dimensions du monde et affichage des animaux.

MONDE
Population, chronons et organisation des actions.


---
Mauro
---
Le déroulement d’un chronon

Prendre une copie de la population.
Faire agir chaque animal encore présent.
Gérer ses déplacements, ses repas et sa reproduction.
Retirer immédiatement les animaux mangés ou morts.
Actualiser la grille et avancer le chronon à la fin du tour.

Les nouveau-nés commencent à agir au tour suivant.

---
Kateryna
---
Le travail en équipe

3 personnes et 9 jours de projet

• 1 jour de cours.
• 7 jours de réalisation.
• 1 jour de présentation.

Répartition des responsabilités :

• Grille et monde : [prénom]
• Poissons : [prénom]
• Requins : Kateryna

Git et GitHub permettent de travailler sur des branches et de réunir les contributions.

---
Benjamin
---
Les vérifications à effectuer

• Le requin choisit un poisson avant une case vide.
• Les déplacements respectent les quatre directions autorisées.
• Les animaux peuvent traverser les bords de la grille.
• Chaque déplacement du requin retire un point d’énergie.
• Un repas ajoute un point d’énergie.
• Un animal mangé ou mort ne joue plus.
• Un nouveau-né attend le chronon suivant.

---
Kateryna
---
La démonstration

• Présenter la grille et la population initiale.
• Observer le déplacement d’un poisson et d’un requin.
• Suivre l’énergie du requin avant et après un repas.
• Montrer une naissance et une mort par manque d’énergie.
• Observer l’évolution des effectifs.

Les résultats dépendent des paramètres et des choix aléatoires.

---
Kateryna
----
Bilan et perspectives

Le projet permet de mettre en pratique :

• La programmation orientée objet et l’héritage.
• Les conditions et les boucles imbriquées.
• La gestion des interactions entre objets.
• La collaboration avec Git et GitHub.

Améliorations possibles :

Une interface Pygame, des courbes de population et un export des données.

Merci pour votre attention !