import unittest
import tempfile
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class TestLogin(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        # Créer un répertoire temporaire pour les données utilisateur avec un identifiant unique
        unique_id = str(int(time.time()))  # Utiliser un timestamp comme identifiant unique
        self.temp_dir = tempfile.mkdtemp(prefix=f"user_data_{unique_id}_")
        chrome_options.add_argument(f"user-data-dir={self.temp_dir}")
        # Option pour éviter les problèmes de sécurité dans les environnements CI
        chrome_options.add_argument('--no-sandbox')
        
        # Instancier le WebDriver Chrome
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_login(self):
        # Exemple de test de connexion
        self.driver.get("https://example.com/login")
        # Ajoutez ici vos étapes de test pour remplir le formulaire de connexion

    def tearDown(self):
        # Fermer le navigateur et supprimer le répertoire temporaire
        self.driver.quit()
        import shutil
        shutil.rmtree(self.temp_dir)

if __name__ == "__main__":
    unittest.main()
