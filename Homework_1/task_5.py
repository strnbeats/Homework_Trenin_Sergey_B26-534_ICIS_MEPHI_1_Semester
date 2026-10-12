import numpy as np


def median_of_sorted(values):
    n = len(values)
    middle = n // 2
    if n % 2 == 1:
        return values[middle]
    return (values[middle - 1] + values[middle]) / 2


def get_quartiles(numbers):
    if len(numbers) == 0:
        raise ValueError("Список пуст")
    values = sorted(numbers)
    n = len(values)
    half = n // 2
    median = median_of_sorted(values)
    if n == 1:
        return median, median, median
    lower_half = values[:half]
    upper_half = values[n - half:]
    q1 = median_of_sorted(lower_half)
    q3 = median_of_sorted(upper_half)
    return q1, median, q3


def get_quartiles_numpy(numbers):
    if len(numbers) == 0:
        raise ValueError("Список пуст")
    values = np.sort(np.array(numbers, dtype=float))
    n = len(values)
    half = n // 2
    median = np.median(values)
    if n == 1:
        return median, median, median
    q1 = np.median(values[:half])
    q3 = np.median(values[n - half:])
    return q1, median, q3


def compare(numbers):
    own = get_quartiles(numbers)
    with_numpy = get_quartiles_numpy(numbers)
    same = True
    for i in range(3):
        if abs(own[i] - with_numpy[i]) > 1e-9:
            same = False
    print("Данные:", numbers)
    print("Свой расчет  (Q1, медиана, Q3):", own)
    print("Расчет numpy (Q1, медиана, Q3):", tuple(float(x) for x in with_numpy))
    print("Результаты совпадают:", same)
    print()


print("Правило: числа сортируются; для четного количества медиана - среднее двух центральных,")
print("данные делятся пополам; для нечетного количества центральный элемент в половины не входит.")
print("Q1 - медиана нижней половины, Q3 - медиана верхней половины.")
print()

compare([7, 15, 36, 39, 40, 41])
compare([1, 2, 3, 4, 5, 6, 7, 8, 9])
compare([3, 1, 2, 10, 8, 5, 4, 9])
compare([5, 3, 9, 1, 7])
compare([42])