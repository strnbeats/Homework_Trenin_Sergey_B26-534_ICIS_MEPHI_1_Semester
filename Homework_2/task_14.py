from contextlib import contextmanager


@contextmanager
def log_operation(filename, description):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"START: {description}\n")

    try:
        yield

    except Exception:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"ERROR: {description}\n")
        raise

    else:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"END: {description}\n")


with log_operation("operation.log", "Data processing"):
    print("Обработка данных")