import csv
from math import sqrt
import unittest


def format_data(csv_reader):
    l = []
    for row in csv_reader:
        l.append(row[:1] + list(map(int, row[1:])))

    return l


def read_csv(file_name):

    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        return format_data(csv_reader)


def circle_area(r):

    return 3.14 * r**2


def circle_perimetr(r):
    return 2 * 3.14 * r


def triangle_area(a):

    return (sqrt(3) / 4) * a**2


def triangle_perimetr(a):
    return a * 3


def square_area(a, b):
    return a * b


def square_perimetr(a, b):
    return 2 * (a + b)


def calc_area_perimetr(data):
    for row in data:
        figure_type = row[0]
        sides = row[1:]

        if figure_type == 'triangle':
            perimetr = triangle_perimetr(sides[0])
            area = triangle_area(sides[0])
        elif figure_type == 'square':
            perimetr = square_perimetr(sides[0], sides[1])
            area = square_area(sides[0], sides[1])
        elif figure_type == 'circle':
            perimetr = circle_perimetr(sides[0])
            area = circle_area(sides[0])
        else:
            print(f'Unknown shape type {figure_type}')
            continue

        str_sides = ', '.join(map(str, sides))
        print(
            f'For {figure_type} with sides {str_sides} {figure_type} perimetr = {perimetr}, area = {area}'
        )


class TestAreaPerimeterFunctions(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(3), 3.14 * 3**2)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimetr(3), 2 * 3.14 * 3)

    def test_triangle_area(self):
        self.assertAlmostEqual(triangle_area(4), (sqrt(3) / 4) * 4**2)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimetr(4), 3 * 4)

    def test_square_area(self):
        self.assertEqual(square_area(4, 5), 4 * 5)

    def test_square_perimeter(self):
        self.assertEqual(square_perimetr(4, 5), 2 * (4 + 5))

    def test_format_data(self):
        csv_data = [['circle', '3'], ['triangle', '4'], ['square', '4', '5']]
        result = format_data(csv_data)
        self.assertEqual(result, [['circle', 3], ['triangle', 4], ['square', 4, 5]])


if __name__ == "__main__":
    data_csv = read_csv('lab2/csv.csv')
    calc_area_perimetr(data_csv)
