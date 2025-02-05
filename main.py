"""
Renaud Morissette
TP 01
"""

# 1
print("#1\n")


def racines_communes(racine1, racine2):
    racines_non_communes = racines1.symmetric_difference(racines2)
    racines_union = racines1.union(racines2)
    racines_communes_paires = {x for x in racines1.intersection(racines2) if x % 2 == 0}

    return racines_non_communes, racines_union, racines_communes_paires


racines1 = {1, 2, 3, 4, 5}
racines2 = {4, 5, 6, 7}

non_communes, union, communes_paires = racines_communes(racines1, racines2)

print("Racines non communes :", non_communes)
print("Racines de l'union :", union)
print("Racines communes paires :", communes_paires)
print()

#2.a
print("#2.a\n")

meteo_semaine = [(12, 25, 0), (15, 28, 10), (14, 27, 5), (13, 24, 15), (11, 22, 8),
                 (10, 20, 20), (12, 23, 0)]

amplitude_thermique = lambda meteo: meteo[1] - meteo[0]
print(amplitude_thermique(meteo_semaine[5]))
print()

#2.b
print("#2.b\n")

JOURS = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]
dict_amplitude_thermique = {}
for i in range(7):
    dict_amplitude_thermique[JOURS[i]] = amplitude_thermique(meteo_semaine[i])
print(dict_amplitude_thermique)
print()

#2.c
print("#2.c\n")

pluie = lambda meteo: meteo[2]
dict_pluie = {}
for i in range(7):
    dict_pluie[JOURS[i]] = pluie(meteo_semaine[i])
pluie_oui_non = {
    jours: "oui" if dict_pluie > 0
    else "non"
    for jours, dict_pluie in dict_pluie.items()
}
print(pluie_oui_non)
print()

#2.d
print("#2.d\n")

list_temp_max = []
for i in range(7):
    temp_max = meteo_semaine[i][1]
    list_temp_max.append(temp_max)

temp_max_haut = set(filter(lambda x: x > 25, list_temp_max))
for i in temp_max_haut:
    print(JOURS[list_temp_max.index(i)])
print()

#3.a
print("#3.a\n")

matrice = {(0, 0): -1, (0, 2): 3, (1, 1): -2, (2, 0): 4, (2, 2): 5}
