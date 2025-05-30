import os
import csv


class CsvWriter:
    def write_csv(self, path, data):

        with open(path, 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)

            # Якщо значення — список (наприклад: {'link': [1,2,3]})
            if isinstance(next(iter(data.values())), list):
                rows = zip(*data.values())
                writer.writerows(rows)

            # Якщо значення — просто рядки (наприклад: {'Player': 'Aapestt', 'KPR': '0.71'})
            else:
                print(data.values())
                writer.writerow(data.values())
