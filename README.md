# 📄 README - Application Flask avec Tests et CI/CD

## Fonctionnalités de l'application

Cette application Flask propose un formulaire de contact contenant les champs suivants :

* Prénom
* Nom
* Email
* Téléphone
* Sujet
* Message
* Case à cocher pour le consentement

Les données soumises sont vérifiées côté serveur avant traitement.

---

## Fonctionnement des tests

### 1. `est_valide(prenom, nom, email, consentement)`

Fonction qui vérifie que :

* le prénom et le nom ne sont pas vides
* l'email contient un `@`
* le consentement est donné

### 2. `test_est_valide()`

Test unitaire vérifiant les cas suivants :

* Tous les champs valides → retourne `True`
* Prénom ou nom vide → retourne `False`
* Email invalide → retourne `False`
* Consentement non donné → retourne `False`

### 3. `telephone_valide(tel)`

Vérifie que le numéro :

* est composé uniquement de chiffres (`isdigit()`)
* contient exactement 10 chiffres

### 4. `test_telephone_valide()`

Test unitaire avec les cas suivants :

* Numéro valide (10 chiffres)
* Contient des lettres → invalide
* Vide → invalide
* Moins de 10 chiffres → invalide

### 5. `valider_formulaire(data)`

Fonction globale qui combine les deux tests précédents pour valider le formulaire complet.

### 6. `test_formulaire_selenium()`

Test fonctionnel automatisé avec Selenium qui :

* Lance le navigateur en mode "headless"
* Remplit automatiquement le formulaire avec des valeurs valides
* Soumet le formulaire
* Capture une capture d'écran `screenshot.png`

Ce test nécessite que l'application Flask soit démarrée localement (`localhost:5000`).

---

##  CI/CD avec Jenkins

### 🔧 Jenkinsfile

Le pipeline Jenkins contient les étapes suivantes :

1. **Récupération du code** depuis GitHub
2. **Installation des dépendances** avec `pip install -r requirements.txt`
3. **Exécution des tests unitaires** avec `pytest`
4. **Exécution des tests fonctionnels** avec Selenium
5. **Génération des rapports** HTML pour chaque test

###  Intégration continue

* Le pipeline est automatiquement déclenché à chaque **push** grâce à un **webhook GitHub**
* Dans Jenkins :

  * Activer « GitHub hook trigger for GITScm polling » dans les **triggers**
* Sur GitHub :

  * Ajouter l'URL `http://<JENKINS_URL>/github-webhook/` dans les **Webhooks**

###  Webhook GitHub

* **Content type** : `application/json`
* **Event** : `Just the push event`

---

## Rapports de tests

* `rapport_unitaires.html` : généré par `pytest --html=...`
* `rapport_fonctionnel.html` : même principe avec Selenium

---

## Exécution manuelle des tests

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer les tests unitaires
pytest tests/test_logiciel.py --html=rapport_unitaires.html

# Lancer les tests fonctionnels
pytest tests/test_selenium.py --html=rapport_fonctionnel.html
```

