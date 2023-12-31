import PySimpleGUI as sg # importa todos os comandos da lib para o GUI
import serial as srl # importa pyserial
from time import sleep # Importa sleep para intereação com usuário

import os # importa lib Miscellaneous
import csv # lib para ler arquivo CSV
cwd = os.getcwd()
print("Current working directory is:", cwd) # 

# Login
def login():
    sg.theme('DefaultNoMoreNagging')
    layout = [
        [sg.Text('Faça o Login para acessar:', font=('Segoe UI', 12))],
        [sg.Text('Código de colaborador:', font=('Segoe UI', 8))],
        [sg.Input(key='usuario')],
        [sg.Text('Senha:', font=('Segoe UI', 8))],
        [sg.Input(key='senha')],
        [sg.Text('', font=('Segoe UI', 2))],
        [sg.Button('Login', size = (20,1))],
        [sg.Text('', key='mensagem')],
        [sg.Text('__________________________________________________')]
    ]

    janela = sg.Window('Login', layout)

    while True:
        event, values = janela.read()
        if event == sg.WIN_CLOSED:
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

                # inserir função que abre a IHM de fato
                #produtos = slots()
                product_list()
                #
                                
            else:
                janela['mensagem'].update('usuário e/ou senha incorreto(s)', text_color=('red'))


# Leitura de Dados e IHM
def slots():
    produtos = []
    with open('estoque.csv', encoding='utf-8') as arquivo_referencia:
        table = csv.reader(arquivo_referencia, delimiter=',')
        for len in table:
            index = len[0]
            presence = len[1]
            produto = [index, presence]
            produtos.append(produto)
    return produtos


def product_list():

    sg.theme('DefaultNoMoreNagging')
    layout1 = [
        [sg.Frame('Posição 1,1', [[sg.T(s=50)],
            [sg.Text('', key="status_a11")],
            [sg.Button('Estocar', key='be11'), sg.Button('Paletizar', key='bp11')]]),
            
            sg.Frame('Posição 1,2', [[sg.T(s=50)],
            [sg.Text('', key="status_a12")],
            [sg.Button('Estocar', key='be12'), sg.Button('Paletizar', key='bp12')]]),

            sg.Frame('Posição 1,3', [[sg.T(s=50)],
            [sg.Text('', key="status_a13")],
            [sg.Button('Estocar', key='be13'), sg.Button('Paletizar', key='bp13')]]),
        ],
        [sg.Frame('Posição 2,1', [[sg.T(s=50)],
            [sg.Text('', key="status_a21")],
            [sg.Button('Estocar', key='be21'), sg.Button('Paletizar', key='bp21')]]),
            
            sg.Frame('Posição 2,2', [[sg.T(s=50)],
            [sg.Text('', key="status_a22")],
            [sg.Button('Estocar', key='be22'), sg.Button('Paletizar', key='bp22')]]),

            sg.Frame('Posição 2,3', [[sg.T(s=50)],
            [sg.Text('', key="status_a23")],
            [sg.Button('Estocar', key='be23'), sg.Button('Paletizar', key='bp23')]]),
        ],
        [sg.Frame('Posição 3,1', [[sg.T(s=50)],
            [sg.Text('', key="status_a31")],
            [sg.Button('Estocar', key='be31'), sg.Button('Paletizar', key='bp31')]]),
            
            sg.Frame('Posição 3,2', [[sg.T(s=50)],
            [sg.Text('', key="status_a32")],
            [sg.Button('Estocar', key='be32'), sg.Button('Paletizar', key='bp32')]]),

            sg.Frame('Posição 3,3', [[sg.T(s=50)],
            [sg.Text('', key="status_a33")],
            [sg.Button('Estocar', key='be33'), sg.Button('Paletizar', key='bp33')]]),
        ],
        [sg.Button('Inventário', disabled=True), sg.Text(' '*255),
         sg.Button('Atualizar', key='refresh')]

    ]

    janela = sg.Window("Automação Intralogística Avançada v1.0", layout1, size=(1200, 400))

    positive = 'Produto localizado'
    negative = 'Produto não localizado'

    while True:

        botao, valores = janela.read(timeout=100)

        dados = slots()

        # Definição de produtos nos slots a_ij
        k = len(dados)
    
        aij = [dados[0][1], dados[1][1], dados[2][1],
            dados[3][1], dados[4][1], dados[5][1],
            dados[6][1], dados[7][1], dados[8][1]]

        #a11
        if int(aij[0]) == 1:
            janela["status_a11"].update(positive, text_color='green')
            janela['be11'].update(disabled=True)
            janela['bp11'].update(disabled=False)
        else:
            janela["status_a11"].update(negative, text_color='red')
            janela['be11'].update(disabled=False)
            janela['bp11'].update(disabled=True)
        #a12
        if int(aij[1]) == 1:
            janela["status_a12"].update(positive, text_color='green')
            janela['be12'].update(disabled=True)
            janela['bp12'].update(disabled=False)
        else:
            janela["status_a12"].update(negative, text_color='red')
            janela['be12'].update(disabled=False)
            janela['bp12'].update(disabled=True)
        #a13
        if int(aij[2]) == 1:
            janela["status_a13"].update(positive, text_color='green')
            janela['be13'].update(disabled=True)
            janela['bp13'].update(disabled=False)
        else:
            janela["status_a13"].update(negative, text_color='red')
            janela['be13'].update(disabled=False)
            janela['bp13'].update(disabled=True)
        #a21
        if int(aij[3]) == 1:
            janela["status_a21"].update(positive, text_color='green')
            janela['be21'].update(disabled=True)
            janela['bp21'].update(disabled=False)
        else:
            janela["status_a21"].update(negative, text_color='red')
            janela['be21'].update(disabled=False)
            janela['bp21'].update(disabled=True)
        #a22
        if int(aij[4]) == 1:
            janela["status_a22"].update(positive, text_color='green')
            janela['be22'].update(disabled=True)
            janela['bp22'].update(disabled=False)
        else:
            janela["status_a22"].update(negative, text_color='red')
            janela['be22'].update(disabled=False)
            janela['bp22'].update(disabled=True)
        #a23
        if int(aij[5]) == 1:
            janela["status_a23"].update(positive, text_color='green')
            janela['be23'].update(disabled=True)
            janela['bp23'].update(disabled=False)
        else:
            janela["status_a23"].update(negative, text_color='red')
            janela['be23'].update(disabled=False)
            janela['bp23'].update(disabled=True)
        #a31
        if int(aij[6]) == 1:
            janela["status_a31"].update(positive, text_color='green')
            janela['be31'].update(disabled=True)
            janela['bp31'].update(disabled=False)
        else:
            janela["status_a31"].update(negative, text_color='red')
            janela['be31'].update(disabled=False)
            janela['bp31'].update(disabled=True)
        #a32
        if int(aij[7]) == 1:
            janela["status_a32"].update(positive, text_color='green')
            janela['be32'].update(disabled=True)
            janela['bp32'].update(disabled=False)
        else:
            janela["status_a32"].update(negative, text_color='red')
            janela['be32'].update(disabled=False)
            janela['bp32'].update(disabled=True)
        #a33
        if int(aij[8]) == 1:
            janela["status_a33"].update(positive, text_color='green')
            janela['be33'].update(disabled=True)
            janela['bp33'].update(disabled=False)
        else:
            janela["status_a33"].update(negative, text_color='red')
            janela['be33'].update(disabled=False)
            janela['bp33'].update(disabled=True)
            
        if botao == sg.WIN_CLOSED:
            break
        
        match botao:
            case 'be11': writeData(1, 1, 'a')
            case 'bp11': writeData(1, 0, 'A')

            case 'be12': writeData(2, 1, 'b')
            case 'bp12': writeData(2, 0, 'B')

            case 'be13': writeData(3, 1, 'c')
            case 'bp13': writeData(3, 0, 'C')

            case 'be21': writeData(4, 1, 'd')
            case 'bp21': writeData(4, 0, 'D')

            case 'be22': writeData(5, 1, 'e')
            case 'bp22': writeData(5, 0, 'E')

            case 'be23': writeData(6, 1, 'f')
            case 'bp23': writeData(6, 0, 'F')

            case 'be31': writeData(7, 1, 'g')
            case 'bp31': writeData(7, 0, 'G')

            case 'be32': writeData(8, 1, 'h')
            case 'bp32': writeData(8, 0, 'H')

            case 'be33': writeData(9, 1, 'i')
            case 'bp33': writeData(9, 0, 'I')


        
