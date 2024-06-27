from numb3rs import validate

def test_edge_validate():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_positive():
    assert validate("1.2.3.4") == True
    assert validate("10.20.30.49") == True
    assert validate("100.150.200.250") == True

def test_negative():
    assert validate("-1.2.3.4") == False
    assert validate("0.-1.2.3") == False
    assert validate("0.0.-1.2") == False
    assert validate("0.1.2.-3") == False

def test_unfit():
    assert validate("1-2-3-4") == False
    assert validate("1234") == False
    assert validate("fail") == False
    assert validate("255") == False
    assert validate("255.256.256.256") == False
    assert validate("255.255.256.256") == False
    assert validate("255.255.255.256") == False
    assert validate("0") == False

