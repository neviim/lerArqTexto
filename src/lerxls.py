#!/usr/bin/env python
# -*-coding: utf-8-*-

__autor__   = "Neviim Jads"
__version__ = "v 0.3"

import io
import yaml
import pandas as pd
from libjads import Valida, Doador

# le os arquivos dentro do diretorio ../data ...
path = '../data'
lista = Valida(path)
arquivos = lista.getArquivos()

# -- tem que arrumar isso para autolatico planilha especifica.
arq_xls = pd.ExcelFile(path +'/'+ arquivos[1])
aba_xls = arq_xls.sheet_names

# le a sheet 1 da planilha
df = arq_xls.parse(aba_xls[0])
linhas = df[df.columns[0]]

# loop
#for i in df.index:
for i in range(0, len(df[df.columns[0]].dropna())):
    ''' Loop para ler todas as linhas. '''
    # loop para ler todas as colunas.
    registro = ['id_neviim_777']
    for x in range(len(df.columns)):
        registro.append(df[df.columns[x]][i]) # passara por todos as colunas

    # processa registro por linha da planilha.
    doador = Doador(*registro)
    #doador = yaml.load(str(Doador(*registro)))
    #doador = yaml.load(str(Doador.valor_dia(*registro)))
    print(doador)
    print("...")

    #print(doador['campanha_diaria']['id'])
    #break
