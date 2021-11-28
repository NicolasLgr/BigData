# tous les imports de ce TD devront être placés ici
from math import dist
import random
import time
import numpy as np
import string

nbIteration = 0

# la fonction de conversion dune chaîne de caractères en liste de valeurs ASCII vous est founie
def string_to_int_list(string):
    return [ord(character) for character in list(string)]


def get_distance(string1, string2):
    distance = 0 
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
        # if get_distance(string1, string2) >= 100:
        choice = np.random.choice(np.arange(0, 2), p=[0.85, 0.15])
        if choice == 0: 
            enfant.append(string1Int[i])
        else: 
            enfant.append(string2Int[i])
        # else:
        #     choice = np.random.choice(np.arange(0, 2), p=[0.60, 0.40])
        #     if choice == 0: 
        #         enfant.append(string1Int[i])
        #     else: 
        #         enfant.append(string2Int[i])
    
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
        random = np.random.choice(np.arange(0, 5), p=[0.2, 0.2, 0.2, 0.2, 0.2])
        if bestDistance[1] > 100:
            if random == 0:
                randomWord1 = newGeneration[0]
                randomWord2 = newGeneration[0]
                newEnfant1 = crossover(randomWord1, randomWord2)
                newEnfant2 = mutation(newEnfant1,target)
                newGeneration.append(ascii_to_lettre(newEnfant2))
            elif random == 1:
                randomWord1 = newGeneration[0]
                randomWord2 = newGeneration[1]
                newEnfant1 = crossover(randomWord1, randomWord2)
                newEnfant2 = mutation(newEnfant1, target)
                newGeneration.append(ascii_to_lettre(newEnfant2))
            elif random == 2:
                randomWord1 = newGeneration[1]
                randomWord2 = newGeneration[2]
                newEnfant1 = crossover(randomWord1, randomWord2)
                newEnfant2 = mutation(newEnfant1, target)
                newGeneration.append(ascii_to_lettre(newEnfant1))
            elif random == 3:
                randomWord1 = newGeneration[2]
                randomWord2 = newGeneration[3]
                newEnfant1 = crossover(randomWord1, randomWord2)
                newEnfant2 = mutation(newEnfant1, target)
                newGeneration.append(ascii_to_lettre(newEnfant1))
            elif random == 4:
                randomWord1 = newGeneration[3]
                randomWord2 = newGeneration[4]
                newEnfant1 = crossover(randomWord1, randomWord2)
                newEnfant2 = mutation(newEnfant1, target)
                newGeneration.append(ascii_to_lettre(newEnfant1))
        else:
            randomWord2 = np.random.choice(maListe)
            randomWord1 = np.random.choice(newGeneration)
            newEnfant1 = crossover(randomWord1, randomWord2)
            newEnfant2 = mutation(newEnfant1,target)
            newGeneration.append(ascii_to_lettre(newEnfant2))

    return newGeneration

def mutation(motAscii, maTarget):
    tailleMot = len(motAscii)
    distance = get_distance(maTarget,ascii_to_lettre(motAscii))
    for i in range(tailleMot):
        if distance < 100:
            chance = random.randint(0,20)
            if chance == 1:
                poidsMutation = distance// 20
                randomNumber = random.randint(-1 * poidsMutation,poidsMutation)
                motAscii[i] = (randomNumber + motAscii[i]) % 255
        elif distance < 50:
            chance = random.randint(0,200)
            if chance == 1:
                poidsMutation = 2
                randomNumber = random.randint(-1 * poidsMutation,poidsMutation)
                motAscii[i] = (randomNumber + motAscii[i]) % 255
        elif distance < 20:
            chance = random.randint(0,2)
            if chance == 1:
                poidsMutation = 1
                randomNumber = random.randint(-1 * poidsMutation,poidsMutation)
                motAscii[i] = (randomNumber + motAscii[i]) % 255
        else:
            chance = random.randint(0,3)
            if chance == 1:
                poidsMutation = distance// 11
                randomNumber = random.randint(-1 * poidsMutation,poidsMutation)
                motAscii[i] = (randomNumber + motAscii[i]) % 255 
 
    return motAscii

def printer_ascii(indiv, length):
    tab_print = [indiv[i*length:(i*length)+length] for i in range(int(len(indiv)/length))]
    for line in tab_print:
        print("".join(chr(c) for c in line))



#            *         *      *         *                 
#           ***          **********          ***          
#        *****           **********           *****       
#      *******           **********           *******     
#    **********         ************         **********   
#  ****************************************************** 
# ********************************************************
# ********************************************************
# ********************************************************
#  ****************************************************** 
#   ********      ************************      ********  
#    *******       *     *********      *       *******   
#        *****             *****              *****       
#           ***             ***              ***          
#             **             *              **            


ascii_batman="              *         *      *         *                        ***          **********          ***                 *****           **********           *****            *******           **********           *******        **********         ************         **********     ****************************************************   ****************************************************** ************************************************************************************************************************************************************************ ******************************************************   ********      ************************      ********     *******       *     *********      *       *******        ******             *******              ******            *****             *****              *****                 ***             ***              ***                      **             *              **            "

target_toupie ="     /\        .'  `.    .'      `. <          > `.      .'    `.  .'        \/     "
ascii_target="/\     /\   \ _____\   (_)-(_)"


# test_length = 32
# target = "".join([chr(random.randint(0, 255)) for _ in range(test_length)])
print("target : ",ascii_target, "de longueur", len(ascii_target))

listeInit = word_list_init(200, len(ascii_target))

print("iteration n°" ,nbIteration)
newGeneList = new_generation(ascii_target, listeInit)
bestWord = get_best(ascii_target, newGeneList)[0]
bestDistance = get_best(ascii_target,newGeneList)[1]
print("le meilleur mot est :", bestWord,"avec une distance de:",bestDistance) 
# time.sleep(1)

start = time.time()
while bestWord != ascii_target:
    # time.sleep(1)
    nbIteration += 1
    print("iteration n°",nbIteration)
    newGeneList = new_generation(ascii_target, newGeneList)
    bestWord = get_best(ascii_target, newGeneList)[0]
    bestDistance = get_best(ascii_target,newGeneList)[1]
    print("     le meilleur mot est :", bestWord,"avec une distance de:",bestDistance) 
print(time.time() - start)
asciiIntList = string_to_int_list(bestWord)
targetAscii = printer_ascii(asciiIntList, 10)