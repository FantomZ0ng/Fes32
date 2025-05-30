import csv


class CSVReader:

    def read_csv(self, file_name):

        with open(file_name, 'r', encoding='utf8') as file:
            csv_reader = csv.reader(file)
            return [[row[0], *map(int, row[1:])] for row in csv_reader if row]