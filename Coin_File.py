import pandas as pd
import xlsxwriter

#Criar e salvar arquivo com os parametros de "Nome do arquivo(filename) e Dataframe(resultTable)"
def saveFile(resultTable, filename):
   writerTable = pd.ExcelWriter(filename, engine='xlsxwriter')
   resultTable.to_excel(writerTable, sheet_name='Coins', index=False)

   writerTable.close()

#Ler a tabela de um arquivo Excel com o parametro(CoinTable) que é o diretorio do aquivo
def ReadFile(CoinTable):
   df = pd.read_excel(CoinTable)

   return df






