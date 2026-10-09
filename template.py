# Classe représentant un poisson dans la grille
class Fish:
    def __init__(
            self, 
            position_x: int, 
            position_y: int, 
            reproduction_time: int
        ) -> None:
        pass


# Classe représentant un requin, hérite des caractéristiques de Fish
class Shark(Fish):
    def __init__(
            self, 
            position_x: int, 
            position_y: int, 
            reproduction_time: int, 
            starvation_time: int
        ) -> None:
        pass


# Classe représentant la grille de la simulation
class Grid:
    def __init__(self, size: int) -> None:
        pass


# Classe gérant la simulation
class World:
    def __init__(self, grid: Grid) -> None:
        pass
