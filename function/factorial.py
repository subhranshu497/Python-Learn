def calculate_factorial(n : int)-> int:
    for num in range(n,1,-1):
        n *= num-1
    return n
print(calculate_factorial(5))
