def slices(series, length):
    if length > len(series):
        raise ValueError(
            "The given 'length' is greater than length of 'series'.")
    if length < 1:
        raise ValueError(
            "The argument 'length' must be greater than zero.")

    digit_series = [series[i:i+length]
                    for i in range(len(series)) if i+length <= len(series)]

    return digit_series
