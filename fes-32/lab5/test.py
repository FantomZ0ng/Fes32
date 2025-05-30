import unittest
from math import sqrt
from figures import Circle, Triangle, Square, Cube
from managers import FigureManager, FigureCreator


class TestShapes(unittest.TestCase):

    def test_circle(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 3.14 * 5**2)
        self.assertAlmostEqual(circle.perimetr(), 2 * 3.14 * 5)

    def test_triangle(self):
        triangle = Triangle(6)
        self.assertAlmostEqual(triangle.area(), (sqrt(3) / 4) * 6**2)
        self.assertEqual(triangle.perimetr(), 6 * 3)

    def test_square(self):
        square = Square(4, 5)
        self.assertEqual(square.area(), 4 * 5)
        self.assertEqual(square.perimetr(), 2 * (4 + 5))

    def test_cube(self):
        cube = Cube(3)
        self.assertEqual(cube.area(), 6 * 3**2)
        self.assertEqual(cube.perimetr(), 12 * 3)
        self.assertEqual(cube.volume(), 3**3)


class TestFigureCreator(unittest.TestCase):

    def setUp(self):
        self.fm = FigureManager()
        self.fm.add_figure('circle')(Circle)
        self.fm.add_figure('triangle')(Triangle)
        self.fm.add_figure('square')(Square)
        self.fm.add_figure('cube')(Cube)
        self.fc = FigureCreator(self.fm)

    def test_create_circle(self):
        circle = self.fc.create_figure('circle', [5])
        self.assertIsInstance(circle, Circle)
        self.assertEqual(circle.radius, 5)

    def test_create_triangle(self):
        triangle = self.fc.create_figure('triangle', [6])
        self.assertIsInstance(triangle, Triangle)
        self.assertEqual(triangle.side, 6)

    def test_create_square(self):
        square = self.fc.create_figure('square', [4, 5])
        self.assertIsInstance(square, Square)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 5)

    def test_create_cube(self):
        cube = self.fc.create_figure('cube', [3])
        self.assertIsInstance(cube, Cube)
        self.assertEqual(cube.side, 3)

    def test_invalid_figure(self):
        with self.assertRaises(ValueError):
            self.fc.create_figure('hexagon', [2])


if __name__ == "__main__":
    unittest.main()
