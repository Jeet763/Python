nums = [2,7,11,15]
target = 9

seen = {}

for num in nums:
 needed = target - num

 if needed in seen:
  print((needed , num))
  break
 
 seen[num] = True

#  using set 

# nums = [2, 7, 11, 15]
# target = 9

# seen = set()

# for num in nums:

#     needed = target - num

#     if needed in seen:
#         print((needed, num))
#         break

#     seen.add(num)
