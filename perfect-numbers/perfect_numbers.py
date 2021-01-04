def classify(number: int):
    if number < 1:
        raise ValueError("Number is not a positive integer.")

    aliquot_sum = sum([n for n in range(1, number) if number % n == 0])
    print(aliquot_sum)
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
