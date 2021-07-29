from typing import List, Literal
from math import sqrt, pi


def sCircle(r:int) -> float:
    return round(pi * r**2, 2)


def sRectangle(a:int, b:int) -> float:
    return round(a * b, 2)


def sTriangle(a:int, b:int, c:int) -> float:
    p = float(a + b + c) / 2

    return round(sqrt(p*(p-a)*(p-b)*(p-c)), 2)


def main(figure: Literal['circle', 'rectangle', 'triangle'], sides: List[int]) -> float:
    if figure == "circle":
        return sCircle(sides[0])
    if figure == "rectangle":
        return sRectangle(sides[0], sides[1])
    if figure == "triangle":
        return sTriangle(sides[0], sides[1], sides[2])


if __name__ == '__main__':
    print(main('circle', [4]))