# import PySimpleGUI as sg
# sg.theme_previewer()

from PySimpleGUI import * # importa todos os comandos da lib para o GUI
import serial as srl # importa pyserial
from time import sleep # Importa sleep para intereação com usuário

import os # importa lib Miscellaneous
import csv # lib para ler arquivo CSV
cwd = os.getcwd()
print("Current working directory is:", cwd) # 

theme('DefaultNoMoreNagging') 

layout = [
    [Text('Faça o Login para acessar:', font=('Segoe UI', 12))],
    [Text('Código de colaborador:', font=('Segoe UI', 8))],
    [Input(key='usuario')],
    [Text('Senha:', font=('Segoe UI', 8))],
    [Input(key='senha')],
    [Text('', font=('Segoe UI', 2))],
    [Button('Login', size = (20,1))],
    [Text('', key='mensagem')],
    [Text('__________________________________________________')]
]


########################## Leitura de Banco de Dados #############################

def slots():
   
    x = 10

    return x

########################## Escreve no Arquivo ####################################

def write_data(data):

    return 0 

##################################################################################


janela = Window('Login', layout)

while True:
    event, values = janela.read()
    if event == WIN_CLOSED:
        break
    elif event == 'Login':
        password = '111213'
        user = '20204055'
        usuario = values['usuario']
        senha = values['senha']
        if senha == password and usuario == user:
            janela['mensagem'].update('Login feito com sucesso')

            sleep(1)
            
            janela.close()
            janela = Window('IHM', layout1, size = (1400,700))
            events, values = janela.read()
            if event == WIN_CLOSED:
                break
            else:
                slots()
            
        else:
            janela['mensagem'].update('usuário e/ou senha incorreto', text_color=('red'))

# eventos, valores = janela.Read()
# if eventos == 'Login':
#     janela = Window('IHM', layout1, size=(1400,700))
#     eventos, valores = janela.Read()
#     if eventos == 'P2,3':
#         janela = Window('P 2-3', layout2)
 

# while True: #Laço para o envio do comandos
#     eventos, valores = janela.Read() #Leitural dos valores e eventos da tela
#     cmd = '' #Comando a ser enviado
#     if eventos == WINDOW_CLOSED: #Checa se a janela é fechada
#         break
    
#     #Cerifica quais botões foram apertados
#     if eventos == 'Gay':
#         cmd = 'a'
#         print('a')
#     elif eventos == 'Gay2':
#         cmd = 'b'
#         print('b')


