from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_animals(self):
        animals = ['Dog', 'Cat', 'Wolf', 'Tiger']
        actual = fit_transform(animals)
        expected = [('Dog', [0, 0, 0, 1]),
                    ('Cat', [0, 0, 1, 0]),
                    ('Wolf', [0, 1, 0, 0]),
                    ('Tiger', [1, 0, 0, 0])]
        self.assertEqual(actual, expected)

    def test_drinks(self):
        drinks = ['Coca-cola', 'Fanta', 'Sprite']
        actual = fit_transform(drinks)
        expected = [('Coca-cola', [0, 0, 1]),
                    ('Fanta', [0, 1, 0]),
                    ('Sprite', [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_minidrinks(self):
        minidrinks = ['Coca-cola']
        actual = fit_transform(minidrinks)
        bigdrinks = [('Coca-cola', [0, 0, 1]),
                     ('Fanta', [0, 1, 0]),
                     ('Sprite', [1, 0, 0])]
        self.assertNotIn(actual, bigdrinks)

    def test_catch_exception(self):
        numbers = 123
        try:
            fit_transform(numbers)
        except TypeError:
            self.assertRaises(TypeError)
