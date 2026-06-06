a = [1,2,3,4]
b = [3,4,5,6]

# result = list(set(a) & set(b))
# print(result)

# alternative way 

result = []

for num in a :
    if num in b :
        result.append(num)

print(result)