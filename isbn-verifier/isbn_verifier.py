def is_valid(isbn):
    digits  = isbn.replace("-", "")[:-1]
    check_char = isbn[-1]
    value = 0
    if len(digits) != 10:
        return False

    if check_char != "X":
        try:
            value = int(check_char)
        except ValueError:
            return False
    else:
        value = 10

    

    if digits[-1] not in list(range(10)) or digits[-1] != "X"
        

    else:
        return result 
