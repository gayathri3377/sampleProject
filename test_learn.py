import unittest
from learn import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(list(fibonacci(0)), [])

    def test_one(self):
        self.assertEqual(list(fibonacci(1)), [0])

    def test_five(self):
        self.assertEqual(list(fibonacci(5)), [0, 1, 1, 2, 3])

    def test_ten(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(list(fibonacci(10)), expected)

    def test_generator_next(self):
        gen = fibonacci(4)
        self.assertEqual(next(gen), 0)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 2)
        with self.assertRaises(StopIteration):
            next(gen)


if __name__ == '__main__':
    unittest.main()
