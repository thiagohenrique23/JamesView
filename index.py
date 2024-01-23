from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='./chromedriver.exe')

# Configurar instância do navegador

options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--headless") 
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# Criar instância do navegador

driver = webdriver.Chrome(service=service, options=options)

# Número desejado de visitas

num_visitas = 10

# Abrir o site várias vezes

for _ in range(num_visitas):
    driver.get('https://www.google.com/')
    # Aguardar um tempo (por exemplo, 1 segundo) entre as visitas
    time.sleep(1)

# Fechar o navegador no final
    
driver.quit()
