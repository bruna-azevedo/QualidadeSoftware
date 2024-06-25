from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Substitua pelo caminho para o seu ChromeDriver
# ou
# chrome_driver_path = "/caminho/para/seu/chromedriver"  # No macOS/Linux

# Configuração do WebDriver
driver = webdriver.Chrome()

try:
    # Carregar a página Client Side Delay no UI Testing Playground
    driver.get("http://uitestingplayground.com/clientdelay")

    # Esperar até que a página seja carregada
    time.sleep(2)

    # Localizar o botão Ajax e clicar nele
    ajax_button = driver.find_element(By.ID, 'ajaxButton')
    ajax_button.click()

    # Aguardar o tempo necessário para que a operação seja concluída (neste caso, 17 segundos)
    time.sleep(17)

    # Verificar se a mensagem de sucesso está presente
    success_message = driver.find_element(By.CLASS_NAME, 'bg-success').text
    assert "Data calculated on the client side." in success_message, "Mensagem de sucesso não encontrada."

    # Imprimir o resultado do teste
    print("Teste de Client Side concluído com sucesso!")

finally:
    # Fechar o navegador
    driver.quit()
