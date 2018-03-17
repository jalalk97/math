from copy import deepcopy
from fractions import Fraction
from utils import to_fraction



class Vector(list):
    def __init__(self, arg=None):
        """
        Creates a new Vector from the argument
        Usage:
        >> Vector(), Vector(None) Vector([]) creates empty vector
        >> Vector([5, 6, 6.7, Fraction(5, 6)]) creates vector with elements as list
        """
        if arg is None:
            super().__init__()
        elif isinstance(arg, list):
            super().__init__(to_fraction(arg))
        elif isinstance(arg, Vector):
            self = deepcopy(arg)
        else:
            raise TypeError('Invalid argument type:', arg)

    def __getitem__(self, arg):
        """
        Uses the basic list indexing
        Usage:
        >> v[0] returns the firt element
        >> v[-1] returns the last element
        >> v[:] shallow copy of vector elements
        >> v[4:8] returns a sclice of the vectors element from 4 to 8
        """
        return super().__getitem__(arg)

    def __setitem__(self, arg, value):
        """
        Uses the basic list indexing to set values
        Usage:
        >>
        >>
        >>
        >>
        """

        value = to_fraction(value)
        super().__setitem__(arg, value)
