def est_valide(prenom, nom, email, consentement):
    return all([
        prenom.strip(),
        nom.strip(),
        "@" in email,
        consentement
    ])

def test_est_valide():
    assert est_valide("Salma", "Totite", "salma@test.com", True) is True
    assert est_valide("", "Totite", "salma@test.com", True) is False
    assert est_valide("Salma", "", "salma@test.com", True) is False
    assert est_valide("Salma", "Totite", "invalidemail", True) is False
    assert est_valide("Salma", "Totite", "salma@test.com", False) is False

def telephone_valide(tel):
    return tel.isdigit() and len(tel) == 10

def test_telephone_valide():
    assert telephone_valide("0601020304") is True
    assert telephone_valide("06abc20304") is False
    assert telephone_valide("") is False
    assert telephone_valide("12345") is False

