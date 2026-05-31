employees = [
    ("HR", "Alice"),
    ("IT", "Bob"),
    ("HR", "John"),
    ("IT", "Mike")
]

result = {}
 
for dept , emp in employees:
    if dept not in result:
        result[dept] = []
    
    result[dept].append(emp)

print(result)