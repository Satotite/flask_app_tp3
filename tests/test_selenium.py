from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_formulaire_selenium():
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    try:
        driver.get("http://127.0.0.1:5000/form")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "prenom")))
        driver.find_element(By.NAME, "prenom").send_keys("Salma")
        driver.find_element(By.NAME, "nom").send_keys("Totite")
        driver.find_element(By.NAME, "email").send_keys("salma@test.com")
        driver.find_element(By.NAME, "telephone").send_keys("0600000000")
        driver.find_element(By.NAME, "sujet").send_keys("Support technique")
        driver.find_element(By.NAME, "message").send_keys("Message test")
        # driver.find_element(By.NAME, "consentement").click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form button"))).click()

        driver.save_screenshot("screenshot.png")
    finally:
        driver.quit()

