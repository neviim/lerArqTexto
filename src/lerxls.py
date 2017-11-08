#!/usr/bin/env python
# -*-coding: utf-8-*-

__autor__   = "Neviim Jads"
__version__ = "v 0.3"

import io
import pandas as pd
from libjads import Valida, Doador

# le os arquivos dentro do diretorio ../data ...
path = '../data'
lista = Valida(path)
arquivos = lista.getArquivos()
#print(lista)

# -- tem que arrumar isso para autolatico planilha especifica.
arq_xls = pd.ExcelFile(path +'/'+ arquivos[1])
aba_xls = arq_xls.sheet_names
#print(aba_xls)

# le a sheet 1 da planilha
# df = pd.read_excel(xlsx, aba_xls[0])

df = arq_xls.parse(aba_xls[0])
#print(arq_xls.parse(aba_xls[0]))

#print(df.columns)
#print(df[df.columns[0]])
#print(df[df.columns[0]][1])
#print(df[df.columns[1]][1])
#print(df[df.columns[2]][1])
#print(len(df.columns))

linhas = df[df.columns[0]]
#print(linhas)
#print(len(linhas.dropna()))
#print(linhas.dropna())

# loop
#for i in df.index:
for i in range(len(df[df.columns[0]].dropna())):
    ''' Loop para ler todas as linhas. '''
    # loop para ler todas as colunas.
    registro = ['id_neviim_777']
    for x in range(len(df.columns)):
        registro.append(df[df.columns[x]][i]) # passara por todos as colunas

    # processa registro por linha da planilha.
    doador = Doador(*registro)
    print(doador)
    print('...')
    #break
