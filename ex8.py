formatter = '{} {} {} {}'

print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format('a', 'b', 'c', 'd'))

print(formatter.format([1], ['two'], 'three', 4))

print(formatter.format(True, False, True, False))

print(formatter.format(
    'First long string',
    'Second string',
    "3rd string",
    'Fourth string',
))