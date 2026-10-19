import re
import json
import logging
from collections import Counter

logging.basicConfig(
    filename="access_analysis.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

pattern = re.compile(
    r"^\S+\s+\S+\s+"
    r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+"
    r"(?P<method>[A-Z]+)\s+"
    r"(?P<url>\S+)\s+"
    r"(?P<status>\d{3})$"
)

methods = Counter()
urls = Counter()
errors_4xx = 0
total = 0

try:
    with open("access.log", "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            match = pattern.match(line.strip())

            if not match:
                logging.warning("Некорректная строка %s", line_number)
                continue

            data = match.groupdict()

            methods[data["method"]] += 1
            urls[data["url"]] += 1
            total += 1

            status = int(data["status"])

            if 400 <= status < 500:
                errors_4xx += 1

    result = {
        "requests_by_method": dict(methods),
        "errors_4xx": errors_4xx,
        "most_common_url": urls.most_common(1)[0][0] if urls else None,
        "total_requests": total
    }

    with open("access_stats.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)

    logging.info("Обработка завершена")
    print(json.dumps(result, ensure_ascii=False, indent=4))

except OSError as error:
    logging.exception("Ошибка обработки файла")
    print("Ошибка:", error)