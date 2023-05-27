from collections.abc import Iterable
from abc_composite import AbsComposite
from functools import reduce
from datetime import date


class Tree(Iterable, AbsComposite):
    _members = []

    def __init__(self, members):
        self._members = members

    def __iter__(self):
        return iter(self._members)

    def get_oldest(self):
        def f(t1, t2):
            t1_, t2_ = t1.get_oldest(), t2.get_oldest()
            return t1_ if t1_.birthdate < t2_.birthdate else t2_

        return reduce(f, self, NullPerson())


class NullPerson(AbsComposite):
    name = None
    birthdate = date.max

    def get_oldest(self):
        return self
