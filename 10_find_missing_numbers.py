ids = [1001,1002,1004,1005,1007]

missing=[]

for num in range(1001,1008):
    if num not in ids:
        missing.append(num)


print(missing)