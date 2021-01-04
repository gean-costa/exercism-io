def value(colors):
    bands = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    return int(str(bands[colors[0]]) + str(bands[colors[1]]))

if __name__ == "__main__":
    print(value(["Red", "Black"]))
    