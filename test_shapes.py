import unittest
import math
from shapes import area_circle, perimeter_circle, area_square, perimeter_square

class TestShapes(unittest.TestCase):
    def test_area_circle(self):
        self.assertAlmostEqual(area_circle(5), math.pi * 25)
        self.assertEqual(area_circle(0), 0)
        with self.assertRaises(ValueError):
            area_circle(-5)

    def test_perimeter_circle(self):
        self.assertAlmostEqual(perimeter_circle(5), 2 * math.pi * 5)
        self.assertEqual(perimeter_circle(0), 0)
        with self.assertRaises(ValueError):
            perimeter_circle(-5)

    def test_area_square(self):
        self.assertEqual(area_square(5), 25)
        self.assertEqual(area_square(0), 0)
        with self.assertRaises(ValueError):
            area_square(-5)

    def test_perimeter_square(self):
        self.assertEqual(perimeter_square(5), 20)
        self.assertEqual(perimeter_square(0), 0)
        with self.assertRaises(ValueError):
            perimeter_square(-5)

if __name__ == '__main__':
    unittest.main()