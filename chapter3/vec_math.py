def elementwise_multiplication(vec_a, vec_b):
    res = []
    for a, b in zip(vec_a, vec_b):
        res.append(a * b)
    return res


def elementwise_addition(vec_a, vec_b):
    res = []
    for a, b in zip(vec_a, vec_b):
        res.append(a + b)
    return res


def vector_sum(vec_a):
    return sum(vec_a)


def vector_average(vec_a):
    return vector_sum(vec_a) / len(vec_a)


def vector_scalar(vec_a, vec_b):
    return vector_sum(elementwise_multiplication(vec_a, vec_b))
