from typing import List

import config
import parse


def report_period(meta: dict, row: List[str]) -> dict:
    current = row[0].split(" ")
    meta["start_date"] = current[1]
    meta["end_date"] = current[3].strip(",")
    return meta


def customer_id(row: List[str]) -> dict:
    return {
        "code": row[1],
        "name": row[3],
        "phone": parse.numbers_only(row[-1])
    }


def customer_data(customer: dict, row: List[str]) -> dict:
    total_spent = float(
        row[-1].replace('.', '').replace(',', '.')
    )
    customer["total_spent"] = total_spent
    customer["equivalent_voucher_qty"] = int(total_spent // config.VOUCHER_EQUIV)
    return customer
