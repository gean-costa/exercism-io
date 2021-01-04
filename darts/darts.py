from math import sqrt


def score(x, y):
    r = sqrt((x**2 + y**2))
    points = 0
    if r <= 10 and r > 5:
        points = 1
    elif r <= 5 and r > 1:
        points = 5
    elif r <= 1:
        points = 10

    return points
