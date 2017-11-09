#!/usr/bin/env python
# -*-coding: utf-8-*-

''' Dependencias:
        $ pip install openpyxl
'''
import io
import libjads
from libjads import Valida

# função lista arquivos
def listaArquivo(path, arquivos):
    # Le e imprime todas as linhas do arquivo.
    arquivo = io.open(path +'/'+ arquivos[0], 'r', encoding='utf-8')
    for linha in arquivo:
        print(linha)
    arquivo.close()

# inicio...
if __name__ == '__main__':
    # Usando esta função.
    path = '../data'
    lista = libjads.Valida(path)
    arquivos = lista.getArquivos()
    print(arquivos)

    listaArquivo(path, arquivos)
