numbers = [21, 3, 7, 1, 2, 444, 108]
group = [108, 21]

def sort_priority(numbers, group):
    def custom(x):
        if x in group:
            return 0, x
        return 1, x
    return sorted(numbers, key=custom)

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
# a callable, which carries along a state
res = sorted(numbers, key=sorter)
print('sorted', res)
print('found', sorter.found)


# now, let's see how we can do this without clever tricks
def sort_brute_force(numbers, group):
    s1 = sorted(x for x in numbers
                if x in group)
    s2 = sorted(x for x in numbers
                if x not in group)
    return s1 + s2, True if len(s1) > 0 else False

print('numbers', numbers)
print('group', group)
res, found = sort_brute_force(numbers, group)
print('sorted', res)
print('found', found)


# another attempt
def sort_brute_force_fancy(numbers, group):
    d = {x: 0 if x in group else 1
         for x in numbers}
    found = 1 in d.values()
    d = sorted(d, key=lambda k: (d[k], k))
    return d, found

print('numbers', numbers)
print('group', group)
res, found = sort_brute_force_fancy(numbers, group)
print('sorted', res)
print('found', found)
