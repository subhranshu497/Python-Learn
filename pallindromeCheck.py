list=[1,2,3,2,1]
copy_list = list.copy()
rev = reverse(copy_list)
if list==rev:
    print("The list is a palindrome")
else:    print("The list is not a palindrome")