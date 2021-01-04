def steps(number):
    if number < 1:
        raise ValueError("The given number is not positive greater than 0.")
    step = 0
    while number != 1:
        if number % 2 == 0:
            number = number/2
        else:
            number = number*3 + 1
        step += 1
    return step
