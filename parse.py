import csv
import re


def numbers_only(string: str) -> int:
    numbers = re.findall(r'\d+', string)
    return int(''.join(numbers)) if numbers else 0


def clean_csv_file(file_path: str):
    with open(file_path, 'r', encoding='windows-1252') as f:
        csv_reader = csv.reader(f)
        cleaned_data = []

        for row in csv_reader:
            cleaned_row = [cell for cell in row if cell]  # Ignore empty strings
            if cleaned_row:  # Ignore empty rows
                cleaned_data.append(cleaned_row)

    return cleaned_data
