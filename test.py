import numpy as np
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0

for i in range(100):
    random = np.random.choice(np.arange(0, 5), p=[0.5, 0.25, 0.15, 0.05, 0.05])
    if random == 0:
        count0+= 1
    if random == 1:
        count1 += 1
    if random == 2:
        count2 += 1
    if random == 3:
        count3 += 1
    if random == 4:
        count4 += 1
    print(random)

print("pour 0 : \n\t", "moyenne", count0/100, "apparition:", count0)
print("pour 1 : \n\t", "moyenne", count1/100, "apparition:", count1)
print("pour 2 : \n\t", "moyenne", count2/100, "apparition:", count2)
print("pour 3 : \n\t", "moyenne", count3/100, "apparition:", count3)
print("pour 4 : \n\t", "moyenne", count4/100, "apparition:", count4)