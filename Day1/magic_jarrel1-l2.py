import random

print("Bienvenue dans le jeu !")

# compteur de clés magiques
keys = 0

# répeter les manches de notre jeu
while keys != 3:
    print("Vous disposez de 5 jarres devant vous, choisissez entre 1, 2, 3, 4 ou 5")

    # choix aléatoire qui fait perdre notre joueur
    snake_jar = random.randint(1, 5) 

    # demande à notre joueur de mettre une valeur
    choix = int(input())

    print(f"Le joueur a mis dans la jarre n°{choix}")

    if choix < 1 and choix > 5:
        choix = int(input("Veuillez saisir un nombre valide"))

    # verification
    if choix != snake_jar: # gagné
        keys += 1
        print(f"Gagné ! Vous obtenez une clé magique ! La jarre infectée était le n°{snake_jar}")
        print(f"Vous avez {keys}/3 clés")
    else:
        print("Perdu ! Un serpent apparaît !")

        # si le joueur n'a pas de clé
        if keys > 0:
            keys -= 1
        print(f"Vous avez {keys}/3 clés")

print("Vous devenez Roi du temple !")