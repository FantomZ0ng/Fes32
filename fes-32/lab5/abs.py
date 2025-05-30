from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    def __str__(self):
        fig_name = self.__class__.__name__
        str_sides = self.__dict__

        return (
            f'{fig_name}: {str_sides} prmtr = {self.perimetr()}, area = {self.area()}'
        )


class SolidShape(Shape):

    @abstractmethod
    def volume(self):
        pass

    def __str__(self):

        return super().__str__() + f', volume = {self.volume()}'
