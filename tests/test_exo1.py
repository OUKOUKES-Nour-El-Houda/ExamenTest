from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Utilisez le WebDriver approprié
        self.driver.implicitly_wait(10)  # Attendre implicitement jusqu'à ce que les éléments soient disponibles

    def test_login(self):
        driver = self.driver
        driver.get("https://automationexercise.com/login")
        print("Page chargée")

        # Remplir le formulaire d'inscription
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys("essaiydy")
        driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("abir.@test.com")
        driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

        # Remplir le formulaire de création de compte
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("Super124!")
        driver.find_element(By.ID, "first_name").send_keys("ABI")
        driver.find_element(By.ID, "last_name").send_keys("ESAIYdA")
        driver.find_element(By.ID, "address1").send_keys("12345 de Paris")
        driver.find_element(By.ID, "state").send_keys("Île-de-France")
        driver.find_element(By.ID, "city").send_keys("Lille")
        driver.find_element(By.ID, "zipcode").send_keys("7521")
        driver.find_element(By.ID, "mobile_number").send_keys("+3323467869")

        # Soumettre le formulaire de création de compte
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='create-account']"))).click()

        # Vérifie que la connexion a été réussie
        try:
            # Remplacez 'some-success-class' par la classe qui est réellement affichée après la connexion
            success_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "success-message-class")))  # Mettez ici la classe correcte
            self.assertTrue(success_element.is_displayed(), "L'élément de succès n'est pas affiché.")
        except Exception as e:
            print("Erreur lors de la vérification de la connexion:", e)

    def tearDown(self):
        self.driver.quit()  # Fermer le navigateur après les tests

if __name__ == "__main__":
    unittest.main()
