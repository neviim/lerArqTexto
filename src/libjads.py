#!/usr/bin/env python
# -*-coding: utf-8-*-

__autor__   = "Neviim Jads"
__version__ = "v 0.1"

import os

# ler extenção do arquivo.
def getExtension(name):
    ''' Le e retorna a estenção do arquivo recebido em (name).
    '''
    fileName, fileExtension = os.path.splitext(name)
    return fileExtension

# Valida se é uma extenção permitida.
def isExtensionValida(extension):
   ''' Valida se é uma extenção valida
   '''
   extensions = ['txt', 'dat']
   for x in extensions:
       if extension[:1] == '.':
           if extension[1:].lower() == x:
               return True
       elif extension.lower() == x:
           return True
   return False

# lista o arquivo neste diretorio
def lookupDirectory(path):
    ''' Coloca em uma lista todos os arquivos com extenção valida.

        Depende da função:
                            isExtensionValida(extension)
                            getExtension(name)

        Mode de uso: lookupDirectory('..\data')

        Retorna uma lista com todos os arquivos dentro deste diretorio.
    '''
    if os.path.isdir(path):
        files = os.listdir(path)
        lista = []
        for i in files:
            if i + '/' != 'windows/':
                if os.path.isdir(path + i + '/'):
                    lookupDirectory(path + i + '/')
                if isExtensionValida(getExtension(i)) == True:
                    lista.append(i)
        return lista

# Usando função: lookupDirectory(path)
# if __name__ == '__main__':
#    lookupDirectory('.\data')
