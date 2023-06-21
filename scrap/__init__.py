import parse
from . import content


def report_data(filepath: str) -> tuple:
    cleaned_data = parse.clean_csv_file(filepath)
    meta = {"valid": False}
    customers = []
    customer = dict()

    for row in cleaned_data:
        if "Relatório: 4 - Vendas para Clientes - " == row[0]:
            meta["report_date"] = row[1]
            continue

        if "Relatorio Sintético de Vendas por Cliente" == row[0]:
            meta["valid"] = True
            continue

        if "Data: " in row[0]:
            meta = content.report_period(meta, row)
            continue

        if "Cliente:" == row[0]:
            customer = content.customer_id(row)
            continue

        if "Total do Cliente:." == row[0]:
            customer = content.customer_data(customer, row)
            customers.append(customer)
            continue

    return meta, customers
