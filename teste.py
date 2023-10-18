# import PySimpleGUI as sg
# sg.theme_previewer()

from PySimpleGUI import * # importa todos os comandos da lib para o GUI
import serial as srl # importa pyserial
from time import sleep

theme('Default') 

layout = [
    [Text('Faça o Login para acessar:', font=('Segoe UI', 12))],
    [InputText('Digite o código de colaborador', size = (26,1))],
    [InputText('Digite sua senha', size = (15,1))],
    [Button('Login', size = (20,1)), Button('Cancelar', size = (20,1))],
    [Text('__________________________________________________')],
    [Graph((125, 50), (0,0), (125,50), k='-GRAPH-')]
]

layout1 = [
    [Text('Automação Intralogística', font=('Segoe UI', 12))],
    [Text('Selecione o "slot" desejado da prateleira')],
    [Button('P1,1', size = (12,1)), Button('P1,2', size = (12,1)), Button('P1,3', size = (12,1))],
    [Button('P2,1', size = (12,1)), Button('P2,2', size = (12,1)), Button('P2,3', size = (12,1))],
    [Button('P3,1', size = (12,1)), Button('P3,2', size = (12,1)), Button('P3,3', size = (12,1))],
    [Text('_______________________________________________')],
    [Button('Inventário', size = (12,1)), Text('                             '), Button('Sair', size = (10,1))]
]

layout2 = [
    [Text('Você acessou a posição linha 2, coluna 3 da prateleira:', font=('Segoe UI', 12))],
    #[Checkbox('Texto do Checkbox', key='chave', default=False, change_submits=True, enable_events=False)]
    [Text('A posição: Contém produto "X"', font=('Segoe, UI', 10))],
    [Button('Paletizar', size = (8,1)), Button('Abastecer', size = (8,1), disabled=True)]
]

janela = Window('Login', layout)

eventos, valores = janela.Read()
if eventos == 'Login':
    janela = Window('IHM', layout1)
    eventos, valores = janela.Read()
    if eventos == 'P2,3':
        janela = Window('P 2-3', layout2)
 

while True: #Laço para o envio do comandos
    eventos, valores = janela.Read() #Leitural dos valores e eventos da tela
    cmd = '' #Comando a ser enviado
    if eventos == WINDOW_CLOSED: #Checa se a janela é fechada
        break
    
    #Cerifica quais botões foram apertados
    if eventos == 'Gay':
        cmd = 'a'
        print('a')
    elif eventos == 'Gay2':
        cmd = 'b'
        print('b')
