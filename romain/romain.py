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
    return valeurs.get(chiffre_romain.upper(), 0)


def romain_to_num(romain):
    nombre = 0
    for i in range(len(romain)):
        if i < len(romain) - 1:
            suiv = i + 1
            # ignorer le caractère si il n'est pas valable
            while valeur_de(romain[suiv]) == 0:
                suiv += 1
            if valeur_de(romain[i]) < valeur_de(romain[suiv]):
                nombre -= valeur_de(romain[i])
            else:
                nombre += valeur_de(romain[i])
        else:
            nombre += valeur_de(romain[i])
    return nombre


def calculatrice(operateur, romain1, romain2):
    if operateur == '+':
        return romain_to_num(romain1) + romain_to_num(romain2)
    elif operateur == '-':
        return romain_to_num(romain1) - romain_to_num(romain2)
    elif operateur == '*':
        return romain_to_num(romain1) * romain_to_num(romain2)
    elif operateur == '/':
        return romain_to_num(romain1) / romain_to_num(romain2)
    return 0