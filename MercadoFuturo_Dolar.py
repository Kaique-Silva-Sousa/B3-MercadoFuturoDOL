import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta

data_atual = datetime.today().strftime('%d/%m/%Y')

hoje = datetime.now()
ultimos_30_dias = [(hoje - timedelta(days=i)).strftime('%d/%m/%Y') for i in range(30)]

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
browser = webdriver.Chrome(options=options)

def conversao_numerico(x):
    if pd.isna(x):
        return x
    return x.replace('.', '').replace(',', '.')

def getDados():
    browser.get('https://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-sistema-pregao-ptBR.asp?Data=01/08/2024&Mercadoria=DOL')
    vencimentos = []
    dados_precos = []
    data = []
    for datas in ultimos_30_dias:
        try:
            input_data = browser.find_element(By.ID, 'dData1')
            input_data.clear()
            select_element = browser.find_element(By.ID, "comboMerc1")
            select_dol = Select(select_element)
            input_data.send_keys(datas)
            select_dol.select_by_visible_text("DOL : Dólar comercial")
            ven = browser.find_element(By.ID, 'MercadoFut0').text
            vencimentos.extend(ven.split()[1:])
            dados_preços = browser.find_element(By.ID, 'MercadoFut2').text
            dados_precos.extend(dados_preços.split()[19:])
            data.extend([datas]*len(ven.split()[1:]))
        except:
            vencimentos.extend([np.nan])
            data.extend([np.nan])
            dados_precos.extend([np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
            browser.get('https://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-sistema-pregao-ptBR.asp?Data=01/08/2024&Mercadoria=DOL')
    browser.quit()
    vencimentos_df = pd.DataFrame({"Vencimentos":vencimentos})
    dados_precos_split = np.array_split(dados_precos, vencimentos_df.shape[0])
    dados_precos_df = pd.DataFrame(dados_precos_split, columns=['PREÇO ABERT.', 'PREÇO MÍN', 'PPREÇO MÁX.', 'PREÇO MÉD.', 'ÚLT. PREÇO', 'AJUSTE', 'VAR. PTOS.', 'ÚLT. OF. COMPRA','ÚLT. OF. VENDA'])
    tabela_unida = vencimentos_df.merge(dados_precos_df, left_index=True,right_index=True,how='inner')
    datas_df = pd.DataFrame({"Data":data})
    tabela_final = tabela_unida.merge(datas_df,left_index=True,right_index=True,how='inner')
    tabela_final = tabela_final[~tabela_final['Vencimentos'].isnull()]
    columns  = ['PREÇO ABERT.', 'PREÇO MÍN', 'PPREÇO MÁX.', 'PREÇO MÉD.', 'ÚLT. PREÇO', 'AJUSTE', 'VAR. PTOS.', 'ÚLT. OF. COMPRA','ÚLT. OF. VENDA']

    tabela_final[columns] = tabela_final[columns].applymap(conversao_numerico)
    tabela_final[columns] = tabela_final[columns].apply(lambda x: pd.to_numeric(x,errors='ignore'))
    tabela_final.to_excel('MercadoFuturo_DOL.xlsx', index=False)

getDados()
