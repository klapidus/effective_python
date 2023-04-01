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
