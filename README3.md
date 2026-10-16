# 🐟🦈 Wa-Tor — Simulation proies / prédateurs

> _Phrase d'accroche : une ligne résumant le projet._

![Python](https://img.shields.io/badge/python-3.X-blue) ![Tests](https://img.shields.io/badge/tests-passing-green) ![Licence](https://img.shields.io/badge/licence-MIT-lightgrey)

<!-- Optionnel : capture ou GIF de la simulation -->
<!-- ![Aperçu de la simulation](docs/images/apercu.gif) -->

---

## 📖 Présentation

Wa-Tor est une simulation proies-prédateurs imaginée par A. K. Dewdney (1984). Des poissons et des requins évoluent sur une planète torique : les bords de la grille se rejoignent.

_[1 à 2 phrases : cadre du projet (formation, module) et objectif.]_

---

## 📜 Règles de la simulation

Le temps avance par **chronons**. À chaque chronon, chaque entité joue une fois.

| Entité | Déplacement | Reproduction | Mort |
|---|---|---|---|
| 🐟 Poisson | Case libre adjacente au hasard | Après 3 chronons | Mangé par un requin |
| 🦈 Requin | Priorité à une case contenant un poisson, sinon case libre | Après 10 chronons | Énergie à 0 (−1 par chronon, retour à 3 par poisson mangé) |

---

## 🚀 Installation

**Prérequis :** Python 3.14.4

```bash
git clone https://github.com/Fodba/wa_tor.git
cd wa_tor
python -m venv .venv
source .venv/bin/activate      # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Utilisation

```bash
python main.py
```

### Paramètres

_[Où les modifier : fichier de config, arguments en ligne de commande, constantes.]_

| Paramètre | Description | Valeur par défaut |
|---|---|---|
| _[largeur / hauteur]_ | Dimensions de la grille | 32 / 14 |
| _[TAILLE_POPULATION]_ | Population initiale de poissons et de requins | 300 |
| _[population]_ | Population initiale de poissons et requins | _[…]_ |
| _[temps_de_reproduction]_ | Chronons avant reproduction d'un poisson | 3 |
| _[temps_de_reproduction]_ | Chronons avant reproduction d'un poisson | 10|
| _[energie]_ | Énergie initiale d'un requin | 3 |

---

## 🧩 Architecture

```
wator/
├── classes/
│   ├── __init__.py
│   ├── _[grille.py]_
│   ├── _[poisson.py]_
│   ├── _[requin.py]_
│   └── _[monde.py]_
├── docs/
│   ├── UML/
│   │   └── CU_Monde_Scenario.md
│   │   └── CU_Monde.JPG
│   │   └── CU_Poisson_Scenario.md
│   │   └── CU_Poisson.md
│   │   └── DC.JPG
│   ├── Wa-Tor _ Écosystème Simulé de Requins et Poissons
├── main.py
├── requirements.txt
└── README.md
```

| Classe | Rôle |
|---|---|
| `Grille` | Grille torique, accès aux cases voisines |
| `Poisson` | Classe parente, comportement des proies |
| `Requin` | Comportement des prédateurs |
| `Monde` | Boucle des chronons, statistiques |

Diagramme de classes : ![docs/DC.JPG](./docs/UML/DC.JPG)

---

## ✅ Tests

Les tests ont été réalisés de façon manuelle d'abord pour le développement des comportements et la boucle de simulation.
Puis pour trouver les paramètres de stabilité de la simulation.

---

## 🛠️ Technologies

- Python 3.14.4
- termcolor

---

## 👥 Équipe

| Nom | GitHub |
|---|---|
| Mauro FADIKA | @fodba |
| Benjamin DOCHEZ | @Hoyrax |
| Kateryna VORONINA | @mail4kkate-droid |

---
