import csv
from os import listdir, times
import random as rd
import numpy as np
import time

tab = []
mon_fichier = []

# 47 normalement
def get_result_from_csv(name, csv_file):
    with open(csv_file, "r") as file:
        data = file.readlines()
        for line in data:
            line = line.split(",")
            if line[1] == name:
                if '' not in line and '\n' not in line:
                    if float(line[2]).is_integer() == True and float(line[3]).is_integer() == True and float(line[4]).is_integer() == True and float(line[5]).is_integer() == True and float(line[6]).is_integer() == True and float(line[7]).is_integer() == True:
                        if -1000 <= int(line[2]) <= 1000 and -1000 <= int(line[3]) <= 1000 and -1000 <= int(line[4]) <= 1000 and -1000 <= int(line[5]) <= 1000 and -1000 <= int(line[6]) <= 1000:
                            if int(line[2]) != 0 and int(line[3]) != 0 and  int(line[4]) != 0 and int(line[5]) != 0 and int(line[6]) != 0 and int(line[7]) != 0:
                                if -5000000 <= int(line[7]) <= 5000000:
                                    line[7] = line[7].split("\n")[0]
                                    for i in range(2,8):
                                        tab.append(line[i])
                                    
    return tab, len(tab)

# for elements in get_result_from_csv("Leger", "TD2\ExamColl.csv")[0]:
#     print(elements)

# Renvoie la meilleur distance entre 2 mots
def get_distance(mon_y, mon_x, mon_c):
    res = 0
    
    for i in range(5):
        res = res + mon_c[i] * mon_x[i]
        
    return abs(mon_y - res)

# Renvoie le meilleur d'une liste et sa distance avec la target
def get_best(mon_y, mon_x, liste_mon_c):
    liste_distance = []
    
    for liste_nombre in liste_mon_c:
        liste_distance.append(get_distance(mon_y,mon_x,liste_nombre))
        
    min_distance = min(liste_distance)
    mot = liste_mon_c[liste_distance.index(min_distance)]
    return mot, min_distance

# Fonction qui renvoie une liste de mots
# prends en paramêtre le nombre de mot que doit contenir la liste
def word_list_init(nombre_de_mot, nb_facteur):
    liste_mot = []
    end_list = []

    for iteration in range(nombre_de_mot):
        for i in range(nb_facteur):
            liste_mot.append(rd.randint(-1000, 1000))
        end_list.append(liste_mot.copy())
        liste_mot.clear()

    return end_list

# Prends 2 mots en paramêtres
# Renvoie un nouveau mot en mélangeant les 2 mots données
def crossover_nombre(mon_c1, mon_c2):
    enfant = []
    list_number1_length = len(mon_c1)
    # Il y a 85% de chance de prendre la lettre du premiers mot placé en paramêtre
    for i in range(list_number1_length):
        choice = np.random.choice(np.arange(0, 2), 
                                  p=[0.5, 0.5])
        if choice == 0: 
            enfant.append(mon_c1[i])
        else: 
            enfant.append(mon_c2[i])
    return enfant

def new_generation(mon_y, mon_x, liste_de_c):
    new_generation = []
    len_mon_c = len(liste_de_c)
    
    #Ajoute le mot qui a la meilleur distance au tableau new_generation
    best_distance = get_best(mon_y, mon_x, liste_de_c)
    best_word = best_distance[0]
    new_generation.append(best_word)
    liste_de_c.pop(liste_de_c.index(best_word))

    while len(new_generation) != len_mon_c:
        random = np.random.choice(np.arange(0, 2), p=[0.4, 0.6])
        if random == 0:
            random_word1 = new_generation[0]
            random_word2 = rd.choice(liste_de_c)
            new_enfant1 = crossover_nombre(random_word1, random_word2)
            new_enfant2 = mutation(mon_y, mon_x, new_enfant1)
            new_generation.append(new_enfant2)
        elif random == 1:
            random_word1 = rd.choice(liste_de_c)
            random_word2 = rd.choice(liste_de_c)
            new_enfant1 = crossover_nombre(random_word1, random_word2)
            new_enfant2 = mutation(mon_y, mon_x, new_enfant1)
            new_generation.append(new_enfant2)
    
    return new_generation

# Prend en paramêtre un mot et la target
def mutation(mon_y, mon_x, mon_c ):
    longueur_c = len(mon_c)
    distance = get_distance(mon_y, mon_x, mon_c)
    
    # Pour chaque caractere du mot donné en paramètre
    for i in range(longueur_c):
        chance = rd.randint(0,6)
        if chance == 1:
            if distance < 30:
                poids_mutation = 1
            else:
                poids_mutation = distance // 10
            random_number = rd.randint(-1 * poids_mutation, poids_mutation)
            mon_c[i] = (random_number + mon_c[i]) % 1000 
 
    return mon_c





def algo_genetique(mon_y, mon_x, nb_iteration):
    print("ma_super_target : ",mon_y)

    list_of_c = word_list_init(200,5)
    print(list_of_c)

    print("iteration n°" ,nb_iteration)
    new_gene_list = new_generation(mon_y, mon_x, list_of_c)
    best_word = get_best(mon_y, mon_x, new_gene_list)[0]
    best_distance = get_best(mon_y, mon_x, new_gene_list)[1]
    print("le meilleur mot est :", best_word,"avec une distance de:",best_distance) 

    while best_distance != 0:
        nb_iteration += 1
        print("iteration n°",nb_iteration)
        new_gene_list = new_generation(mon_y,mon_x, new_gene_list)
        best_word = get_best(mon_y,mon_x, new_gene_list)[0]
        best_distance = get_best(mon_y, mon_x, new_gene_list)[1]
        print("     le meilleur mot est :", best_word,"avec une distance de:",best_distance)

x = [444, 510, 789,-862, 306]
c = [[982, 932, -834, 995, 948], [543, 678, -320, 900, 832]] 
c_bis = [543, 678, -320, 900, 832]
y = -155674

print(algo_genetique(y, x, 0))




test = [53, 809, 22, 865, 446]

def verif(mon_x, mon_c):
    somme = 0 
    for i in range(len(mon_x)):
        somme = somme + mon_x[i] * mon_c[i]
    return somme
print(verif(x, test))

