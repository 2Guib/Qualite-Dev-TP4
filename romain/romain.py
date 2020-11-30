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


def num_to_romain(num):
    res = ""
    if num<0:
        num*=-1
        res+="-"
    while num >= valeur_de('M'):
        res += "M"
        num -= valeur_de('M')
    if num >= valeur_de('C') * 9:
        res += "CM"
        num -= romain_to_num("CM")
    while num >= valeur_de('D'):
        res += "D"
        num -= valeur_de('D')
    if num >= valeur_de('C') * 4:
        res += "CD"
        num -= romain_to_num("CD")
    while num >= valeur_de('C'):
        res += "C"
        num -= valeur_de('C')
    if num >= valeur_de('X') * 9:
        res += "XC"
        num -= romain_to_num("XC")
    while num >= valeur_de('L'):
        res += "L"
        num -= valeur_de('L')
    if num >= valeur_de('X') * 4:
        res += "XL"
        num -= romain_to_num("XL")
    while num >= valeur_de('X'):
        res += "X"
        num -= valeur_de('X')
    if num >= valeur_de('I') * 9:
        res += "IX"
        num -= romain_to_num("IX")
    while num >= valeur_de('V'):
        res += "V"
        num -= valeur_de('V')
    if num >= valeur_de('I') * 4:
        res += "IV"
        num -= romain_to_num("IV")
    while num >= valeur_de('I'):
        res += "I"
        num -= valeur_de('I')

    if num == 0:
        return res
    else:
        return -1


def calculatrice_romain(operateur, romain1, romain2):
    return num_to_romain(calculatrice(operateur, romain1, romain2))
