def add_tuple(tuple_a=(), tuple_b=()):
    padded_tuple_a = tuple_a + (0, 0)
    padded_tuple_b = tuple_b + (0, 0)
    result = (padded_tuple_a[0] + padded_tuple_b[0], padded_tuple_a[1] + padded_tuple_b[1])
    return result

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
