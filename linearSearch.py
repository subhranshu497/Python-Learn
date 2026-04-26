tup=[1,4,9,16,25,36,49,64,81,100]
x = int(input("Enter a number: "))
for num in tup:
    if num == x:
        print("Num found in the tuple.")
        break
else:
    print("Num not found in the tuple.")