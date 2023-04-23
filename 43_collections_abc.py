from collections.abc import Sequence, Set


# must realize __len__ and __getitem__
# gets other methods for free:
# __reverse__
# __index__
# __count__
class CustomList(Sequence):
    def __init__(self, xs: list):
        self._data = xs
        self._access_count = 0

    def __len__(self):
        return len(self._data)

    def __getitem__(self, idx):
        self._access_count += 1
        return self._data[idx]

    def counts(self):
        return self._access_count

cl = CustomList([2, 3, 3, 7, 108, 2])
print(cl[3], cl[3])
print(cl.counts())

# realized by Sequence
print(cl.index(108))
print(cl.index(3))
print(cl.count(3))
print(cl.count(200))

# reversed returns a generator
print(reversed(cl))  # is a generator object
for k in reversed(cl):
    print(k)
print(list(reversed(cl)))


# note, however, that such operations as union, etc
# are not realized here
class SetTwice(Set):
    """Allows element to appear (only) twice in a set."""
    def __init__(self, xs: list):
        self._d = []
        counts = {}
        for x in xs:
            c = counts.get(x, 0) + 1
            if c <= 2:
                self._d.append(x)
            counts[x] = c

    def __contains__(self, item):
        return item in self._d

    def __iter__(self):
        yield from self._d

    def __len__(self):
        return len(self._d)


se = SetTwice([1, 2, 2, 3, 3, 3])
for el in se:
    print(el)

print("check and operation")
se2 = SetTwice([1, 3, 3, 3, 4, 4])
