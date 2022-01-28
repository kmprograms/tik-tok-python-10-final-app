from collections import namedtuple
from typing import Final

# W jaki sposób w Python możesz utworzyć stałą?

# Python nie posiada możliwości tworzenia stałych
# w taki sposób jak np Java czy C# (słowa kluczowe
# const, final)
# Musimy zastosowac inne sposoby, żeby uzyskać
# taką funkcjonalność ;)

# 1,
# Możesz napisac funkcję, która zwraca określoną
# wartość:
def MY_CONST():
    return "KMPROGRAMS"

# 2.
# Możesz pogrupować funkcje w klasy i stworzyć
# zbiór stałych
class Color:
    @staticmethod
    def RED():
        return "RED"

    @staticmethod
    def GREEN():
        return "GREEN"

# 3.
# Możesz zastosować property w klasie
class Country:
    def __init__(self):
        self._POLAND = 'POLAND'

    @property
    def POLAND(self):
        return self._POLAND

    @POLAND.setter
    def POLAND(self, value):
        raise ValueError('Cannot be reassigned')

# 4.
# Możesz zastosować namedtuple
Number = namedtuple('Number', ['PI', 'E'])
number = Number(3.14, 2.718)



if __name__ == '__main__':
    print(MY_CONST())

    print(Color.RED())
    print(Color.GREEN())

    country = Country()
    print(country.POLAND)

    print(number.PI)
    print(number.E)

    # 5.
    # Jest jeszcze type checker Final
    # Informuje, że dana zmienna ma charakter
    # stałej i sugeruje, żeby jej nie zmieniać
    X: Final = 10
    X = 12