def print_list_rec(lst : list, index : int = 0):
    #base case
    if index == len(lst):
        return
    print(lst[index], end=' ')
    print_list_rec(lst, index+1)

print()
print_list_rec([1, 2, 3, 4, 5])
print()
print_list_rec(['a', 'b', 'c', 'd', 'e'])
print()