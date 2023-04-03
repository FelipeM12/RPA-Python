import time
import re
from selenium import webdriver as opWeb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Coin_File import ReadFile as directoryFile
from Coin_File import saveFile

# Ler tabela
coinTable = directoryFile('Coin.xlsx')
print(coinTable)
time.sleep(1)
# Abrir o site
navegador = opWeb.Chrome()
navegador.get('https://www.bcb.gov.br/conversao')
element = WebDriverWait(navegador, 10).until(ec.presence_of_element_located((By.NAME, 'valorBRL')))
time.sleep(2)

#Verificar a quantidade de itens no dropDown
navegador.find_element(By.ID, 'button-converter-de').click()
dropdown = navegador.find_element(By.ID, 'moedaBRL')
num_Itens = len(dropdown.find_elements(By.TAG_NAME, 'li'))
navegador.find_element(By.ID, 'button-converter-de').click()
print(num_Itens)

#Começar a tarefa
linha = 0
for index, item in coinTable.iterrows():
    #escrever o valor#
    valor_input = navegador.find_element(By.NAME, 'valorBRL')
    valor_input.clear()
    verificar = False
    for char in str(item['Valor']):
        valor_input.send_keys(char)
        time.sleep(0.15)
    #Indicar qual a primeira moeda#
    converter_Button = navegador.find_element(By.ID, 'button-converter-de').click()
    time.sleep(1)

    #definir condição 'enquanto' o numero de linhas não passar de 'num_Itens'(numero pego no dropDown) continue
    while linha < int(num_Itens):
        linha = linha + 1
        itemsele = ""
        itemsele = navegador.find_element(By.XPATH, '//*[@id="moedaBRL"]/li['+str(linha)+']/a')
        texto_itemsele = itemsele.text

        #comparar se a moeda da TAG é igual a moeda da tabela
        if texto_itemsele.strip() == str(item['Moeda1']).strip():
            print("Numero:" + str(linha) + ' - Valor encontrado:' + texto_itemsele + ':' + str(item['Moeda1']).strip())
            itemsele.click()
            time.sleep(1)
            linha = 0
            break
        elif linha >= num_Itens:
            print('Parametro incorreto!')
            break

        else:
            # Criar uma lista para melhorar a visualização caso não encontre o item desejado
            print("Numero:"+str(linha)+' - '+texto_itemsele+' : ' + str(item['Moeda1']).strip())

    #Indicar qual a primeira moeda#
    converter_Button = navegador.find_element(By.ID, 'button-converter-para').click()
    linha = 0
    # Definir condição: 'enquanto' o numero de linhas não passar de 'num_Itens'(numero pego no dropDown) continue
    while linha < num_Itens:
        linha = linha + 1
        itemsele = ""
        itemsele = navegador.find_element(By.XPATH, '//*[@id="moedaResultado1"]/li['+str(linha)+']/a')
        texto_itemsele = itemsele.text

        # comparar se a moeda da TAG é igual a moeda da tabela
        if texto_itemsele.strip() == str(item['Moeda2']).strip():
            print("Numero:" + str(linha) + ' - Valor encontrado:' + texto_itemsele + ':' + str(item['Moeda2']).strip())
            itemsele.click()
            time.sleep(1)
            linha = 0
            break
        elif linha >= num_Itens:
            print('Parametro incorreto!')
            break

        else:
            #Criar uma lista para melhorar a visualização caso não encontre o item desejado
            print("Numero:"+str(linha)+' - '+texto_itemsele+' : ' + str(item['Moeda2']).strip())

    navegador.find_element(By.XPATH, '/html/body/app-root/app-root/main/dynamic-comp/div/div[1]/bcb-detalhesconversor/div/div[1]/form/div[2]/div[5]/div/button').click()
    time.sleep(1)

    #tratar o texto retirado do site com Regex(Expressão regular)
    element_Result = navegador.find_element(By.XPATH,
                                            '/html/body/app-root/app-root/main/dynamic-comp/div/div[1]/bcb-detalhesconversor/div/div[2]/div/div[1]/div[2]/div').text
    str_result = re.search(r'Resultado da conversão: (\d{1,3}(?:\.\d{3})*,\d{4})', element_Result)

    if str_result:
        numero = str_result.group(1)
    else:
        numero = None
    #escrever o texto de conversão na coluna 'Resultado' na tabela 'CoinTable'
    time.sleep(1)
    coinTable.loc[index, 'Resultado'] = numero
    time.sleep(1)
    print(coinTable)

#chamar a função saveFile com os parametros 'coinTable' e o nome do arquivo
saveFile(coinTable, "ModifyCoin.xlsx")

print('Conversão completa!!')


#//*[@id="moedaBRL"]/li[122]/a


#<a _ngcontent-pch-c155="" class="dropdown-item"> Dólar dos Estados Unidos (USD) </a>//*[@id="moedaBRL"]/li[162]/a





