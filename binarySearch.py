tup =[1,4,9,16,25,36,49,64,81,100]
l=0
r=len(tup)-1
x = int(input("Enter a number: "))
while l <= r:
    mid = l+int((r-l)/2)
    print("Current mid index: ", mid)
    if tup[mid] == x:
        print("Found at index: ", mid)
        break
    elif tup[mid] < x:
        l = mid + 1
    else:
        r = mid - 1
else:
    print("Not found in the list.")
