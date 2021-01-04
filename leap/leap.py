def leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                result = True
            else:
                result = False
        else:
            result = True
    else:
        result = False

    return result

if __name__ == "__main__":
    print(leap_year(2012))
