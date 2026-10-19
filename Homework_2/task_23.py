import re

text = "Это   строка    с     большим    количеством   пробелов."

result = re.sub(r" {2,}", " ", text)
print(result)

text = "   Текст   с   пробелами   "

result = re.sub(r" {2,}", " ", text).strip()
print(result)