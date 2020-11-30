import romain.romain as r
import pytest


def test_valeur_de():
    assert r.valeur_de('I') == 1
    assert r.valeur_de('V') == 5
    assert r.valeur_de('X') == 10
    assert r.valeur_de('L') == 50
    assert r.valeur_de('C') == 100
    assert r.valeur_de('D') == 500
    assert r.valeur_de('M') == 1000
    assert r.valeur_de('Q') == 0


def test_chiffre():
    assert r.romain_to_num("I") == 1
    assert r.romain_to_num("V") == 5
    assert r.romain_to_num("X") == 10
    assert r.romain_to_num("L") == 50
    assert r.romain_to_num("C") == 100
    assert r.romain_to_num("D") == 500
    assert r.romain_to_num("M") == 1000
    assert r.romain_to_num("K") == 0


def test_nombres_simple():
    assert r.romain_to_num("VI") == 6
    assert r.romain_to_num("XVI") == 16
    assert r.romain_to_num("LXVI") == 66
    assert r.romain_to_num("CLXVI") == 166
    assert r.romain_to_num("DCLXVI") == 666
    assert r.romain_to_num("MDCLXVI") == 1666


def test_nombres_doubles():
    assert r.romain_to_num("II") == 2
    assert r.romain_to_num("VV") == 10
    assert r.romain_to_num("XX") == 20
    assert r.romain_to_num("LL") == 100
    assert r.romain_to_num("CC") == 200
    assert r.romain_to_num("DD") == 1000
    assert r.romain_to_num("MM") == 2000


def test_nombres_sous():
    assert r.romain_to_num("IV") == 4
    assert r.romain_to_num("XIV") == 14
    assert r.romain_to_num("VXIV") == 9
    assert r.romain_to_num("MCMXLIV") == 1944


def test_nombres_invalide():
    assert r.romain_to_num("IKV") == 4
    assert r.romain_to_num("XKIV") == 14
    assert r.romain_to_num("VKXIV") == 9
    assert r.romain_to_num("MCKMXLIV") == 1944


def test_calculatrice_addition_chiffres():
    assert r.calculatrice('+', "", "") == 0
    assert r.calculatrice('+', "I", "") == 1
    assert r.calculatrice('+', "I", "I") == 2
    assert r.calculatrice('+', "V", "I") == 6
    assert r.calculatrice('+', "I", "V") == 6
    assert r.calculatrice('+', "V", "X") == 15
    assert r.calculatrice('+', "L", "X") == 60
    assert r.calculatrice('+', "L", "C") == 150
    assert r.calculatrice('+', "D", "C") == 600
    assert r.calculatrice('+', "D", "M") == 1500


def test_calculatrice_addition_nombres():
    assert r.calculatrice('+', "IV", "") == 4
    assert r.calculatrice('+', "IV", "VI") == 10
    assert r.calculatrice('+', "XIV", "LVI") == 70
    assert r.calculatrice('+', "III", "MCMXLIV") == 1947


def test_calculatrice_soustraction_chiffres():
    assert r.calculatrice('-', "", "") == 0
    assert r.calculatrice('-', "I", "") == 1
    assert r.calculatrice('-', "", "I") == -1
    assert r.calculatrice('-', "I", "I") == 0
    assert r.calculatrice('-', "V", "I") == 4
    assert r.calculatrice('-', "I", "V") == -4


def test_calculatrice_soustraction_nombres():
    assert r.calculatrice('-', "IV", "VI") == -2
    assert r.calculatrice('-', "VI", "IV") == 2
    assert r.calculatrice('-', "IV", "IV") == 0
    assert r.calculatrice('-', "XI", "VI") == 5
    assert r.calculatrice('-', "MCMXLIV", "XLIV") == 1900
    assert r.calculatrice('-', "XL", "MCMXLIV") == -1904


def test_calculatrice_multiplication_chiffres():
    assert r.calculatrice('*', "I", "I") == 1
    assert r.calculatrice('*', "V", "I") == 5
    assert r.calculatrice('*', "V", "") == 0
    assert r.calculatrice('*', "0", "V") == 0
    assert r.calculatrice('*', "V", "V") == 25
    assert r.calculatrice('*', "V", "X") == 50
    assert r.calculatrice('*', "X", "V") == 50


