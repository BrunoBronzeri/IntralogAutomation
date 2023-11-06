import PySimpleGUI as sg
import os
import csv
cwd = os.getcwd()
print("Current working directory is:", cwd)


def grava_dados(viagens):
    arquivo = open('viagens.csv', 'a+', encoding='utf-8')
    municipio = viagens['municipio']
    estado = viagens['estado']
    atividades = viagens['atividades']
    arquivo.write(municipio + ", " + estado + ", " + atividades + "\n")
    print('GRAVOU O ARQUIVO')
    arquivo.close()


def tela_inicial():
    sg.theme('DarkTeal3')
    layout = [
        [sg.Text("Cadastro de viagens", font="Arial 16 bold", pad=(25, 30))],
        [sg.Button("Cadastro", key="cadastro", size=(40, 2))],
        [sg.Button("Consulta", key="consulta", size=(40, 2))]
    ]

    janela = sg.Window("Tela inicial", layout, text_justification="center")
    botao, valores = janela.read()
    janela.close()
    return botao


def cadastra():
    sg.theme('DarkTeal3')
    layout = [
        [sg.Text("Cadastre sua viagem!", font=("Arial 16 bold"), pad=(20, 30))],
        [sg.Text("Município", size=(10, 1)), sg.Input(
            key="municipio", size=(40, 1))],
        [sg.Text("Estado", size=(10, 1)), sg.Input(
            key="estado", size=(40, 1))],
        [sg.Text("Atividades", size=(10, 1)), sg.Input(
            key="atividades", size=(40, 1))],
        [sg.Button("Cadastrar", key="cadastrar", size=(23, 2)),
         sg.Button("Voltar", key="voltar", size=(24, 2))]
    ]

    janela = sg.Window("Cadastro", layout)
    botao, valores = janela.read()
    janela.close()
    if botao == 'cadastrar':
        grava_dados(valores)
    elif botao == 'voltar':
        tela_inicial()


def listar():
    viagens = []
    with open('viagens.csv', encoding='utf-8') as arquivo_referencia:
        tabela = csv.reader(arquivo_referencia, delimiter=',')
        for l in tabela:
            municipio = l[0]
            estado = l[1]
            ativ = l[2]
            viagem = [municipio, estado, ativ]
            viagens.append(viagem)
    return viagens


def lista_viagens(dados):
    sg.theme('DarkTeal3')
    layout = [
        [sg.Text("Lista de viagens", font=("Arial 16 bold"), pad=(20, 30))],
        [sg.Table(values=dados, headings=['Município', 'Estado',
                  'Atividades'], auto_size_columns=True, num_rows=10)],
        [sg.Button("Voltar", key="voltar", size=(24, 2))]
    ]
    janela = sg.Window("Lista de viagens", layout)
    botao, valores = janela.read()
    janela.close()
    if botao == 'voltar':
        tela_inicial()


def main():
    sg.theme('DarkTeal3')

    while True:
        opcao = tela_inicial()
        try:
            match opcao:
                case 'cadastro':
                    cadastra()
                case 'consulta':
                    viagens = listar()
                    lista_viagens(viagens)
                case _:
                    grava_dados()
                    break

        except SystemExit:
            exit()


main()