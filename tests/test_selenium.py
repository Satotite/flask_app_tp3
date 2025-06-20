from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_formulaire_selenium():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:5000/form")

    # ✅ Attendre que le champ prénom soit visible (le formulaire est prêt)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "prenom"))
    )

    driver.find_element(By.NAME, "prenom").send_keys("Salma")
    driver.find_element(By.NAME, "nom").send_keys("Totite")
    driver.find_element(By.NAME, "email").send_keys("salma@test.com")
    driver.find_element(By.NAME, "telephone").send_keys("0601020304")
    driver.find_element(By.NAME, "sujet").send_keys("Support technique")
    driver.find_element(By.NAME, "message").send_keys("Je rencontre un problème technique.")
    driver.find_element(By.NAME, "consentement").click()

    # ✅ Attendre que le bouton soit cliquable
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "form button"))
    ).click()

    # Vérification du message de succès
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Merci Salma Totite")
    )

    # Capture
    driver.save_screenshot("formulaire_riche_resultat.png")
    driver.quit()
