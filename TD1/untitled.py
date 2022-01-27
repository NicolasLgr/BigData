# tous les imports de ce TD devront être placés ici
from math import dist
import random
import time
import numpy as np
import string

nb_iteration = 0

# la fonction de conversion dune chaîne de caractères en liste de valeurs ASCII vous est founie
def string_to_int_list(string):
    return [ord(character) for character in list(string)]


def get_distance(string1, string2):
    distance = 0 
    index = 0
    distance_B = 0
    int1 = string_to_int_list(string1)
    int2 = string_to_int_list(string2)
    
    for number in int1:
        distance_B = abs(int1[index] - int2[index])
        distance += distance_B
        index += 1
    
    return distance


def get_best(string, liste_compare):
    liste_distance = []
    
    for liste_nombre in liste_compare:
        liste_distance.append(get_distance(string,liste_nombre))
        if len(liste_distance) == 1:
            min_distance = liste_distance[0]
            mot = liste_nombre
        else:
            if get_distance(string,liste_nombre) < min_distance:
                min_distance = get_distance(string,liste_nombre)
                mot = liste_nombre
            
    return mot, min_distance


# Fonction qui renvoie une liste de mots
# prends en paramêtre le nombre de mot que doit contenir la liste
def word_list_init(nombre_de_mot, lettre):
    liste_mot = []
    
    # genere 5 lettres aléatoire, fait un espace et regènère 5 lettres aléatoire
    # le nombre de fois qui est demandé par la fonction passé en paramètre
    for iteration in range(nombre_de_mot):
        liste_mot.append(''.join(random.choice(string.ascii_letters) 
                                for index in range(lettre)))
    return liste_mot

#change une liste asctii en mot
def ascii_to_lettre(ascii_liste):
    return ''.join(chr(i) for i in ascii_liste)


def crossover(string1, string2):
    string1_int = string_to_int_list(string1)
    string2_int = string_to_int_list(string2)
    enfant = []
    string1_length = len(string1_int)
    
    for i in range(string1_length):
        choice = np.random.choice(np.arange(0, 2), 
                                  p=[0.85, 0.15])
        if choice == 0: 
            enfant.append(string1_int[i])
        else: 
            enfant.append(string2_int[i])
    
    return enfant
    
def new_generation(ma_super_target, ma_liste):
    new_generation = []
    len_ma_liste = len(ma_liste)
    
    #Ajoute le mot qui a la meilleur distance au tableau new_generation
    for i in range(5):
        best_distance = get_best(ma_super_target, ma_liste)
        best_word = best_distance[0]
        new_generation.append(best_word)
        ma_liste.pop(ma_liste.index(best_word))

    while len(new_generation) != len_ma_liste:
        random = np.random.choice(np.arange(0, 5), p=[0.2, 0.2, 0.2, 0.2, 0.2])
        if best_distance[1] > 100:
            if random == 0:
                random_word1 = new_generation[0]
                random_word2 = new_generation[0]
                new_enfant1 = crossover(random_word1, random_word2)
                new_enfant2 = mutation(new_enfant1,ma_super_target)
                new_generation.append(ascii_to_lettre(new_enfant2))
            elif random == 1:
                random_word1 = new_generation[0]
                random_word2 = new_generation[1]
                new_enfant1 = crossover(random_word1, random_word2)
                new_enfant2 = mutation(new_enfant1, ma_super_target)
                new_generation.append(ascii_to_lettre(new_enfant2))
            elif random == 2:
                random_word1 = new_generation[1]
                random_word2 = new_generation[2]
                new_enfant1 = crossover(random_word1, random_word2)
                new_enfant2 = mutation(new_enfant1, ma_super_target)
                new_generation.append(ascii_to_lettre(new_enfant1))
            elif random == 3:
                random_word1 = new_generation[2]
                random_word2 = new_generation[3]
                new_enfant1 = crossover(random_word1, random_word2)
                new_enfant2 = mutation(new_enfant1, ma_super_target)
                new_generation.append(ascii_to_lettre(new_enfant1))
            elif random == 4:
                random_word1 = new_generation[3]
                random_word2 = new_generation[4]
                new_enfant1 = crossover(random_word1, random_word2)
                new_enfant2 = mutation(new_enfant1, ma_super_target)
                new_generation.append(ascii_to_lettre(new_enfant1))
        else:
            random_word2 = np.random.choice(ma_liste)
            random_word1 = np.random.choice(new_generation)
            new_enfant1 = crossover(random_word1, random_word2)
            new_enfant2 = mutation(new_enfant1,ma_super_target)
            new_generation.append(ascii_to_lettre(new_enfant2))

    return new_generation

