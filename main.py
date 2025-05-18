a_str = input("Enter 'a' for a*b :")
a = int(a_str)
b_str = input("Enter 'b' for a*b :")
b = int(b_str)

def multiply_one_iteration(a,b):
    return a*b
result = multiply_one_iteration(a,b)
print("1 Iteration :", result)

def multiply_n_iterations(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

numbers = (a,b)
result = multiply_n_iterations(numbers)
print("N Iterations :", result)  