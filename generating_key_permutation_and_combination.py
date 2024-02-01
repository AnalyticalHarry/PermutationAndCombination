#importing permutations and combiantions 
from itertools import permutations, combinations

#creating function to generate values for permutations and combinations 
def generate_permutations_and_combinations(digits, r):
    #list of permutations and combinations using itertools
    all_permutations = list(permutations(digits, r))
    all_combinations = list(combinations(digits, r))

    #printing all permutations
    print("All Permutations:")
    for i in all_permutations:
        print(i)

    #printing all combinations
    print("\nAll Combinations:")
    for j in all_combinations:
        print(j)

    #total number of permutations and combinations
    total_permutations = len(all_permutations)
    total_combinations = len(all_combinations)
    print(f"\nTotal Permutations: {total_permutations}")
    print(f"Total Combinations: {total_combinations}")

#digits from (0 to 9)
digits = list(range(10))

#number of digits in the key
r = 3

#call the function 
generate_permutations_and_combinations(digits, r)
