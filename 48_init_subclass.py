from abc import ABC, abstractmethod


import numpy as np


class TSBase(ABC):
    ndim = None

    def __init_subclass__(cls):
        super.__init_subclass__()
        if not 3 < cls.ndim < 10:
            raise ValueError("Number of dimensions is wrong!")
        # note, this can be achieved in a standard way
        # by defining an abstract method
        if "from_df" not in dir(cls):
            raise ValueError("from_df method must be implemented!")

    @classmethod
    @abstractmethod
    def from_xarray(cls):
        raise NotImplementedError


class TS(TSBase):
    ndim = 4

    def __init__(self, X: np.ndarray):
        self._X = X

    @classmethod
    def from_df(cls, df):
        cls(df.values())

    # is there a way to enforce this to be a class method?
    def from_xarray(self):
        print(f"From xarray {self._X}")


# the ValueError is raised, even though an object was not constructed
class DummyDF:
    def values(self):
        return np.full(3, 1.0)


TS.from_df(DummyDF())

ts = TS(np.full(3, 2.2))
