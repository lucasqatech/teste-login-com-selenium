from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Abrir o navegador
driver = webdriver.Edge()  # ou Chrome, Firefox, etc.
driver.get("https://www.saucedemo.com/")

# Localizar os campos
nome = driver.find_element(By.ID, "user-name")
senha = driver.find_element(By.ID, "password")

# Preencher e enviar
nome.send_keys("standard_user")
senha.send_keys("secret_sauce")
senha.send_keys(Keys.RETURN)

# Feche o navegador
driver.quit()

