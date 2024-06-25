from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/visibility")

    # Esperar até que a página seja carregada
    time.sleep(2)

    # Localizar o botão Hide
    hide_button = driver.find_element(By.ID, 'hideButton')

    # Clicar no botão Hide para esconder o elemento
    hide_button.click()

    # Esperar um pouco para que a ação seja concluída
    time.sleep(1)

    # Verificar se o elemento 'zeroWidthButton' possui a classe 'zerowidth'
    zero_width_button = driver.find_element(By.ID, 'zeroWidthButton')
    classes = zero_width_button.get_attribute('class')
    assert 'zerowidth' in classes.split(), "O elemento 'zeroWidthButton' não possui a classe 'zerowidth'."

    # Imprimir o resultado do teste
    print("O elemento 'zeroWidthButton' possui a classe 'zerowidth'.")

finally:
    # Fechar o navegador
    driver.quit()
