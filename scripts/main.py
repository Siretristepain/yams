import logging
import random

logger = logging.getLogger("__name__")
logging.basicConfig(filename='./logs/yams.log', level=logging.DEBUG, encoding='utf-8')

def show_dices(dices: list):
    """
    Méthode utilisée pour afficher le plateau avec les 5 dés.
    Vérifie s'il y a bien 5 dés dans la liste.

    Args :
        dices (list): la liste contenant les valeurs des 5 dés à afficher.
    
    Returns:
        to_show (str): les 5 dés affichés.
    """

    logger.debug("Affichage du plateau...")

    # Vérification du nombre de dés
    if len(dices) != 5:
        logger.critical('Il y a plus de 5 dés dans la méthode show_dices')
        raise ValueError(f"5 éléments sont attendus dans la liste. Il y en a {len(dices)}.")

    # Afficher les dés
    to_show = f"""
_____________________
|   |   |   |   |   |
| {dices[0]} | {dices[1]} | {dices[2]} | {dices[3]} | {dices[4]} |
|   |   |   |   |   |
_____________________
"""

    return to_show


def throw_a_dice():
    """
    Méthode utilisée pour lancer 1 dés.

    Returns:
        int: Valeur obtenue par le lancer.
    """

    logger.debug("Lancer d'un dés...")
    return random.randint(1,6)

def choices(turn: int):
    """
    Méthode utilisée pour afficher les différentes options possibles au joueur en cours.
    Se sert de la variable 'turn' en argument pour savoir si le joueur peut encore lancer les dés ou non.

    Args:
        turn (int): le tour du jouer en cours (de 1 à 3).
    """

    choice = input(f"""
Que souhaitez vous faire :

(1) Lancer les 5 dés {'X' if turn >= 3 else ''}
(2) Relancer certains dés {'X' if turn >= 3 else ''}
(3) Conserver {'X' if turn == 0 else ''}
(4) Consulter la fiche de score
(q) Quitter

Votre choix :
""")

    if choice not in ["1", "2", "3", "4", "q"]:
        logger.error(f"L'action {choice} n'est pas une action valide.")
        print(f"Veuillez saisir une action valide.")
        choices(turn=turn)

    # Gestion des choix invalides selon le tour
    if turn == 0 and choice == "3":
        logger.debug("Le joueur souhaite conserver sans avoir lancer les dés.")
        print(f"Vous ne pouvez pas conserver sans avoir lancer les dés.")
        choices(turn=turn)
    elif turn >= 3 and (choice == "1" or choice == "2"):
        logger.debug("Le joueur souhaite relancer les dés malgré ses 3 tentatives.")
        print("Vous avez déjà lancer les dés 3 fois.")
        choices(turn=turn)

    return choice

def main():

    # Demander le nombre de joueur
    while True:
        nb_players = input(f"Nombre de joueur : ")
        try:
            nb_players = int(nb_players)
            logger.debug(f"Nombre de joueurs : {nb_players}")
            break

        except ValueError:
            logger.error(f"Le format du nombre de joueur n'est pas correct : {nb_players}.")
            print(f"Le nombre de joueur attendus doit être un entier positif.")

    # On initialise une variable pour identifier le tour
    turn = 1

    # Afficher les différentes options
    logger.debug("Affichage des options...")
    choice = choices(turn=turn)
    logger.debug(f"Le joueur à choisis l'option : {choice}.")

# a = print(show_dices(dices=[1,2,3,4,5]))
main()
# print(choices())