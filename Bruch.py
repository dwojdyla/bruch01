"""This module representantes a Bruch engl. fraction"""
from __future__ import division, print_function, unicode_literals

class Bruch(object):
    """ Bruch

    This class acts like a full functional fraction object
    so you can invoke all youre favourite fraction operations and
    maybe try some new ones.

    - **Included Functions**

       :func:`__add__`, :func:`__iadd__`, :func:`__radd__`:  Addition

       :func:`__sub__`, :func:`__isub__`, . :func:`__rsub__`: Substrtaction

       :func:`__mul__`, . :func:`__imul__`, . :func:`__rmul__`:   Multiplikation

       :func:`__truediv__`, . :func:`__itruediv__`, . :func:`__rdiv__`, . :func:`__rdiv__`: Division

       :func:`__pow__`:  Exponent

       :func:`__iter__`:   Iteration

       :func:`__abs__`:  Absolute

       :func:`__float__`, :func:`__int__`:  Type Conversion

    - **How to** use the class
        :Example: Multiplicatio  of two fractions

    """
    def __iter__(self):
        return (self.zaehler, self.nenner).__iter__()

    def __init__(self, zaehler=0, nenner=1):
        """
        construktor


        :raise TypeError: conflicting types, incompatible types

        """

        if isinstance(zaehler, Bruch):
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner
            return
        elif type(zaehler) is not int or type(nenner) is not int:
            raise TypeError('incompatible types:' + type(zaehler).__name__)
        elif nenner == 0:
            raise ZeroDivisionError
        self.zaehler = zaehler
        self.nenner = nenner



    def __str__(self):
        """
        converts Object to a String

        :return: object displayed as string

        """
        reduced = Bruch.reduce(self.zaehler, self.nenner)
        self.zaehler //= reduced
        self.nenner //= reduced
        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1

        if self.nenner == 1:
            return "(%d)" % self.zaehler
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)

    def __add__(self, value):
        """
        add


        :return: Bruch

        """
        # temp --> temporary used
        temp = Bruch()
        if type(value) is int:
            temp.zaehler = value
            temp.nenner = 1
        elif isinstance(value, Bruch):
            temp = value
        else:
            raise TypeError('conflicting types, incompatible types' + type(value).__name__)
        return Bruch(self.zaehler * temp.nenner + temp.zaehler * self.nenner, self.nenner * temp.nenner)

    def __iadd__(self, other):
        """
        iadd


        :return: Object of Bruch

        """
        tmp = Bruch.__makeBruch(other)
        self = self + tmp
        return self

    def __radd__(self, other):
        """
        object of Bruch is on the right hand side


        :return: Bruch

        """
        tmp = Bruch.__makeBruch(other)
        self = self + tmp
        return self

    def __eq__(self, other):
        """
        compare two fractions with each other


        :return: True or False whether they are equal

        """
        if type(other) is int:
            other = Bruch(other, 1)

        if not isinstance(other, Bruch):
            raise TypeError('conflicting types, incompatible types' + type(other).__name__ + "should be" + type(self))
        else:
            return (self.zaehler * other.nenner) == (self.nenner * other.zaehler)

    def __float__(self):
        """
        returns the Fraction as float

        :return: float

        """
        return self.zaehler / self.nenner


    def __rdiv__(self, other):
        """
        divides two fractions and returns the result


        :return: Bruch

        """

        if self.zaehler == 0:
            raise ZeroDivisionError("Not 0 pls")

        if type(other) is int and not 0:
            temp = Bruch(other, 1)
            return Bruch(self.zaehler * temp.nenner, self.nenner * temp.zaehler)
        elif isinstance(other, Bruch):
            if other.zaehler != 0:
                return Bruch(self.zaehler * other.nenner, self.nenner * other.zaehler)
            else:
                raise ZeroDivisionError("Dont use zero")
        else:
            raise TypeError("incompatible types"+ type(other).__name__);



    def __rtruediv__(self, other):
        """
        divides two fractions and returns the result


        :return: self

        """
        if type(other) is int:
            z2 = other * self.nenner
            if self.zaehler == 0:
                raise ZeroDivisionError
            return Bruch(z2, self.zaehler)
        else:
            raise TypeError('incompatible types:'+type(other).__name__)

    def __itruediv__(self, other):
        """

        :return: self
        """
        if not isinstance(other, Bruch) and not type(other) == int:
            raise TypeError(" incompatible types"+ type(other).__name__);
        return self / other

    def __truediv__(self, other):
        """
        truediv


        :return: self
        """
        return self.__rdiv__(other)

    def __iter__(self):
        """
        Make iteration available

        :return: iterator
        """
        iter = (self.zaehler, self.nenner).__iter__()
        return iter

    def __mul__(self, other):
        """
        :return: Bruch
        """
        if type(other) is int:
            return Bruch(self.zaehler * other, self.nenner)
        elif isinstance(other, Bruch):
            return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)
        else:
            raise TypeError("incompatible types"+ type(other).__name__)

    def __imul__(self, other):
        """
        equivalent to *=


        :return:
        """
        tmp = Bruch.__makeBruch(other)
        self = self * tmp
        return self

    def __rmul__(self, other):
        """
        right multiplikation


        :return: self
        """
        return self.__mul__(other)

    def __sub__(self, value):
        """
        make Substraktion available


        :return:
        """
        # temp --> temporary used
        temp = Bruch()
        if type(value) is int:
            temp.zaehler = value
            temp.nenner = 1
        elif isinstance(value, Bruch):
            temp = value
        else:
            raise TypeError('incompatible types' + type(value).__name__)
        return Bruch(self.zaehler * temp.nenner - temp.zaehler * self.nenner, self.nenner * temp.nenner)

    def __isub__(self, other):
        """
        isub equivalent to -=


        :return: self
        """
        tmp = Bruch.__makeBruch(other)
        self = self - tmp
        return self

    def __rsub__(self, value):
        """
        right version of substraktion

        :return: Bruch
        """
        # temp --> temporary used
        temp = Bruch()
        if type(value) is int:
            temp.zaehler = value
            temp.nenner = 1
        elif isinstance(value, Bruch):
            temp = value
        else:
            raise TypeError('incompatible types' + type(value).__name__)
        return Bruch(temp.zaehler * self.nenner - self.zaehler * temp.nenner, self.nenner * temp.nenner)

    def __ge__(self, other):
        """
        :return: self
        """
        if not isinstance(other, Bruch):
            raise TypeError("incompatible types"+ type(other).__name__)
        else:
            return self.zaehler * other.nenner >= self.nenner * other.zaehler

    def __gt__(self, other):
        """
        :return: self
        """
        if not isinstance(other, Bruch):
            raise TypeError("inc types")
        else:
            return self.zaehler * other.nenner >= self.nenner * other.zaehler

    def __abs__(self):
        """
        absolute value of bruch

        :return: Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __int__(self):
        """
        returns the float operation as int

        :return: int
        """
        return int(self.__float__())

    def __invert__(self):
        """
        invert the fraction object

        :return: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __neg__(self):
        """
        negation of the actual fraction

        :return: Bruch
        """
        return Bruch(self.zaehler * -1, self.nenner)

    def __pow__(self, power, modulo=None):
        """
        Takes the fraction to the power of power


        :return: Bruch
        """
        return Bruch(self.zaehler ** power, self.nenner ** power)

    def __makeBruch(value):
        """
        generates a new Bruch object


        :return: Bruch
        """
        if isinstance(value, Bruch):
            return value
        elif type(value) is int:
            b = Bruch(value, 1)
            return b
        else:
            raise TypeError('incompatible types:' + type(value).__name__)


    def reduce(a, b):
        """
        reduce the given Fraction


        :return: greatest common divisor
        """
        a = abs(a)
        b = abs(b)
        if a < b:
            a, b = b, a

        while b != 0:
            a, b = b, a % b
        return a
