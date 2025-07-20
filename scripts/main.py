import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='./logs/yams.log', level=logging.DEBUG, encoding='utf-8')

def show_dice(dices: list):
    logger.debug('Début méthode show_dice')
    # Vérification du nombre de dés
    if len(dices) != 5:
        pass

a = show_dice(dices=[1,2,3,4,5])