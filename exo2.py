from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
chrome_options = webdriver.ChromeOptions()

driver.get("https://www.cdiscount.com/")

try:
    driver.find_element(By.ID, 'footer_tc_privacy_button_2').click()
except:
    pass

search = driver.find_element(By.ID, 'search')
search.clear()
search.send_keys("iphone 15")
search.send_keys(Keys.ENTER)

time.sleep(3)

price= driver.find_element(By.XPATH,'//*[@id="lpBloc"]/li[2]/div/div/form/div[3]/div/div[1]/div/div[1]/span')
print(price.text)

products = driver.find_elements(By.XPATH, '//*[@id="lpBloc"]/li[3]/div/div/form')
data = []
for product in products:
    try:
        title = product.find_element(By.XPATH, '//*[@id="lpBloc"]/li[3]/div/div/form/div[2]/a/h2').text
    except:
        title = "Titre non disponible"

    try:
        price = product.find_element(By.XPATH, '//*[@id="lpBloc"]/li[3]/div/div/form/div[3]/div/div[1]/div/div[1]/span').text
    except:
        price = "Prix non disponible"

    try:
        description_ul = product.find_element(By.XPATH, '//*[@id="lpBloc"]/li[3]/div/div/form/div[2]/div[3]/ul')
        description_items = description_ul.find_elements(By.TAG_NAME, "li")
        description = "\n".join([item.text for item in description_items])
    except:
        description = "Description non disponible"


    data.append({"Titre": title, "Prix": price, "Description": description})

for item in data:
    print(f"Titre : {item['Titre']}")
    print(f"Prix : {item['Prix']}")
    print(f"Description : {item['Description']}")

time.sleep(5)  

driver.quit()