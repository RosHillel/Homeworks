from functools import total_ordering


@total_ordering
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_square(self) -> float:
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() < other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        total_area = self.get_square() + other.get_square()
        new_width = self.width + other.width
        new_height = total_area / new_width
        return Rectangle(new_width, new_height)

    def __mul__(self, n: float):
        new_width = self.width * n
        new_height = self.height
        return Rectangle(new_width, new_height)

    __rmul__ = __mul__

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


if __name__ == "__main__":
    r1 = Rectangle(2, 4)
    r2 = Rectangle(3, 6)
    assert r1.get_square() == 8, 'Test1'
    assert r2.get_square() == 18, 'Test2'

    r3 = r1 + r2
    assert abs(r3.get_square() - 26) < 1e-6, 'Test3'

    r4 = r1 * 4
    assert abs(r4.get_square() - 32) < 1e-6, 'Test4'

    assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'


    assert (Rectangle(2, 5) < Rectangle(3, 4))
    assert (Rectangle(2, 5) <= Rectangle(2, 5))
    assert (Rectangle(3, 4) > Rectangle(2, 5))
    assert (Rectangle(3, 4) >= Rectangle(2, 5))

    print("Всі тести пройдені!")