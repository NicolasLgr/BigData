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
    
def new_generation(target, maListe, nbIteration):
    newGeneration = []
    bestDistance = get_best(target, maListe)
    
    #indique le meilleur mot avec sa distance
    print(bestDistance)
    
    lenMaListe = len(maListe)
    
    #Ajoute le mot qui a la meilleur distance au tableau newGeneration
    newGeneration.append(bestDistance[0])
    bestWord = bestDistance[0]
    
    if bestWord == target:        
        return "solution trouvé", nbIteration, "iterations"
    else:  
        maListe.pop(maListe.index(bestWord))

        while len(newGeneration) != lenMaListe:
            randomWord = random.choice(maListe)
            newEnfant = crossover(bestWord, randomWord)
            newEnfant = mutation(newEnfant)
            newGeneration.append(ascii_to_lettre(newEnfant))

        maListe = newGeneration
        
        return new_generation(target, maListe, nbIteration + 1)

def mutation(motAscii):
    tailleMot = len(motAscii)
    
    for i in range(tailleMot):
        choice = random.randint(0,1)
        if choice == 1:
            if get_distance(target,ascii_to_lettre(motAscii)) >= 100:
                motAscii[i] += random.randint(-10,10)
            elif get_distance(target,ascii_to_lettre(motAscii)) >= 40:
                motAscii[i] += random.randint(-5,5)
            elif get_distance(target, ascii_to_lettre(motAscii)) >= 30:
                motAscii[i] += random.randint(-4,4)
            elif get_distance(target, ascii_to_lettre(motAscii)) >= 20:
                motAscii[i] += random.randint(-3,3)
            elif get_distance(target, ascii_to_lettre(motAscii)) >= 10:
                motAscii[i] += random.randint(-2,2)
            elif get_distance(target, ascii_to_lettre( motAscii)) < 10:
                motAscii[i] += random.randint(-1,1)
        
    return motAscii

listeInit = word_list_init(10, len(target))
print(listeInit)
start = time.time()
print(new_generation(target, listeInit, nbIteration))
end = time.time() - start
print(end)


