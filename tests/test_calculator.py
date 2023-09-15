from calculator import hesapla


def test_hesapla():
    assert hesapla('2+2') == 4
    assert hesapla('3*5') == 15
    assert hesapla('10/2') == 5
    assert hesapla('1/0') == "Hata"
