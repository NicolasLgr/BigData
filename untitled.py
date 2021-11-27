# tous les imports de ce TD devront être placés ici
import random
import time

import string


# le mot à trouver
target = "Hello World"

#résultat 11
test = "Hemlo Wohld"
#resultat 105
test2 = "COjsy OfUkp"

#return [105, 11] the best is 11
listeMot = ["COjsy OfUkp", "Hemlo Wohld", "AZERT ERTYF","ZdRfT ERfcd","azEdC Ujnmo"]

nbIteration = 0

# la fonction de conversion dune chaîne de caractères en liste de valeurs ASCII vous est founie
def string_to_int_list(string):
    return [ord(character) for character in list(string)]


def get_distance(string1, string2):
    
    distance =0 
    index = 0
    distanceB = 0
    int1 = string_to_int_list(string1)
    int2 = string_to_int_list(string2)
    
    for number in int1:
        distanceB = abs(int1[index] - int2[index])
        distance += distanceB
        index += 1
    
    return distance


def get_best(string, listeCompare):
    
    listeDistance = []
    
    for listeNombre in listeCompare:
        listeDistance.append(get_distance(string,listeNombre))
        
    minDistance = min(listeDistance)
    mot = listeCompare[listeDistance.index(minDistance)]
            
    return mot, minDistance


# Fonction qui renvoie une liste de mots
# prends en paramêtre le nombre de mot que doit contenir la liste
def word_list_init(nombreDeMot, lettre):
 
    listeMot = []
    
    # genere 5 lettres aléatoire, fait un espace et regènère 5 lettres aléatoire
    # le nombre de fois qui est demandé par la fonction passé en paramètre
    for iteration in range(nombreDeMot):
        listeMot.append(''.join(
                                random.choice(string.ascii_letters) 
                                for index in range(lettre)))
    return listeMot

#change une liste ascii en mot
def ascii_to_lettre(asciiListe):
    return ''.join(chr(i) for i in asciiListe)


def crossover(string1, string2):
        
    string1Int = string_to_int_list(string1)
    string2Int = string_to_int_list(string2)
    
    enfant = []
    
    string1Length = len(string1Int)
    
    for i in range(string1Length):
        choice = random.randint(0,1)
        if choice == 1: 
            enfant.append(string1Int[i])
        else: 
            enfant.append(string2Int[i])
    
    return enfant
    
def new_generation(target, maListe):
    newGeneration = []
    bestDistance = get_best(target, maListe)
    
    #indique le meilleur mot avec sa distance
    print("     Mot :",bestDistance[0], "distance : ",bestDistance[1] )
    
    lenMaListe = len(maListe)
    
    #Ajoute le mot qui a la meilleur distance au tableau newGeneration
    newGeneration.append(bestDistance[0])
    bestWord = bestDistance[0]
    
    if bestWord == target:        
        return "solution trouvé en", nbIteration, "iterations"        
    else:  
        maListe.pop(maListe.index(bestWord))

        while len(newGeneration) != lenMaListe:
            randomWord1 = random.choice(maListe)
            randomWord2 = random.choice(maListe)
            newEnfant = crossover(bestWord, randomWord2)
            newEnfant = mutation(newEnfant)
            newGeneration.append(ascii_to_lettre(newEnfant))

        maListe = newGeneration
        
        return maListe

def mutation(motAscii):
    tailleMot = len(motAscii)
    
    choice = random.randint(0,tailleMot)
    bestDistance = get_distance(target, ascii_to_lettre(motAscii))

    if bestDistance >= 500:
        randomNumber = random.randint(-100,100)
        motAscii[choice]  = (randomNumber + motAscii[choice])%255 
    elif bestDistance >= 100:
        randomNumber = random.randint(-12,12)
        motAscii[choice]  = (randomNumber + motAscii[choice])%255 
    elif bestDistance > 20:
        randomNumber = random.randint(-3,3)
        motAscii[choice]  = (randomNumber + motAscii[choice])%255 
    else:
        randomNumber = random.randint(-1,1)
        motAscii[choice] = (randomNumber + motAscii[choice])%255 
                
    return motAscii

# test_length = 20
# # target = "Hello World"
# target = "".join([chr(random.randint(0, 255)) for _ in range(test_length)])
# print("target : ",target)

# listeInit = word_list_init(100, len(target))
# start = time.time()

# print("iteration n°" ,nbIteration)
# newGeneList = new_generation(target, listeInit)
# bestWord = get_best(target, newGeneList)[0]
# bestDistance = get_best(target,newGeneList)[1]

# while bestWord != target:
#     nbIteration += 1
#     print("iteration n°",nbIteration)
#     newGeneList = new_generation(target, newGeneList)
#     bestWord = get_best(target, newGeneList)[0]
#     bestDistance = get_best(target,newGeneList)[1]

# end = time.time() - start
# print(end)


# # La cible est :
# #/\     /\
# #  \ _____\
#   (_)-(_)
ascii_target="/\     /\   \ _____\   (_)-(_)"
listeInit = word_list_init(200, len(target))

# print("iteration n°" ,nbIteration)

# newGeneList = new_generation(target, listeInit)
# bestWord = get_best(target, newGeneList)[0]
# bestDistance = get_best(target,newGeneList)[1]

# while bestWord != target:
#     nbIteration += 1
#     print("iteration n°",nbIteration)
#     newGeneList = new_generation(target, newGeneList)
#     bestWord = get_best(target, newGeneList)[0]
#     bestDistance = get_best(target,newGeneList)[1]



def printer_ascii(indiv, length):
    tab_print = [indiv[i*length:(i*length)+length] for i in range(int(len(indiv)/length))]
    for line in tab_print:
        print("".join(chr(c) for c in line))

# listeAscii = printer_ascii(ascii_target, len(ascii_target))

asciiListInt = string_to_int_list(ascii_target)
lentgh = len(asciiListInt)
for i in range(lentgh):
    if asciiListInt[i] % lentgh == 0:
        asciiListInt[i].append(11)

print(asciiListInt)
asciiLettre = ascii_to_lettre(asciiListInt)
print(asciiLettre)