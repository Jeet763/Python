# d1 = {"a":1, "b":2}
# d2 = {"b":3, "c":4}

# # output- {"a":1, "b":5, "c":4}

# result = {}

# for key , value in d1.items():
#     result[key] = value

# for key, value in d2.items():
#     if key in result:
#         result[key] += value

#     else:
#         result[key] = value

# print(result)

d1 = {"a":1, "b":2}
d2 = {"b":3, "c":4}

result = {}

for key, value in d1.items():
    result[key] = value

for key, value in d2.items():
    result[key] = value

print(result)