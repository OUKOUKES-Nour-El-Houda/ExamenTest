import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def generate_random_string(length):
    """Génère une chaîne aléatoire de caractères."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def test_inscription(driver):
    driver.get("https://automationexercise.com/login")
    print("Page chargée")

    # Remplissage du formulaire d'inscription
    name = generate_random_string(10)
    email = f"{generate_random_string(5)}@test.com"
    password = "Supernou124!"
    first_name = generate_random_string(5)
    last_name = generate_random_string(5)
    address = f"{random.randint(1, 999)} {generate_random_string(8)} St"
    city = generate_random_string(6)
    state = generate_random_string(6)
    zipcode = ''.join(random.choices(string.digits, k=5))
    mobile_number = ''.join(random.choices(string.digits, k=10))

    # Attendre que le champ de nom soit vis
