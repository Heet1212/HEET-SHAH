import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

print(id(old_list[0]))
print(id(new_list[0]))

print("Old list:", old_list)
print("New list:", new_list)