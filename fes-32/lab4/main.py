from math import sqrt


Figure = type(
    'Figure',
    (object,),
    {
        '__init__': lambda self, a, b=None: setattr(self, '__dict__', {'a': a, 'b': b, 'name': self.__class__.__name__}),
        '__str__': lambda self: f'{self.name} Іванець\n{self.name} Периметр/Довжина: {self.perimetr()}\n{self.name} Площа: {self.area()}',
    },
)


Circle123 = type(
    'Circle',
    (Figure,),
    {
        'area': lambda self: 3.14 * self.a**2,
        'perimetr': lambda self: 2 * 3.14 * self.a,
    },
)


Triangle = type(
    'Triangle',
    (Figure,),
    {
        'area': lambda self: (sqrt(3) / 4) * self.a**2,
        'perimetr': lambda self: self.a * 3,
    },
)


Square = type(
    'Square',
    (Figure,),
    {
        'area': lambda self: self.a * self.b,
        'perimetr': lambda self: 2 * (self.a + self.b),
    },
)


def func():
    obja, objb, objc = Circle123(2), Square(3, 5), Triangle(5)

    for i in (obja, objb, objc):
        print(i)


if __name__ == '__main__':
    func()
