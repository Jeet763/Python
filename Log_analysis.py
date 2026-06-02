logs = [
    "ERROR",
    "INFO",
    "ERROR",
    "WARNING",
    "INFO"
]

result = {}

for log in logs:
    if log not in result:
        result[log] = 1
    else:
        result[log] += 1

print(result)