def mutation(mot_ascii, ma_target):
    taille_mot = len(mot_ascii)
    distance = get_distance(ma_target, ascii_to_lettre(mot_ascii))
    
    for i in range(taille_mot):
        if distance < 100 and distance >= 50:
            chance = random.randint(0,9)
            if chance == 1:
                poids_mutation = distance// 20
                random_number = random.randint(-1 * poids_mutation, poids_mutation)
                mot_ascii[i] = (random_number + mot_ascii[i]) % 255
        elif distance < 50 and distance >= 15:
            chance = random.randint(0,12)
            if chance == 1:
                poids_mutation = 2
                random_number = random.randint(-1 * poids_mutation, poids_mutation)
                mot_ascii[i] = (random_number + mot_ascii[i]) % 255
        elif distance < 15:
            chance = random.randint(0,15)
            if chance == 1:
                poids_mutation = 1
                random_number = random.randint(-1 * poids_mutation, poids_mutation)
                mot_ascii[i] = (random_number + mot_ascii[i]) % 255
        else:
            chance = random.randint(0,18)
            if chance == 1:
                poids_mutation = distance// 10
                random_number = random.randint(-1 * poids_mutation, poids_mutation)
                mot_ascii[i] = (random_number + mot_ascii[i]) % 255 
 
    return mot_ascii

def printer_ascii(indiv, length):
    tab_print = [indiv[i*length:(i*length)+length] for i in range(int(len(indiv)/length))]
    for line in tab_print:
        print("".join(chr(c) for c in line))



#               *         *      *         *              
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
ascii_target = "/\     /\   \ _____\   (_)-(_)"

       
test_length = 20
target = "".join([chr(random.randint(0, 255)) for _ in range(test_length)])
nb_iteration = 0

def algo_genetique(ma_super_target, nb_iteration):
    print("ma_super_target : ",ma_super_target, "de longueur", len(ma_super_target))

    listeInit = word_list_init(100, len(ma_super_target))

    print("iteration n°" ,nb_iteration)
    new_gene_list = new_generation(ma_super_target, listeInit)
    best_word = get_best(ma_super_target, new_gene_list)[0]
    best_distance = get_best(ma_super_target,new_gene_list)[1]
    print("le meilleur mot est :", best_word,"avec une distance de:",best_distance) 
    # time.sleep(1)

    start = time.time()
    while best_word != ma_super_target:
        # time.sleep(1)
        nb_iteration += 1
        print("iteration n°", nb_iteration)
        print("")
        new_gene_list = new_generation(ma_super_target, new_gene_list)
        best_word = get_best(ma_super_target, new_gene_list)[0]
        best_distance = get_best(ma_super_target,new_gene_list)[1]
        print("     le meilleur mot est :", best_word,"avec une distance de:",best_distance) 

# algo_genetique(target, nb_iteration)
# for i in range(100):
#     random_number = np.random.choice(np.arange(-1, 2), p=[0.5, 0, 0.5])
#     print(random_number)

print("c1 : 651")
print("random number == -1927")
print("651 - 1927 %1000")
soustra = 651 - 1927
print(soustra)
#  mon c1 avant : 651
#          poid de mutation : 2911
#          random number ==  -1927
#          mon c1 après : 724