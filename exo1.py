from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


driver.get("https://automationexercise.com/login")
print("Page chargée")
time.sleep(5) 


WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys("essaiydynour")


driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("abirnou.@test.com")
driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()


WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))


driver.find_element(By.ID, "password").send_keys("Supernou124!")
driver.find_element(By.ID, "first_name").send_keys("ABtI")
driver.find_element(By.ID, "last_name").send_keys("ESAIYdjtA")
driver.find_element(By.ID, "address1").send_keys("12345 dett Paris")
driver.find_element(By.ID, "state").send_keys("Île-deLAFractte")
driver.find_element(By.ID, "city").send_keys("little")
driver.find_element(By.ID, "zipcode").send_keys("752t1")
driver.find_element(By.ID, "mobile_number").send_keys("+33238467869")


WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='create-account']"))).click()


time.sleep(5)
driver.quit()
