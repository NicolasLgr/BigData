import csv
import pandas

tab = []

# "_id",name,x1,x2,x3,x4,x5,y
# x1 à x5 compris entre -1000 et 1000
# Dès que il y a une valeur à 0 on enlève
# y compris entre 5 millions et -5 millions


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
                                    tab.append(line)
    return tab, len(tab)
                      

def get_result_2(name, csv_file):
    with open(csv_file, "r") as file:
        data = file.readlines()
        print(data)

get_result_2("Leger", "ExamColl.csv")
# print(get_result_from_csv("Leger", "ExamColl.csv"))