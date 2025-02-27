from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

# Configuration du navigateur
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # Accéder à la page d'inscription
    driver.get("https://automationexercise.com/login")
    print("Page chargée")
    time.sleep(3)  # Pause pour laisser le popup apparaître

    # Première action : Cliquer sur "Autoriser" pour les cookies
    print("Recherche du bouton 'Autoriser' dans le popup de consentement...")
    autoriser_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fc-cta-consent"))
    )
    autoriser_button.click()
    print("✅ Bouton 'Autoriser' cliqué avec succès")
    time.sleep(2)  # Pause pour stabiliser

    # Fonctions de génération aléatoire
    def generate_random_string(length):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def generate_random_email():
        return f"{generate_random_string(8)}@test.com"

    def generate_random_password():
        return f"{generate_random_string(10)}!Aa1"

    def generate_random_address():
        return f"{random.randint(1, 9999)} {generate_random_string(10)} Street"

    # Génération des données
    name = generate_random_string(6)
    email = generate_random_email()
    password = generate_random_password()
    first_name = generate_random_string(5)
    last_name = generate_random_string(7)
    address = generate_random_address()
    state = generate_random_string(8)
    city = generate_random_string(6)
    zipcode = ''.join(random.choices(string.digits, k=5))
    mobile_number = ''.join(random.choices(string.digits, k=10))

    print(f"Essai avec l'email : {email}")

    # Remplir le formulaire d'inscription initial
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@data-qa='signup-name']"))
    ).send_keys(name)

    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    # Attendre le formulaire détaillé
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))

    # Remplir les champs supplémentaires
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "first_name").send_keys(first_name)
    driver.find_element(By.ID, "last_name").send_keys(last_name)
    driver.find_element(By.ID, "address1").send_keys(address)
    driver.find_element(By.ID, "state").send_keys(state)
    driver.find_element(By.ID, "city").send_keys(city)
    driver.find_element(By.ID, "zipcode").send_keys(zipcode)
    driver.find_element(By.ID, "mobile_number").send_keys(f"+33{mobile_number}")

    # Soumettre le formulaire final avec défilement
    create_account_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-qa='create-account']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", create_account_button)
    time.sleep(1)

    try:
        create_account_button.click()
        print("✅ Bouton 'Create Account' cliqué avec succès")
    except:
        print("⚠️ Clic normal intercepté, tentative avec JavaScript...")
        driver.execute_script("arguments[0].click();", create_account_button)
        print("✅ Clic forcé via JavaScript effectué")

    # Attendre explicitement la page de confirmation
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Account Created')]"))
        )
        print("✅ Inscription réussie avec succès !")
    except:
        print("⚠️ Échec de la vérification de la confirmation. La page a peut-être mal chargé.")

except Exception as e:
    print(f"❌ Une erreur s'est produite : {e}")

finally:
    driver.quit()
    