import re

text = """
alice@example.com
bob@test.org
alice@example.com
admin@company.ru
"""

emails = re.findall(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    text
)

for email in dict.fromkeys(emails):
    print(email)