import os

import PySimpleGUI as sg

import scrap
import write


def main():
    layout = [
        [sg.Text("Calculadora de Cupons", justification='center', font="Helvetica 14 bold")],
        [sg.Text("Selecione o .CSV do Relatório Sintético de Vendas por Cliente", font="Helvetica 10 bold")],
        [
            sg.Input(key="-FILE-", enable_events=True),
            sg.FileBrowse("Procurar...", file_types=(("CSV Files", "*.csv *.CSV"),))
        ],
        [sg.P(), sg.Button("Exportar Planilha", size=20, font="Default 10 bold"), sg.P()]
    ]
    window = sg.Window("Calculadora de Cupons", layout)

    while True:
        event, values = window.read()
        if event == "Exportar Planilha":
            in_filepath = values["-FILE-"]
            meta, customers = scrap.report_data(in_filepath)
            out_filepath = write.spreadsheet(meta, customers, in_filepath)
            sg.popup('Arquivo exportado com sucesso')
            os.system(f'start "excel" "{out_filepath}"')

        if event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == '__main__':
    main()
