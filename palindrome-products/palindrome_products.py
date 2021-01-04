from itertools import combinations_with_replacement


def largest(max_factor, min_factor=0):
    if min_factor > max_factor:
        raise ValueError(
            "Invalid arguments. 'max_factor' must be greater than 'min_factor'.")

    factors = []
    values = []
    products = combinations_with_replacement(
        list(range(min_factor, max_factor+1)), 2)

    for i in products:
        if str(i[0]*i[1]) == str(i[0]*i[1])[::-1]:
            factors.append([i[0], i[1]])
            values.append(i[0]*i[1])

    val = max(values) if len(values) > 0 else None
    fac = [fac for fac in factors if fac[0]*fac[1] == val]

    return val, fac


def smallest(max_factor, min_factor=0):
    if min_factor > max_factor:
        raise ValueError(
            "Invalid arguments. 'max_factor' must be greater than 'min_factor'.")

    factors = []
    values = []
    products = combinations_with_replacement(
        list(range(min_factor, max_factor+1)), 2)

    for i in products:
        if i[0]*i[1] not in values and str(i[0]*i[1]) == str(i[0]*i[1])[::-1]:
            factors.append([i[0], i[1]])
            values.append(i[0]*i[1])

    val = min(values) if len(values) > 0 else None
    fac = [fac for fac in factors if fac[0]*fac[1] == val]

    return val, fac


if __name__ == "__main__":
    value, factors = smallest(min_factor=1, max_factor=9)
    print(value, factors)
    value, factors = largest(min_factor=1, max_factor=9)
    print(value, factors)
