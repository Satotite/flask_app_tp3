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
print("Test lancé depuis GitHub Actions")