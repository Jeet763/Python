data = [1,2,3,4,2,5,6,3,7]

seen = set()
duplicates = set()

for num in data :
    
    if num in seen:
        duplicates.add(num)

    else:
        seen.add(num)

print(list(duplicates))