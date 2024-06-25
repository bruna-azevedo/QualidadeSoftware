from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # Carregar a página do Progress Bar no UI Testing Playground
    driver.get("http://uitestingplayground.com/progressbar")

    # Esperar até que a página seja carregada
    time.sleep(2)

    # Iniciar a barra de progresso clicando no botão Start
    start_button = driver.find_element(By.ID, 'startButton')
    start_button.click()

    # Monitorar a barra de progresso até que atinja 75%
    progress_bar = driver.find_element(By.CSS_SELECTOR, '#progressBar')

    while True:
        progress_value = progress_bar.get_attribute('aria-valuenow')
        print(f"Progresso atual: {progress_value}%")
        if int(progress_value) >= 75:
            break
        time.sleep(0.1)  # Pequena espera para não sobrecarregar a CPU

    # Parar a barra de progresso clicando no botão Stop
    stop_button = driver.find_element(By.ID, 'stopButton')
    stop_button.click()

    # Verificar se a barra de progresso parou em 75%
    final_value = progress_bar.get_attribute('aria-valuenow')
    print(f"Progresso final: {final_value}%")
    assert int(final_value) == 75, f"Esperado 75%, mas foi {final_value}%"

finally:
    # Fechar o navegador
    driver.quit()
