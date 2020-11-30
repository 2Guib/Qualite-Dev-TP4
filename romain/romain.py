def valeur_de(chiffre_romain):
    valeurs = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return valeurs.get(chiffre_romain.upper(), 0);


def romain_to_num(romain):
    nombre = 0
    for i in range(len(romain)):
        if i < len(romain) - 1 and valeur_de(romain[i]) < valeur_de(romain[i + 1]):
            nombre -= valeur_de(romain[i])
        else:
            nombre += valeur_de(romain[i])
    return nombre
