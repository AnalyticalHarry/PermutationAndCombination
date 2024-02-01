#Number of permutations and combinations for a 3-digit key where each digit can vary from 0 to 9

#function for factorial
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

#total number of options for each digit (0 to 9)
n = 10

#number of digits in the key
r = 3

#permutations
def calculate_permutations(n, r):
    #Permutations P(n, r) = n! / (n - r)!
    #P(10, 3) = 10! / (10 - 3)! = 10! / 7! = 720 permutations
    return factorial(n) // factorial(n - r)

#combinations
def calculate_combinations(n, r):
    #Combinations C(n, r) = n! / (r!(n - r)!)
    #C(10, 3) = 10! / (3!(10 - 3)!) = 120 combinations
    return factorial(n) // (factorial(r) * factorial(n - r))

#calling function 
permutations = calculate_permutations(n, r)
combinations = calculate_combinations(n, r)
print(f"Permutations: {permutations}")
print(f"Combinations: {combinations}")
