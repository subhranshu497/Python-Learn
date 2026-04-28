def fun_print_list(lst: list):
    for item in lst:
        print(item, end=' ')
    print()  # for a new line after printing the list
    

    ## call the function
fun_print_list([1, 2, 3, 4, 5])
fun_print_list(['a', 'b', 'c', 'd', 'e'])
fun_print_list([1, 'a', 3.14, True, None])