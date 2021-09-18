import typing as t


def calc_avg(numbers: list[t.Union[int, float]]) -> float:
    if len(numbers) == 0:
        raise Exception('Empty lists are not allowed')
    sum: float = 0.0
    for number in numbers:
        sum += number
    return round(sum / len(numbers), 2)
