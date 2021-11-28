# tous les imports de ce TD devront être placés ici
import random
import time
import numpy as np
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
    print("le meilleur mot est :", mot,"avec une distance de:",minDistance) 
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
    lenMaListe = len(maListe)
    
    #Ajoute le mot qui a la meilleur distance au tableau newGeneration
    for i in range(5):
        bestDistance = get_best(target, maListe)
        bestWord = bestDistance[0]
        newGeneration.append(bestWord)
        maListe.pop(maListe.index(bestWord))

    while len(newGeneration) != lenMaListe:
        random = np.random.choice(np.arange(0, 5), p=[0.5, 0.25, 0.15, 0.05, 0.05])
        if random == 0:
            randomWord1 = newGeneration[0]
            randomWord2 = newGeneration[0]
            newEnfant1 = crossover(randomWord1, randomWord2)
            test = newEnfant1
            newEnfant2 = mutation(newEnfant1)
            newGeneration.append(ascii_to_lettre(newEnfant2))
        elif random == 1:
            randomWord1 = newGeneration[0]
            randomWord2 = newGeneration[1]
            newEnfant1 = crossover(randomWord1, randomWord2)
            test = newEnfant1
            newEnfant2 = mutation(newEnfant1)
            newGeneration.append(ascii_to_lettre(newEnfant2))
        elif random == 2:
            randomWord1 = newGeneration[1]
            randomWord2 = newGeneration[2]
            newEnfant1 = crossover(randomWord1, randomWord2)
            test = newEnfant1
            newEnfant2 = mutation(newEnfant1)
            newGeneration.append(ascii_to_lettre(newEnfant2))
        elif random == 3:
            randomWord1 = newGeneration[2]
            randomWord2 = newGeneration[3]
            newEnfant1 = crossover(randomWord1, randomWord2)
            test = newEnfant1
            newEnfant2 = mutation(newEnfant1)
            newGeneration.append(ascii_to_lettre(newEnfant2))
        elif random == 4:
            randomWord1 = newGeneration[3]
            randomWord2 = newGeneration[4]
            newEnfant1 = crossover(randomWord1, randomWord2)
            test = newEnfant1
            newEnfant2 = mutation(newEnfant1)
            newGeneration.append(ascii_to_lettre(newEnfant2))

    return newGeneration

def mutation(motAscii):
    tailleMot = len(motAscii)
    
    for i in range(tailleMot):
        choice = random.randint(0,5)
        if choice == 3:
            if get_distance(target,ascii_to_lettre(motAscii)) >= 100:
                randomNumber = random.randint(-10,10)
                motAscii[i] = (randomNumber + motAscii[i])%255 
            if get_distance(target,ascii_to_lettre(motAscii)) >= 60:
                randomNumber = random.randint(-6,6)
                motAscii[i] = (randomNumber + motAscii[i])%255 
            elif get_distance(target,ascii_to_lettre(motAscii)) >= 40:
                randomNumber = random.randint(-5,5)
                motAscii[i] = (randomNumber + motAscii[i])%255 
            elif get_distance(target, ascii_to_lettre(motAscii)) >= 30:
                randomNumber = random.randint(-4,4)
                motAscii[i] = (randomNumber + motAscii[i])%255 
            elif get_distance(target, ascii_to_lettre(motAscii)) >= 20:
                randomNumber = random.randint(-3,3)
                motAscii[i] = (randomNumber + motAscii[i])%255 
            elif get_distance(target, ascii_to_lettre(motAscii)) >= 10:
                randomNumber = random.randint(-2,2)
                motAscii[i] = (randomNumber + motAscii[i])%255 
            elif get_distance(target, ascii_to_lettre( motAscii)) < 10:
                randomNumber = random.randint(-1,1)
                motAscii[i] = (randomNumber + motAscii[i])%255 
        
    return motAscii

test_length = 32
target = "".join([chr(random.randint(0, 255)) for _ in range(test_length)])
print("target : ",target)

listeInit = word_list_init(200, len(target))
start = time.time()

print("iteration n°" ,nbIteration)
newGeneList = new_generation(target, listeInit)
bestWord = get_best(target, newGeneList)[0]
bestDistance = get_best(target,newGeneList)[1]
# time.sleep(1)

while bestWord != target:
    nbIteration += 1
    print("iteration n°",nbIteration)
    newGeneList = new_generation(target, newGeneList)
    bestWord = get_best(target, newGeneList)[0]
    bestDistance = get_best(target,newGeneList)[1]
    #time.sleep(1)

end = time.time() - start
print(end)

# # # La cible est :
# # #/\     /\
# # #  \ _____\
# # #   (_)-(_)
# ascii_target="/\     /\   \ _____\   (_)-(_)"

# def printer_ascii(indiv, length):
#     tab_print = [indiv[i*length:(i*length)+length] for i in range(int(len(indiv)/length))]
#     for line in tab_print:
#         print("".join(chr(c) for c in line))

# listeAscii = []
# for c in ascii_target:
#     listeAscii.append(c)

# print(listeAscii)
# print(printer_ascii(listeAscii, len(listeAscii)))