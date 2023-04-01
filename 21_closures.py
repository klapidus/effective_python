def sort_priority(numbers, group):
    def custom(x):
        if x in group:
            return 0, x
        return 1, x
    return sorted(numbers, key=custom)


numbers = [21, 3, 7, 1, 2, 444, 108]
group = [108, 21]

print('numbers', numbers)
print('group', group)
res = sort_priority(numbers, group)
print('sorted', res)


# this is a way to work with a state
class SortPriority:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in group:
            self.found = True
            return 0, x
        return 1, x


print('numbers', numbers)
print('group', group)
sorter = SortPriority(group)
# note that sorter is a callable, very nice!
res = sorted(numbers, key=sorter)
print('sorted', res)
print('found', sorter.found)
