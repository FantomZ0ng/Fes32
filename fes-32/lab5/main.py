from figures import fm
from csv_tools import CSVReader
from managers import FigureCreator, ProcessData



if __name__ == "__main__":
    reader = CSVReader()
    fc = FigureCreator(fm)
    pd = ProcessData(fc)

    data = reader.read_csv('lab5/csv.csv')
    results = pd.process_data(data=data)

    for figure in results:
        print(figure)
