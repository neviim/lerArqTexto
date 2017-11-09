#!/usr/bin/env python
# -*-coding: utf-8-*-

import os

# Autoria e versao.
class Jads(object):
    ''' doc para Jads.
        Usando:
            a = libjads.Jads()
            a.autor
            a.ping
            a.versao
    '''
    def __init__(self, autor='Neviim Jads'):
        super(Jads, self).__init__()
        self.versao = '0.3'
        self.autor = autor
        self.ping = 'pong'


# Validando diretorio e arquivos.
class Valida(object):
    ''' doc para Valida.
            parametro recebido:
                path => caso o Parametro não seja enviado assume por defaut '../data'

            Uso:
                from libjads import Valida

                path = '../data'
                lista = Valida(path)
                arquivos = lista.getArquivos()
                print(arquivos)
    '''
    def __init__(self, path='../data'):
        super(Valida, self).__init__()
        self.path = path

    def getExtensao(self, name):
        ''' Le e retorna a estenção do arquivo recebido em (name).
        '''
        fileName, fileExtension = os.path.splitext(name)
        return fileExtension

    def isExtensaoValida(self, extension):
       ''' Valida se é uma extenção valida
       '''
       extensions = ['txt', 'dat', 'csv', 'xls']
       for x in extensions:
           if extension[:1] == '.':
               if extension[1:].lower() == x:
                   return True
           elif extension.lower() == x:
               return True
       return False

    def getArquivos(self):
        ''' Coloca em uma lista todos os arquivos com extenção valida.

            Depende da função:
                                isExtensaoValida(extension)
                                getExtensao(name)

            Mode de uso: getArquivos('..\data')

            Retorna uma lista com todos os arquivos dentro deste diretorio.
        '''
        if os.path.isdir(self.path):
            files = os.listdir(self.path)
            lista = []
            for i in files:
                if i + '/' != 'windows/':
                    if os.path.isdir(self.path + i + '/'):
                        getArquivos(self.path + i + '/')
                    if self.isExtensaoValida(self.getExtensao(i)) == True:
                        lista.append(i)
            return lista


# classe para abstrair campos da planilha.
class Doador(object):
    ''' Parametro recebido...
        items  = []
        values = []
        ...
        values.append(value)
        item = Doador(*values)
        items.append(item)

        Parametros:
        ['data', 'boletos_Campanha', 'debito_automatico', 'depositos', 'total_diario_clube_do_ouvinte', 'porcentagem_dia_clube', 'davi', 'porcentagem_dia_davi', 'aipf', 'porcentagem_dia_aipf', 'outros', 'porcentagem_dia_outros', 'total_geral_do_dia', 'nan', 'total_acumulado_recebido', 'porcentagem_acumulado', 'dia_util']
    '''
    def __init__(self, id, data, boletos_Campanha, debito_automatico, depositos, total_diario_clube_do_ouvinte,
        porcentagem_dia_clube, davi, porcentagem_dia_davi, aipf, porcentagem_dia_aipf, outros,
        porcentagem_dia_outros, total_geral_do_dia, nan, total_acumulado_recebido, porcentagem_acumulado, dia_util):
        self.id = id
        self.data = data
        self.boletos_Campanha = boletos_Campanha
        self.debito_automatico = debito_automatico
        self.depositos = depositos
        self.total_diario_clube_do_ouvinte = total_diario_clube_do_ouvinte
        self.porcentagem_dia_clube = porcentagem_dia_clube
        self.davi = davi
        self.porcentagem_dia_davi = porcentagem_dia_davi
        self.aipf = aipf
        self.porcentagem_dia_aipf = porcentagem_dia_aipf
        self.outros = outros
        self.porcentagem_dia_outros = porcentagem_dia_outros
        self.total_geral_do_dia = total_geral_do_dia
        self.nan = nan
        self.total_acumulado_recebido = total_acumulado_recebido
        self.porcentagem_acumulado = porcentagem_acumulado
        self.dia_util = dia_util

    def __str__(self):
        ''' Retornar um json com itens por linha. '''
        return("Campanha diaria, object:\n"
               "  id = {0}\n"
               "  data = {1}\n"
               "  boletos_Campanha = {2}\n"
               "  debito_automatico = {3}\n"
               "  depositos = {4}\n"
               "  total_diario_clube_do_ouvinte = {5}\n"
               "  porcentagem_dia_clube = {6}\n"
               "  davi = {7}\n"
               "  porcentagem_dia_davi = {8}\n"
               "  aipf = {9}\n"
               "  porcentagem_dia_aipf = {10}\n"
               "  outros = {11}\n"
               "  porcentagem_dia_outros = {12}\n"
               "  total_geral_do_dia = {13}\n"
               "  nan = {14}\n"
               "  total_acumulado_recebido = {15}\n"
               "  porcentagem_acumulado = {16}\n"
               "  dia_util = {17}"
               .format(self.id, self.data, self.boletos_Campanha, self.debito_automatico,
                       self.depositos, self.total_diario_clube_do_ouvinte,
                       self.porcentagem_dia_clube, self.davi, self.porcentagem_dia_davi,
                       self.aipf, self.porcentagem_dia_aipf, self.outros, self.porcentagem_dia_outros,
                       self.total_geral_do_dia, self.nan, self.total_acumulado_recebido,
                       self.porcentagem_acumulado, self.dia_util))


# Usando função: getArquivos(path)
# if __name__ == '__main__':
#    getArquivos('.\data')
