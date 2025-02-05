"""
Renaud Morissette
TP 01
"""


# 1
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
