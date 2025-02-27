import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Exécuter en mode headless pour CI/CD
        self.driver = webdriver.Chrome(options=options)

    def test_login(self):
        driver = self.driver
        driver.get("https://automationexercise.com/login")
        print("Page chargée")

        # Remplir le formulaire d'inscription
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys("essaiydy")
        driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("abir.@test.com")
        driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

        # Remplir le formulaire de création de compte
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
        driver.find_element(By.ID, "password").send_keys("Super124!")
        driver.find_element(By.ID, "first_name").send_keys("ABI")
        driver.find_element(By.ID, "last_name").send_keys("ESAIYdA")
        driver.find_element(By.ID, "address1").send_keys("12345 de Paris")
        driver.find_element(By.ID, "state").send_keys("Île-deLAFrace")
        driver.find_element(By.ID, "city").send_keys("lile")
        driver.find_element(By.ID, "zipcode").send_keys("7521")
        driver.find_element(By.ID, "mobile_number").send_keys("+3323467869")

        # Soumettre le formulaire de création de compte
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='create-account']"))).click()

        # Vérifie que la connexion a été réussie (adapté selon l'application)
        # Par exemple, vérifier si un élément spécifique est présent sur la page après la connexion
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "some-success-class")))  # Remplace par une classe existante sur la page

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
