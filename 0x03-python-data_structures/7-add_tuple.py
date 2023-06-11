def add_tuple(tuple_a=(), tuple_b=()):
    sum0 = 0
    sum1 = 0

    if len(tuple_a) == 0:
        a_0 = 0
        a_1 = 0
    elif len(tuple_a) == 1:
        a_0 = tuple_a[0]
        a_1 = 0
    else:
        a_0 = tuple_a[0]
        a_1 = tuple_a[1]

    if len(tuple_b) == 0:
        b0 = 0
        b1 = 0
    elif len(tuple_b) == 1:
        b0 = tuple_b[0]
        b1 = 0
    else:
        b0 = tuple_b[0]
        b1 = tuple_b[1]

    sum0 = a_0 + b0
    sum1 = a_1 + b1

    return (sum0, sum1)
