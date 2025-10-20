

def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    take 2 lists of integers or floats in input and returns a list
    of BMI values.
    """
    if height.__len__() != weight.__len__():
        raise AssertionError("array not equal")
    if height.__len__() == 0:
        raise AssertionError("empty array")
    if not isinstance(height[0], (int, float)) or not\
            isinstance(weight[0], (int, float)):
        raise AssertionError("Wrong type")
    bmi: list[int | float] = []
    for lenght, mass in zip(height, weight):
        bmi.append(mass/(lenght ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    accepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of booleans
    (True if above the limit).
    """
    if bmi.__len__() == 0:
        raise AssertionError("empty array")
    if not isinstance(bmi[0], (int, float)):
        raise AssertionError("Wrong type")
    array: list[bool] = []
    for values in bmi:
        array.append(values > limit)
    return array
