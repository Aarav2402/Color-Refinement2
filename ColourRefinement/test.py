lists = [[55,56], [54,53,55], [57,58,55], [55,58,57], [55]], [[56,55], [55,58,57], [55], [55,57,58], [54,53,55]]

unique_lists = {}
index = 0
result = []

for lst in lists:
    unique_lst = tuple(sorted(lst))
    if unique_lst not in unique_lists:
        unique_lists[unique_lst] = index
        index += 1
    result.append(unique_lists[unique_lst])

print(result)