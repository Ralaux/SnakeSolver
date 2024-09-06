# SnakeSolver

Solver 0:
Snake fait toujours le même tracé en boucle. 100% de winrate, mais algo le plus lent (et le moins intéressant) possible.  

Solver 1 (Le bot ne gagne pas à tout les coups):
Je commence par juste aller chercher le chemin le plus court.
Puis par dire au serpent de ne pas se rentrer dedans quand il a un autre choix.
Il avance jusqu'au milieu de partie, mais se met tout seul dans des boucles mortelles.
Je me mets alors à créer un algo pour trouver des "iles" : quand il se retrouve face à sa queue, si son corps forme une boucle d'un coté, je le repère et part de l'autre. 
Problème : les murs ne doivent pas être comptés (sinon toutes les cases libres sont dans des boucles), mais du coup l'algo s'enferme dans les coins.
Solution possible : Considérer chaque déplacement comme une sélection de "zone libre" et quantifier ces zones libres pour que le serpent aille chercher la plus grande.

