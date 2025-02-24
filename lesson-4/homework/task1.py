list1 = [1, 1, 2]
list2 = [2, 3, 4]
combine = list1 + list2
common_elements = set(list1).intersection(list2)
result = []
for x in combine:
    if x not in common_elements:
        result.append(x)

print(result)