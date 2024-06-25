from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com")

# 2 - Navega até a pagina "Text Input"
    text_input_link = driver.find_element(By.LINK_TEXT, "Text Input")
    text_input_link.click()
    time.sleep(4)
# Esperando a pagina carregar
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "newButtonName")))

    # 3 - Digita o texto no campo
    input_field = driver.find_element(By.ID, "newButtonName")
    test_text = "Nome Teste Botão"
    input_field.send_keys(test_text)
    time.sleep(6)

    # 4 - Clica no botão
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    time.sleep(3)

    # 5 - Verifica se a mudança no botão esta de acordo
    updated_button_text = button.text
    assert updated_button_text == test_text, f"Botão esperado era: '{test_text}', mas recebido: '{updated_button_text}'"
    time.sleep(2)

    print("Teste bem sucedido: Botão atualizado")

finally:
    driver.quit()