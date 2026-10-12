def split_increasing(numbers):
    groups = []
    if len(numbers) == 0:
        return groups, 0
    current = [numbers[0]]
    longest = 1
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current.append(numbers[i])
        else:
            groups.append(current)
            current = [numbers[i]]
        if len(current) > longest:
            longest = len(current)
    groups.append(current)
    return groups, longest


tests = [
    [1, 3, 5, 2, 4, 7, 1, 8],
    [1, 1, 1],
    [5, 4, 3],
    [1, 2, 3, 4],
    [7],
    [],
]

for data in tests:
    copy_before = data[:]
    groups, longest = split_increasing(data)
    print("Исходный список:", data)
    for group in groups:
        print(group)
    print("Длина самой длинной группы:", longest)
    print("Исходный список не изменен:", data == copy_before)
    print()