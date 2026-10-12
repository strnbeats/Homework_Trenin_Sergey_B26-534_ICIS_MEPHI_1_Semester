import random
import time
import functools


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("[время]", func.__qualname__, "-", round(end - start, 6), "сек")
        return result

    return wrapper


class DataSource:
    def get_data(self):
        raise NotImplementedError("Метод должен быть переопределен")


class ListSource(DataSource):
    def __init__(self, values):
        self.values = values

    @measure_time
    def get_data(self):
        return list(self.values)


class FileSource(DataSource):
    def __init__(self, path):
        self.path = path

    @measure_time
    def get_data(self):
        data = []
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                for line in file:
                    text = line.strip()
                    if text == "":
                        continue
                    try:
                        data.append(float(text))
                    except ValueError:
                        continue
        except FileNotFoundError:
            print("Файл не найден:", self.path)
        return data


class DataFilter:
    def apply(self, data):
        raise NotImplementedError("Метод должен быть переопределен")


class NegativeFilter(DataFilter):
    @measure_time
    def apply(self, data):
        result = []
        for value in data:
            if value >= 0:
                result.append(value)
        return result


class RangeFilter(DataFilter):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    @measure_time
    def apply(self, data):
        result = []
        for value in data:
            if self.low <= value <= self.high:
                result.append(value)
        return result


class DataAnalyzer:
    @measure_time
    def analyze(self, data):
        if len(data) == 0:
            return None
        minimum = data[0]
        maximum = data[0]
        total = 0
        for value in data:
            if value < minimum:
                minimum = value
            if value > maximum:
                maximum = value
            total += value
        mean = total / len(data)
        squares = 0
        for value in data:
            squares += (value - mean) ** 2
        std = (squares / len(data)) ** 0.5
        return {"count": len(data), "min": minimum, "max": maximum, "mean": mean, "std": std}


class ReportGenerator:
    @measure_time
    def generate(self, stats):
        if stats is None:
            return "Отчет\nПосле фильтрации данных не осталось\n"
        lines = [
            "Отчет по данным",
            "Количество значений: " + str(stats["count"]),
            "Минимум: " + str(round(stats["min"], 4)),
            "Максимум: " + str(round(stats["max"], 4)),
            "Среднее: " + str(round(stats["mean"], 4)),
            "Стандартное отклонение: " + str(round(stats["std"], 4)),
        ]
        return "\n".join(lines) + "\n"

    def save(self, text, path):
        with open(path, "w", encoding="utf-8") as file:
            file.write(text)


def run_pipeline(source, filters, analyzer, generator, output_path):
    data = source.get_data()
    for data_filter in filters:
        data = data_filter.apply(data)
    stats = analyzer.analyze(data)
    report = generator.generate(stats)
    generator.save(report, output_path)
    return stats, report


def generate_input_file(path, count=10000):
    if count < 10000:
        count = 10000
    with open(path, "w", encoding="utf-8") as file:
        for i in range(count):
            file.write(str(round(random.uniform(-50, 150), 3)) + "\n")
        file.write("не число\n")
        file.write("\n")


def run_small_test():
    print("Проверка на маленьком наборе")
    source = ListSource([10, -5, 20, 200, 30])
    filters = [NegativeFilter(), RangeFilter(0, 100)]
    stats, report = run_pipeline(source, filters, DataAnalyzer(), ReportGenerator(), "report_small_10.txt")
    print(report)
    ok = (
        stats["count"] == 3
        and stats["min"] == 10
        and stats["max"] == 30
        and stats["mean"] == 20
        and abs(stats["std"] - 8.164966) < 0.0001
    )
    print("Результат верный:", ok)
    print()


def run_empty_test():
    print("Проверка, когда все данные отфильтрованы")
    source = ListSource([-1, -2, 500])
    stats, report = run_pipeline(source, [NegativeFilter(), RangeFilter(0, 100)], DataAnalyzer(), ReportGenerator(), "report_empty_10.txt")
    print(report)


def run_large_test():
    print("Проверка на большом файле")
    generate_input_file("data_10.txt", 10000)
    source = FileSource("data_10.txt")
    filters = [NegativeFilter(), RangeFilter(0, 100)]
    stats, report = run_pipeline(source, filters, DataAnalyzer(), ReportGenerator(), "report_10.txt")
    print(report)


run_small_test()
run_empty_test()
run_large_test()