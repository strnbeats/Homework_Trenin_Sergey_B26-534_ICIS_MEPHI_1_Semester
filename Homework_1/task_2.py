VOWELS = "aeiouаеёиоуыэюя"


def vowel_ratio(text):
    letters = 0
    vowels = 0
    for char in text.lower():
        if char == " ":
            continue
        letters += 1
        if char in VOWELS:
            vowels += 1
    if letters == 0:
        return 0
    return vowels / letters


def find_best_string():
    best_text = None
    best_ratio = 0
    while True:
        text = input("Введите строку (END для завершения): ")
        if text == "END":
            break
        ratio = vowel_ratio(text)
        if best_text is None or ratio > best_ratio:
            best_text = text
            best_ratio = ratio
    if best_text is None:
        print("Строки не были введены")
    else:
        print("Найденная строка:", best_text)
        print("Отношение гласных к длине:", round(best_ratio, 4))
    return best_text, best_ratio


find_best_string()