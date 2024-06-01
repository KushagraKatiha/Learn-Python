def fact_using_recursion(num):
    if num == 1 or num == 0:
        return 1
    
    factorial = num * fact_using_recursion(num-1)
    return factorial

print(fact_using_recursion(5))