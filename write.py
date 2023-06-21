import os
from typing import List

import pandas as pd

import labels

BASE_FMT = {
    'align': 'center',
    'valign': 'vcenter'
}

NAME_FMT = {
    'align': 'left',
    'valign': 'vcenter'
}

CURRENCY_FMT = {
    'align': 'left',
    'valign': 'vcenter',
    'num_format': 'R$ #,##0.00'
}


def spreadsheet(meta: dict, customers: List[dict], filepath: str) -> str:
    if not meta["valid"]:
        raise ValueError("ERRO: Relatório inválido")

    filedir = os.path.dirname(filepath)
    filename = f"{filedir}/relatorio_{meta['report_date'].replace(' ', '_as_').replace('/', '-').replace(':', '-')}.xlsx"
    sheet_name = f"{meta['start_date'].replace('/', '-')} até {meta['end_date'].replace('/', '-')}"
    df = pd.DataFrame(customers)
    df.rename(columns=labels.customer, inplace=True)

    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    df.to_excel(excel_writer=writer, index=False, sheet_name=sheet_name)
    wb = writer.book
    ws = writer.sheets[sheet_name]

    base = wb.add_format(BASE_FMT)
    name = wb.add_format(NAME_FMT)
    money = wb.add_format(CURRENCY_FMT)
    ws.set_column(0, 0, 12, base)
    ws.set_column(1, 1, 32, name)
    ws.set_column(2, 2, 16, base)
    ws.set_column(3, 3, 12, money)
    ws.set_column(4, 4, 22, base)

    writer.close()
    return filename