def writeData(line, set, cmd):
    
    # Abre o arquivo CSV para leitura
    with open('estoque.csv', 'r') as file:
        reader = csv.reader(file)
        linhas = list(reader)

    # Navega até a linha desejada
    linha_desejada = line  # Índice da linha desejada (começando em 1)
    
    # Colocar um switch para as 9 possibilidades
    if set == 0:
        linha_modificada = '0'  # Substitua pelos novos valores
    elif set == 1:
        linha_modificada = '1'
    

    if 1 <= linha_desejada <= len(linhas):
        linhas[linha_desejada - 1][1] = linha_modificada

    # Criar função para enviar info ao Arduino e
    #entrar num laço while até Arduino retornar 'tarefa feita'
    comArd(cmd)
    # getFrom()

    # Abre o arquivo CSV para escrita e escreve as linhas modificadas
    with open('estoque.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(linhas)
    return 0 

def comArd(cmd):
    arduino.write(cmd.encode()) #Envia o comando UTF-8
    arduino.flush() #Limpa o serial
    sleep(0.5)


def getFrom():
    
    try:
        while True:
            # Leia uma linha da porta serial
            dado = arduino.readline().decode().strip()
            print(f'Dado do Arduino: {dado}')
            break
    except KeyboardInterrupt:
        arduino.close()
        

def main():

    # login()
    
    produtos = slots()
    product_list()

    # return 0

while True: #Laço para conexão com o Arduino
    try: #Tenta se conectar ao Arduino
        arduino = srl.Serial('COM3', 9600) #Cria um elemento conectado a porta COM3
        arduino.flush()
        break
    except Exception: #Se não for possível, imprime a mensagem e dá um delay de 1 segundo
        print('Não foi possível se conectar ao Arduino')
        sleep(1)

main()
