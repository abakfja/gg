"""
A class to handle color for my program
"""


class Color:
    def __init__(self, r: int, g: int, b: int):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.r = r
            self.g = g
            self.b = b
        else:
            raise ValueError('r, g, b values out of range')

    def __str__(self):
        return u"2;" + str(self.r) + ";" + str(self.g) + ";" + str(self.b)

    @property
    def s(self):
        return self.__str__()

    def generate(self, tp):
        if self.eq(tp):
            return u""
        self.r, self.g, self.b = tp
        return self.s

    def to_tuple(self):
        return self.r, self.g, self.b

    def eq(self, tp):
        return self.r == tp[0] and self.g == tp[1] and self.b == tp[2]

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b


class ForegroundColor(Color):
    def __str__(self):
        return u"\u001b[38;" + super(ForegroundColor, self).__str__() + u"m"


class BackgroundColor(Color):
    def __str__(self):
        return u"\u001b[48;" + super(BackgroundColor, self).__str__() + u"m"
