#import libaries
import itertools

#permutations are the arrangements of objects in a specific order.
#they are concerned with the order in which items are arranged.
#if you have a set of n distinct items and you want to arrange them in a specific order (the order matters), you are dealing with permutations.
#the number of permutations of n distinct items taken r at a time is denoted as P(n, r) or nPr and is calculated as n! / (n - r)!.
#function for permutations
def generate_permutations(elements, r):
    permutations = list(itertools.permutations(elements, r))
    return permutations

#combinations, on the other hand, are concerned with selecting items from a set without considering the order.
#if you have a set of n distinct items and you want to select a specific number of items from this set (e.g., for a group or a team), you are dealing with combinations.
#the number of combinations of n distinct items taken r at a time is denoted as C(n, r) or nCr and is calculated as n! / (r!(n - r)!).
#function for combinations
def generate_combinations(elements, r):
    combinations = list(itertools.combinations(elements, r))
    return combinations

#elements is a list representing the set of elements from which you want to generate permutations and combinations. In this specific example, elements is set to [1, 2, 3], so you are working with the elements 1, 2, and 3.
elements = [1, 2, 3]
r = 2

permutations = generate_permutations(elements, r)
combinations = generate_combinations(elements, r)

print("Permutations:")
for perm in permutations:
    print(perm)

print("\nCombinations:")
for comb in combinations:
    print(comb)
