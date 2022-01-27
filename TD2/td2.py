from os import listdir, times
import random as rd
import numpy as np



# 47 valeurs trouvé
def get_result_from_csv(name, csv_file):
    tab_x = []
    tab_y = []
    
    with open(csv_file, "r") as file:
        data = file.readlines()
        #Pour chaque ligne du fichier csv on indique le separateur
        for line in data:
            line = line.split(",")
            #On vérifie le nom de la personne
            if line[1] == name:
                #On ne prend pas en compte les éléments vides ou retour à la ligne
                if '' not in line and '\n' not in line:
                    
                    #On vérifie que les x soit des entiers
                    if float(line[2]).is_integer() == True and float(line[3]).is_integer() == True:
                        if float(line[4]).is_integer() == True and float(line[5]).is_integer() == True:
                            if float(line[6]).is_integer() == True and float(line[7]).is_integer() == True:
                                
                                #On vérifie que les x soient entre -1000 et 1000
                                if -1000 <= int(line[2]) <= 1000 and -1000 <= int(line[3]) <= 1000 and -1000 <= int(line[4]) <= 1000: 
                                    if -1000 <= int(line[5]) <= 1000 and -1000 <= int(line[6]) <= 1000:
                                        
                                        #Le chiffre 0 apparaît trop souvent
                                        #On concidère ça comme une incohérence
                                        #On en prends pas en comlpte les lignes qui possèdent 0
                                        if int(line[2]) != 0 and int(line[3]) != 0 and  int(line[4]) != 0:
                                            if int(line[5]) != 0 and int(line[6]) != 0 and int(line[7]) != 0:
                    
                                                #On vérifie la borne de y
                                                if -5000000 <= int(line[7]) <= 5000000:
                                                    
                                                    #On récupère uniquement la parti du y sans le \n
                                                    line[7] = line[7].split("\n")[0]
                                                    
                                                    #Génère une liste des x et l'ajoute dans la liste de tous les x
                                                    tab_x.append([int(line[2]), 
                                                                int(line[3]), 
                                                                int(line[4]), 
                                                                int(line[5]), 
                                                                int(line[6])])
                                                    
                                                    #Ajout du y dans la liste de tous les y
                                                    tab_y.append(int(line[7]))
                                    
    return len(tab_x), tab_x, tab_y

tab_value = get_result_from_csv("Leger", "TD2\ExamColl.csv")

# tu as un C
# tu le multiplie par tous les X, tu additionne les multiplication et tu soustrais à y
# Renvoie la meilleur distance entre 2 mots
def get_coef_for_distance(mon_y, mon_x, mon_c):
    resultat = 0
    for i in range(5):
        resultat = resultat + mon_c[i] * mon_x[i]
    
    return abs(mon_y - resultat)

def get_distance(mes_y, mes_x, mon_c):

    final_distance = 0
    for i in range(len(mes_y)):
        final_distance = final_distance + get_coef_for_distance(mes_y[i], mes_x[i], mon_c)

    return final_distance

# Renvoie le meilleur d'une liste et sa distance avec la target
def get_best(mon_y, mon_x, liste_mon_c):
    liste_distance = []
    
    for liste_nombre in liste_mon_c:
        liste_distance.append(get_distance(mon_y,mon_x,liste_nombre))
        
    min_distance = min(liste_distance)
    mot = liste_mon_c[liste_distance.index(min_distance)]
    return mot, min_distance

# Fonction qui renvoie une liste de mots
# prends en parametre le nombre de mot que doit contenir la liste
def word_list_init(nombre_de_mot, nb_facteur):
    liste_mot = []
    end_list = []

    for iteration in range(nombre_de_mot):
        for i in range(nb_facteur):
            liste_mot.append(rd.randint(-1000, 1000))
        end_list.append(liste_mot.copy())
        liste_mot.clear()

    return end_list

# Prends 2 mots en parametres
# Renvoie un nouveau mot en melangeant les 2 mots donnees
def crossover_nombre(mon_c1, mon_c2):
    enfant = []
    list_number1_length = len(mon_c1)
    # Il y a 85% de chance de prendre la lettre du premiers mot place en parametre
    for i in range(list_number1_length):
        choice = np.random.choice(np.arange(0, 2), 
                                  p=[0.55, 0.45])
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
    print("best de la generation: ", best_word)
    new_generation.append(best_word)
    liste_de_c.pop(liste_de_c.index(best_word))

    while len(new_generation) != len_mon_c:
        random = np.random.choice(np.arange(0, 2), p=[0.8, 0.2])
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

# Prend en parametre un mot et la target
def mutation(mon_y, mon_x, mon_c ):
    longueur_c = len(mon_c)
    distance = get_distance(mon_y, mon_x, mon_c)
    
    # Pour chaque caractere du mot donne en parametre
    for i in range(longueur_c):
        chance = rd.randint(0,3)
        if chance == 0:
            poids_mutation = distance //10000
            
            random_number = rd.randint(-1 * poids_mutation, poids_mutation)
            if -1000 > (random_number + mon_c[i]) > 1000:
                tmp = (random_number + mon_c[i])
                mon_c[i] = tmp % 1000
            else:
                mon_c[i] = (random_number + mon_c[i])
    
    return mon_c



def algo_genetique(mon_y, mon_x, nb_iteration):
    list_of_c = word_list_init(300,5)

    print("=== Generation numero :" ,nb_iteration,'===')
    new_gene_list = new_generation(mon_y, mon_x, list_of_c)
    best_word = get_best(mon_y, mon_x, new_gene_list)[0]
    best_distance = get_best(mon_y, mon_x, new_gene_list)[1]
    print("le meilleur mot est :", best_word,"avec une distance de:",best_distance,"\n")

    while best_distance != 0:
        nb_iteration += 1
        print("=== Generation numero :" ,nb_iteration,'===')
        new_gene_list = new_generation(mon_y,mon_x, new_gene_list)
        best_word = get_best(mon_y,mon_x, new_gene_list)[0]
        best_distance = get_best(mon_y, mon_x, new_gene_list)[1]
        print("     le meilleur mot est :", best_word,"avec une distance de:",best_distance)
        print("")
    print("\n=============RESULTAT=============")

    return best_word, nb_iteration


print(algo_genetique(tab_value[2], tab_value[1], 0))
# moyenne_iteration = 0
# for i in range(10):
#     moyenne_iteration += algo_genetique(tab_value[2], tab_value[1], 0)[1]
# print("=============MOYENNE=============\n",moyenne_iteration/i)

# print("=============TABLEAU DE MON X=============\n",tab_value[1],"\n")
# print("=============TABLEAU DE MON Y=============\n",tab_value[2])
