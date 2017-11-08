#!/usr/bin/env python
# -*-coding: utf-8-*-

''' Dependencias:
        $ pip install openpyxl
'''

__autor__   = "Neviim Jads"
__version__ = "v 0.1"

import io
from libjads import lookupDirectory
from openpyxl import load_workbook

# função lista arquivos
def listaArquivo(arquivos):
    # Le e imprime todas as linhas do arquivo.
    arquivo = io.open("../data/"+ lista[0], 'r', encoding="utf-8")
    print(lista)
    for linha in arquivo:
        print(linha)
    arquivo.close()

# Usando esta função.
lista = lookupDirectory('../data')
listaArquivo(lista)

# Load in the workbook
