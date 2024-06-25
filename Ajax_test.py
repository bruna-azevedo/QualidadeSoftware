from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Substitua pelo caminho para o seu ChromeDriver
#chrome_driver_path = "C:/caminho/para/seu/chromedriver.exe"  # No Windows
# ou
# chrome_driver_path = "/caminho/para/seu/chromedriver"  # No macOS/Linux

# Configuração do WebDriver
driver = webdriver.Chrome()

try:
    # Carregar a página principal do UI Testing Playground
    driver.get("http://uitestingplayground.com/")

    # Esperar até que a página seja carregada
    time.sleep(2)

    # Navegar até a página do teste AJAX
    ajax_test_link = driver.find_element(By.LINK_TEXT, 'AJAX Data')
    ajax_test_link.click()

    # Esperar até que a página do AJAX Data seja carregada
    time.sleep(6)

    # Clicar no botão "AJAX Button"
    ajax_button = driver.find_element(By.ID, 'ajaxButton')
    ajax_button.click()

    # Esperar até que a mensagem resultante seja carregada
    time.sleep(17)  # Aumentar este tempo caso a resposta AJAX demore mais

    # Verificar se a mensagem resultante foi carregada corretamente
    result_message = driver.find_element(By.CSS_SELECTOR, '#content > p.bg-success')
    assert "Data loaded with AJAX get request." in result_message.text

    # Imprimir a mensagem resultante
    print(result_message.text)

finally:
    # Fechar o navegador
    driver.quit()
