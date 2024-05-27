import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Descargar ChromeDriver
# Ruta del controlador de Selenium
driver_path = 'C:/Users/ADRIAN/Desktop/python/chromedriver.exe'  # Ruta al chromedriver.exe

# Define las opciones de Chrome
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# URL del formulario de Google
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfZtGScjsnLKoT4KPQ3VPfPB21qY1ukOf4TkdvcdKWgA5O8xw/viewform'

# Función para llenar y enviar el formulario
def fill_and_submit_form(driver):
    driver.get(form_url)
    
    wait = WebDriverWait(driver, 10)  # Espera hasta 10 segundos por un elemento

    def click_checkbox(xpath):
        checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        checkbox.click()

    # Lista de XPaths de los checkboxes segun la cantidad de alternativas
    checkboxes_xpaths = [
        '//*[@id="i5"]/div[3]/div', '//*[@id="i8"]/div[3]/div', '//*[@id="i11"]/div[3]/div',
        '//*[@id="i18"]/div[3]/div', '//*[@id="i21"]/div[3]/div', '//*[@id="i24"]/div[3]/div',
        '//*[@id="i31"]/div[3]/div', '//*[@id="i34"]/div[3]/div', '//*[@id="i37"]/div[3]/div',
        '//*[@id="i40"]/div[3]/div', '//*[@id="i47"]/div[3]/div', '//*[@id="i50"]/div[3]/div',
        '//*[@id="i53"]/div[3]/div', '//*[@id="i56"]/div[3]/div', '//*[@id="i59"]/div[3]/div',
        '//*[@id="i62"]/div[3]/div', '//*[@id="i65"]/div[3]/div', '//*[@id="i68"]/div[3]/div',
        '//*[@id="i75"]/div[3]/div', '//*[@id="i78"]/div[3]/div', '//*[@id="i81"]/div[3]/div',
        '//*[@id="i88"]/div[3]/div', '//*[@id="i91"]/div[3]/div', '//*[@id="i94"]/div[3]/div',
        '//*[@id="i97"]/div[3]/div', '//*[@id="i104"]/div[3]/div', '//*[@id="i107"]/div[3]/div',
        '//*[@id="i110"]/div[3]/div', '//*[@id="i117"]/div[3]/div', '//*[@id="i120"]/div[3]/div',
        '//*[@id="i123"]/div[3]/div', '//*[@id="i126"]/div[3]/div', '//*[@id="i129"]/div[3]/div',
        '//*[@id="i136"]/div[3]/div', '//*[@id="i139"]/div[3]/div', '//*[@id="i142"]/div[3]/div',
        '//*[@id="i145"]/div[3]/div', '//*[@id="i152"]/div[3]/div', '//*[@id="i155"]/div[3]/div',
        '//*[@id="i158"]/div[3]/div', '//*[@id="i161"]/div[3]/div', '//*[@id="i164"]/div[3]/div',
        '//*[@id="i171"]/div[3]/div', '//*[@id="i174"]/div[3]/div', '//*[@id="i177"]/div[3]/div',
        '//*[@id="i184"]/div[3]/div', '//*[@id="i187"]/div[3]/div', '//*[@id="i190"]/div[3]/div',
        '//*[@id="i197"]/div[3]/div', '//*[@id="i200"]/div[3]/div', '//*[@id="i203"]/div[3]/div',
        '//*[@id="i210"]/div[3]/div', '//*[@id="i213"]/div[3]/div', '//*[@id="i216"]/div[3]/div',
        '//*[@id="i223"]/div[3]/div', '//*[@id="i226"]/div[3]/div', '//*[@id="i229"]/div[3]/div',
        '//*[@id="i236"]/div[3]/div', '//*[@id="i239"]/div[3]/div', '//*[@id="i242"]/div[3]/div',
        '//*[@id="i249"]/div[3]/div', '//*[@id="i252"]/div[3]/div', '//*[@id="i255"]/div[3]/div',
        '//*[@id="i262"]/div[3]/div', '//*[@id="i265"]/div[3]/div', '//*[@id="i268"]/div[3]/div',
        '//*[@id="i271"]/div[3]/div', '//*[@id="i278"]/div[3]/div', '//*[@id="i281"]/div[3]/div',
        '//*[@id="i284"]/div[3]/div', '//*[@id="i287"]/div[3]/div', '//*[@id="i294"]/div[3]/div',
        '//*[@id="i297"]/div[3]/div', '//*[@id="i300"]/div[3]/div', '//*[@id="i303"]/div[3]/div',
        '//*[@id="i310"]/div[3]/div', '//*[@id="i313"]/div[3]/div', '//*[@id="i316"]/div[3]/div',
        '//*[@id="i323"]/div[3]/div', '//*[@id="i326"]/div[3]/div', '//*[@id="i329"]/div[3]/div',
        '//*[@id="i336"]/div[3]/div', '//*[@id="i339"]/div[3]/div', '//*[@id="i342"]/div[3]/div',
        '//*[@id="i349"]/div[3]/div', '//*[@id="i352"]/div[3]/div', '//*[@id="i355"]/div[3]/div',
        '//*[@id="i362"]/div[3]/div', '//*[@id="i365"]/div[3]/div', '//*[@id="i372"]/div[3]/div',
        '//*[@id="i375"]/div[3]/div', '//*[@id="i378"]/div[3]/div', '//*[@id="i381"]/div[3]/div',
        '//*[@id="i388"]/div[3]/div', '//*[@id="i391"]/div[3]/div', '//*[@id="i394"]/div[3]/div',
        '//*[@id="i401"]/div[3]/div', '//*[@id="i404"]/div[3]/div', '//*[@id="i407"]/div[3]/div',
        '//*[@id="i410"]/div[3]/div', '//*[@id="i413"]/div[3]/div', '//*[@id="i416"]/div[3]/div',
        '//*[@id="i423"]/div[3]/div', '//*[@id="i426"]/div[3]/div', '//*[@id="i429"]/div[3]/div',
        '//*[@id="i432"]/div[3]/div', '//*[@id="i439"]/div[3]/div', '//*[@id="i442"]/div[3]/div',
        '//*[@id="i445"]/div[3]/div', '//*[@id="i452"]/div[3]/div', '//*[@id="i455"]/div[3]/div',
        '//*[@id="i458"]/div[3]/div', '//*[@id="i461"]/div[3]/div'
    ]

    # Selecciona un número aleatorio de checkboxes para hacer click
    num_checkboxes_to_click = random.randint(1, len(checkboxes_xpaths))  # Ajustar el rango según la necesidad o se puede omitir
    checkboxes_to_click = random.sample(checkboxes_xpaths, num_checkboxes_to_click)

    # Click  los checkboxes seleccionados aleatoriamente
    for xpath in checkboxes_to_click:
        click_checkbox(xpath)

    # Enviar el formulario
    submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span'
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
    submit_button.click()

    # Tiempo de espera para ver  que el formulario se haya enviado
    time.sleep(10)

# Ejecuta el llenado del formulario 50 veces
for _ in range(50):
    # Configura el servicio de ChromeDriver
    service = Service(driver_path)
    service.start()

    # Inicia el navegador Chrome con las opciones configuradas
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        fill_and_submit_form(driver)
    finally:
        # Cierra el navegador
        driver.quit()
        service.stop()

    # Tiempo de espera en iteraciones para no sobrecargar el server
    time.sleep(5)
