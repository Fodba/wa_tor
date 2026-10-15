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
| 🐟 Poisson | Case libre adjacente au hasard | Après _[N]_ chronons | _[Mangé par un requin]_ |
| 🦈 Requin | Priorité à une case contenant un poisson, sinon case libre | Après _[N]_ chronons | Énergie à 0 (−1 par chronon, +_[N]_ par poisson mangé) |

---

## 🚀 Installation

**Prérequis :** Python _[3.X]_

```bash
git clone _[URL_DU_DEPOT]_
cd wator
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
| _[largeur / hauteur]_ | Dimensions de la grille | _[…]_ |
| _[nb_poissons]_ | Population initiale de poissons | _[…]_ |
| _[nb_requins]_ | Population initiale de requins | _[…]_ |
| _[repro_poisson]_ | Chronons avant reproduction d'un poisson | _[…]_ |
| _[repro_requin]_ | Chronons avant reproduction d'un requin | _[…]_ |
| _[energie_requin]_ | Énergie initiale d'un requin | _[…]_ |
| _[nb_chronons]_ | Durée de la simulation | _[…]_ |

---

## 🧩 Architecture

```
wator/
├── src/
│   ├── __init__.py
│   ├── _[planete.py]_
│   ├── _[poisson.py]_
│   ├── _[requin.py]_
│   └── _[simulation.py]_
├── tests/
│   └── _[test_*.py]_
├── docs/
│   └── _[diagramme_classes.png]_
├── main.py
├── requirements.txt
└── README.md
```

| Classe | Rôle |
|---|---|
| `_[Planete]_` | _[Grille torique, accès aux cases voisines]_ |
| `_[Poisson]_` | _[Comportement des proies]_ |
| `_[Requin]_` | _[Comportement des prédateurs]_ |
| `_[Simulation]_` | _[Boucle des chronons, statistiques]_ |

Diagramme de classes : [docs/diagramme_classes.png](docs/diagramme_classes.png)

---

## ✅ Tests

```bash
pytest -v
```

_[Optionnel : couverture avec `pytest --cov=src` — X %]_

---

## 🛠️ Technologies

- Python _[3.X]_
- _[pygame / tkinter / matplotlib / affichage console]_ pour la visualisation
- _[pytest / unittest]_ pour les tests

---

## 👥 Équipe

| Nom | GitHub |
|---|---|
| _[Prénom Nom]_ | _[@pseudo]_ |
| _[Prénom Nom]_ | _[@pseudo]_ |

---

## 📄 Licence

_[MIT / autre]_
