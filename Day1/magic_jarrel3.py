import random

print("Bienvenue dans le jeu !")

# choix du paramétrage/niveau de difficulté
level = int(input("Ecrit 1: facile, 2:moyen, 3:difficile \n"))

# generation des serpents en fonction du level sans boucle
'''
    snakes = ['S'] * level
    listOfKeys = ['K'] * (5 - level)
    jars = snakes + listOfKeys
    random.shuffle(jars)
'''

# compteur de clés magiques
keys = 0

# répeter les manches de notre jeu
while keys != 3:
    print("Vous disposez de 5 jarres devant vous, choisissez entre 1, 2, 3, 4 ou 5")

    # tableau qui va contenir chacune des jarres
    jars = ['K', 'K', 'K', 'K', 'K']

    # boucle qui va tourner autant de fois qu'il doit y avoir de serpents
    for i in range(0, level):
        jars[i] = 'S'

    # melanger la liste
    random.shuffle(jars)

    # demande à notre joueur de mettre une valeur
    choix = int(input())

    print(f"Le joueur a mis dans la jarre n°{choix}")

    if choix < 1 and choix > 5:
        choix = int(input("Veuillez saisir un nombre valide"))

    # verification
    if jars[choix-1] == 'K': # gagné
        keys += 1
        print(f"Gagné ! Vous obtenez une clé magique ! Voici les jarres : {jars}")
        print(f"Vous avez {keys}/3 clés")
    else:
        print("Perdu ! Un serpent apparaît !")

        # si le joueur n'a pas de clé
        if keys > 0:
            keys -= 1
        print(f"Vous avez {keys}/3 clés")

print("Vous devenez Roi du temple !")