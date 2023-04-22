from collections.abc import Sequence


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
# reversed returns a generator
print(reversed(cl))
for k in reversed(cl):
    print(k)
print(list(reversed(cl)))
print(cl.count(3))
print(cl.count(200))
