import romain.romain as r

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
    assert r.romain_to_num("MDCJLXVI") == 1666

def test_nombres_doubles():
    assert r.romain_to_num("II") == 2
    assert r.romain_to_num("VVII") == 12
    assert r.romain_to_num("XXII") == 22
    assert r.romain_to_num("LLII") == 102
    assert r.romain_to_num("CCII") == 202
    assert r.romain_to_num("DDII") == 1002
    assert r.romain_to_num("MMII") == 2002

def test_nombres_sous():
    assert r.romain_to_num("IV") == 4
    assert r.romain_to_num("XIV") == 14
    assert r.romain_to_num("VXIV") == 9
    assert r.romain_to_num("MCMXLIV") == 1944