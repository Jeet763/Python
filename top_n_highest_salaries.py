employees = {
    "A":50000,
    "B":70000,
    "C":60000
}

employees.items()

sorted_employees = sorted(
    employees.items(),
    key = lambda item: item[1],
    reverse= True
)

top_2 = sorted_employees[:2]
print(top_2)