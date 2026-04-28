def sum_n_recursion(n: int) -> int:
    #base case
    if n==0:
        return 0
    return n +sum_n_recursion(n-1)

print(sum_n_recursion(5))