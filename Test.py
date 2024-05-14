import random #importuje modul má funkci generovat náhodná čísla

pole = []

vzdálenost = random.randint(1,5)

for x in range(vzdálenost):
    pole.append(random.randint(1,1000))

print(pole)