def test_calculatrice_multiplication_nombres():
    assert r.calculatrice('*', "IV", "VI") == 24
    assert r.calculatrice('*', "VI", "IV") == 24
    assert r.calculatrice('*', "VI", "") == 0
    assert r.calculatrice('*', "VI", "I") == 6
    assert r.calculatrice('*', "MCMXLIV", "X") == 19440


def test_calculatrice_division_chiffres():
    assert r.calculatrice('/', "I", "I") == 1
    assert r.calculatrice('/', "V", "I") == 5
    assert r.calculatrice('/', "0", "V") == 0
    assert r.calculatrice('/', "V", "V") == 1
    assert r.calculatrice('/', "V", "X") == 0.5
    assert r.calculatrice('/', "X", "V") == 2


def test_calculatrice_division_nombres():
    assert r.calculatrice('/', "VI", "II") == 3
    assert r.calculatrice('/', "IV", "II") == 2
    assert r.calculatrice('/', "MCMXLIV", "IV") == 486
    assert r.calculatrice('/', "I", "III") == 1 / 3
    assert r.calculatrice('/', "XL", "V") == 8


def test_calculatrice_division_par_0():
    with pytest.raises(ZeroDivisionError):
        assert r.calculatrice('/', "X", "")


def test_calculatrice_operateur_invalide():
    assert r.calculatrice('E', "XL", "V") == 0
    assert r.calculatrice('', "XL", "V") == 0


def test_num_vers_romain_chiffre():
    assert r.num_to_romain(1000) == "M"
    assert r.num_to_romain(500) == "D"
    assert r.num_to_romain(100) == "C"
    assert r.num_to_romain(50) == "L"
    assert r.num_to_romain(10) == "X"
    assert r.num_to_romain(5) == "V"
    assert r.num_to_romain(1) == "I"


def test_num_vers_romain_double():
    assert r.num_to_romain(3000) == "MMM"
    assert r.num_to_romain(300) == "CCC"
    assert r.num_to_romain(30) == "XXX"
    assert r.num_to_romain(3) == "III"


def test_num_vers_romain_sous_chiffres():
    assert r.num_to_romain(4) == "IV"
    assert r.num_to_romain(40) == "XL"
    assert r.num_to_romain(400) == "CD"
    assert r.num_to_romain(900) == "CM"
    assert r.num_to_romain(90) == "XC"
    assert r.num_to_romain(9) == "IX"


def test_num_vers_romain_complexe():
    assert r.num_to_romain(1944) == "MCMXLIV"
    assert r.num_to_romain(2999) == "MMCMXCIX"
    assert r.num_to_romain(4732) == "MMMMDCCXXXII"


def test_calculatrice_romain_addition():
    assert r.calculatrice_romain('+', "IV", "") == "IV"
    assert r.calculatrice_romain('+', "IV", "VI") == "X"
    assert r.calculatrice_romain('+', "XIV", "LVI") == "LXX"
    assert r.calculatrice_romain('+', "III", "MCMXLIV") == "MCMXLVII"

def test_calculatrice_romain_soustraction_nombres():
    assert r.calculatrice_romain('-', "IV", "VI") == "-II"
    assert r.calculatrice_romain('-', "VI", "IV") == "II"
    assert r.calculatrice_romain('-', "IV", "IV") == ""
    assert r.calculatrice_romain('-', "XI", "VI") == "V"
    assert r.calculatrice_romain('-', "MCMXLIV", "XLIV") == "MCM"
    assert r.calculatrice_romain('-', "XL", "MCMXLIV") == "-MCMIV"

def test_calculatrice_romain_multiplication_nombres():
    assert r.calculatrice_romain('*', "IV", "VI") == "XXIV"
    assert r.calculatrice_romain('*', "VI", "IV") == "XXIV"
    assert r.calculatrice_romain('*', "VI", "") == ""
    assert r.calculatrice_romain('*', "VI", "I") == "VI"

def test_calculatrice_romain_division_nombres():
    assert r.calculatrice_romain('/', "VI", "II") == "III"
    assert r.calculatrice_romain('/', "IV", "II") == "II"
    assert r.calculatrice_romain('/', "MCMXLIV", "IV") == "CDLXXXVI"
    assert r.calculatrice_romain('/', "XL", "V") == "VIII"

def test_calculatrice_romain_division_par_0():
    with pytest.raises(ZeroDivisionError):
        assert r.calculatrice_romain('/', "X", "")