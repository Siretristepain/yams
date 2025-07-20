# yams

## Présentation
Dépôt pour developper une version simple du jeu de Yams en Python.
Le **Yams** (aussi connu sous le nom de **Yahtzee**) est un jeu de dés, alliant hasard et un peu de stratégie.
Le but et de réaliser toute une liste de combinaisons avec 5 dés et d'obtenir le plus grand résultat total.
Le jeu se joue donc à un joueur comme à plusieurs.

## Règles du jeu

Les joueurs jouent chacun leur tour.
Le tour de jeu d'un joueur se compose de 3 lancers de dés, sachant que les 2ème et 3ème lancers sont optionnels.
C'est à dire que si après avoir lancer une première fois ses dés, un joueur est satisfait de son lancer, il n'est pas obligé de faire son second et son troisième lancer.

Après avoir fait sa phase de lancer de dés, le joueur doit déclarer la case qu'il souhaite remplir sur la feuille de score.

En effet, une feuille de score permet de suivre l'avancée de la partie.

La feuille de score est composée de 2 tableaux : un tableau supérieur et un tableau inférieure.

Le premier (supérieur), présente 6 lignes : la ligne des 1, la ligne des 2, la ligne des 3, ..., jusqu'à la ligne des 6.
Dans ce tableau, le but est de faire un maximum de dés sur la face 1, une maximum de dés sur la face 2, un maximum de dés sur la face 3,..., jusqu'à un maximum de dés sur la phase 6. Si le score cumulés de ces 6 lignes fait 63 ou plus, un bonus de 35 points est accordé au joueur.

Le second tableau présente différentes combinaisons à réaliser avec les 5 dés à faire au cours de la partie. Certaines combinaisons confèrent un nombre de point prédéterminé tandis que pour d'autre, il faut sommer les 5 faces des dés. Les différentes combinaisons sont les suivantes :

- **Brelan** : trois dés sur la même face. Le score corresponds à la somme des 5 dés. Ainsi, un brelan de 1 confère toujours moins de points qu'un brelan de 6.
- **Carré** : quatre dés sur la même face. Le score corresponds à la somme des 5 dés. Ainsi, un carré de 1 confère toujours moins de points qu'un carré de 6.
- **Full** : un brelan + une paire, c'est à dire 3 dés identiques + 2 dés identiques. Le score du full est toujours de 25 points.
- **Petite suite** : 4 dés qui se suivent. Le score de la petite suite est toujours de 30 points.
- **Grande suite** : 5 dés qui se suivent. Le score de la grande suite est toujours de 40 points.
- **Yams** (ou Yahtzee) : 5 dés identiques. Le score du Yams est toujours de 50 points.
- **Chance** : aucune combinaison particulière. Le score corresponds à la somme des 5 dés.

**Important** : À chaque tour de jeu, le joueur doit obligatoirement remplir une case de sa colonne sur la feuille de score. Ainsi, puisqu'il y a 13 cases sur la feuille de score, une partie de Yams dure forcément 13 tours.

Si après avoir réaliser ses 3 lancers, un joueur ne peut réaliser aucune combinaison, il peut choisir de "barrer" une combinaison. C'est à dire qu'on inscrit une croix dans la combinaison souhaitée et que le joueur ne pourra plus la réaliser de la partie.

Un joueur peut également décider de "barrer" une combinaison s'il n'est pas satisfait de ses lancers alors qu'il pourrait réaliser une combinaison. Ainsi, un joueur pourrait choisir de barrer toutes ses cases s'il veut. Ainsi, le plus petit score réalisable au Yams est 0. Le maximum est 375.

Pour calculer le score total, on calcule les scores des 2 tableaux (en faisant bien attention au bonus du 1er tableau) puis on somme ces 2 totaux pour former le total final.

Le joueur avec le plus grand total final gagne la partie.
