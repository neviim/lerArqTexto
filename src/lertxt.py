#!/usr/bin/env python
# -*-coding: utf-8-*-

__autor__   = "Neviim Jads"
__version__ = "v 0.1"

import io
from libjads import lookupDirectory

# Usando esta função.
lista = lookupDirectory('data')

# Le e imprime todas as linhas do arquivo.
arquivo = io.open("data/"+ lista[0], 'r', encoding="utf-8")
for linha in arquivo:
    print(linha)

arquivo.close()
