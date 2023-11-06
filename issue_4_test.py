from one_hot_encoder import fit_transform
import pytest


def test_animals():
    animals = ['Dog', 'Cat', 'Wolf', 'Tiger']
    expected = [('Dog', [0, 0, 0, 1]),
                ('Cat', [0, 0, 1, 0]),
                ('Wolf', [0, 1, 0, 0]),
                ('Tiger', [1, 0, 0, 0])]
    assert fit_transform(animals) == expected


def test_drinks():
    drinks = ['Coca-cola', 'Fanta', 'Sprite']
    expected = [('Coca-cola', [0, 0, 1]),
                ('Fanta', [0, 1, 0]),
                ('Sprite', [1, 0, 0])]
    assert fit_transform(drinks) == expected


def test_wrong_input():
    with pytest.raises(TypeError):
        fit_transform(123)


def test_countries():
    countries = ['Russia', 'USA', 'UK', 'Germany']
    expected = [('Russia', [0, 0, 0, 1]),
                ('USA', [0, 0, 1, 0]),
                ('UK', [0, 1, 0, 0]),
                ('Germany', [1, 0, 0, 0])]
    assert fit_transform(countries) == expected
