import time
import re
from selenium import webdriver as opWeb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



# Abrir o site
navegador = opWeb.Chrome()
navegador.get('https://www.bcb.gov.br/conversao')
element = WebDriverWait(navegador, 10).until(ec.presence_of_element_located((By.NAME, 'valorBRL')))
navegador.find_element(By.ID, 'button-converter-de').click()
time.sleep(2)
dropdown = navegador.find_element(By.ID, 'moedaBRL')
num_options = len(dropdown.find_elements(By.TAG_NAME, 'li'))
print(num_options)


'''element_Result = navegador.find_element(By.XPATH, '/html/body/app-root/app-root/main/dynamic-comp/div/div[1]/bcb-detalhesconversor/div/div[2]/div/div[1]/div[2]/div').text
str_result = re.search(r'Resultado da conversão: (\d+(?:,\d+)?)', element_Result)

if str_result:
    numero = str_result.group(1)
else:
    numero = None

print(numero)

time.sleep(5)'''