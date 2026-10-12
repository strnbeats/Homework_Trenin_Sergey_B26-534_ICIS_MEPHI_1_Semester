import random
from faker import Faker


def clean_word(word):
    result = ""
    for char in word:
        if char.isalnum():
            result += char
    return result.lower()


def get_words(text):
    words = []
    for part in text.split():
        word = clean_word(part)
        if word != "":
            words.append(word)
    return words


def analyze_text(path):
    sentence_count = 0
    total_words = 0
    longest_sentence = None
    longest_length = 0
    word_counts = {}
    current = ""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            for char in line:
                if char == "\n":
                    current += " "
                elif char == "." or char == "!" or char == "?":
                    words = get_words(current)
                    if len(words) > 0:
                        sentence_count += 1
                        total_words += len(words)
                        if len(words) > longest_length:
                            longest_length = len(words)
                            longest_sentence = current.strip() + char
                        for word in words:
                            if word in word_counts:
                                word_counts[word] += 1
                            else:
                                word_counts[word] = 1
                    current = ""
                else:
                    current += char
    if sentence_count == 0:
        return None
    top_word = None
    for word in word_counts:
        if top_word is None or word_counts[word] > word_counts[top_word]:
            top_word = word
    return {
        "sentences": sentence_count,
        "average_length": total_words / sentence_count,
        "longest_sentence": longest_sentence,
        "longest_length": longest_length,
        "top_word": top_word,
        "top_word_count": word_counts[top_word],
        "unique_share": len(word_counts) / total_words,
        "total_words": total_words,
    }


def generate_text(path, sentences_count=5000):
    if sentences_count < 5000:
        sentences_count = 5000
    fake = Faker()
    written = 0
    with open(path, "w", encoding="utf-8") as file:
        while written < sentences_count:
            line_size = random.randint(1, 4)
            parts = []
            for i in range(line_size):
                if random.random() < 0.7:
                    words_count = random.randint(3, 8)
                else:
                    words_count = random.randint(15, 35)
                sentence = fake.sentence(nb_words=words_count)
                sentence = sentence[:-1] + random.choice(".!?")
                parts.append(sentence)
                written += 1
            file.write(" ".join(parts) + "\n")


def print_result(result):
    if result is None:
        print("В файле нет предложений")
        return
    print("Количество предложений:", result["sentences"])
    print("Всего слов:", result["total_words"])
    print("Средняя длина предложения в словах:", round(result["average_length"], 2))
    print("Самое длинное предложение (слов: " + str(result["longest_length"]) + "):")
    print(result["longest_sentence"])
    print("Самое частое слово:", result["top_word"], "-", result["top_word_count"], "раз")
    print("Доля уникальных слов:", round(result["unique_share"], 4))


def run_small_test():
    text = "Hello world. Hello again, my friend! Is it a long sentence?\nNo, it is short.\nThe end\n"
    with open("small_7.txt", "w", encoding="utf-8") as file:
        file.write(text)
    result = analyze_text("small_7.txt")
    print("Проверка на маленьком файле")
    print_result(result)
    ok = (
        result["sentences"] == 4
        and result["total_words"] == 15
        and result["longest_length"] == 5
        and result["top_word"] == "hello"
    )
    print("Результат верный:", ok)
    print()


def run_empty_test():
    with open("empty_7.txt", "w", encoding="utf-8") as file:
        file.write("")
    print("Проверка на пустом файле")
    print_result(analyze_text("empty_7.txt"))
    print()


run_small_test()
run_empty_test()
generate_text("text_7.txt", 5000)
print("Проверка на большом файле")
print_result(analyze_text("text_7.txt"))