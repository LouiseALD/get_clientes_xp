import time
import pandas as pd

nro = 0
lista_cod_acessores= [ ' inserir numero dos assessor, ex A12345']   # 'A12345','A12345','A12345'
cont_lista_cod_acessores= len(lista_cod_acessores)
df_colunas = []

time.sleep(1) 
while nro<=cont_lista_cod_acessores:
    print(lista_cod_acessores[nro])
    df = pd.read_html('file:///C:/Users/supor/Documents/XP_scraping/urls/'+lista_cod_acessores[nro]+'.html')[0]
    if len(df)>2:
        print('Gerando CSV')
        time.sleep(2) 
        print(df.columns)
        primeira_coluna = df.columns[0]
        segunda_coluna = df.columns[1]
        del df[primeira_coluna]
        del df[segunda_coluna]
        df.rename(columns = {'SortNome do clienteClassificado em ordem crescenteAções da coluna':'Nome do Cliente', 
        'SortNúmero da contaAções da coluna':'Numero Conta', 
        'SortTelefoneAções da coluna':'Telefone',
        'SortPatrimônio XPAções da coluna':'Patrimonio XP', 
        'SortSaldo em contaAções da coluna':'Saldo em conta',
        'SortCódigo do proprietário da contaAções da coluna':'Codigo Proprietario da Conta',
        'SortAplicações financeiras declaradasAções da coluna':'Aplicacoes financeiras',
        'SortRua de correspondênciaAções da coluna':'Rua de Correspondencia',
        'SortCEP de correspondênciaAções da coluna':'CEP Correspondencia',
        'SortEmailAções da coluna': 'Email',
        'SortCelularAções da coluna':'Celular',
        'SortCNPJAções da coluna':'CNPJ',
        'SortAssessor responsávelAções da coluna':'Acessor responsavel',
        'Ação':'receitabovespa'}, inplace=True)
        df
        df.to_csv(lista_cod_acessores[nro]+'.csv', index=False)
        nro += 1
    else:
        nro += 1
