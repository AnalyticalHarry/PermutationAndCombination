import math

#function to calculate the binomial coefficient (n choose k)
def binomial_coefficient(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

#binomial coefficient C(5, 2)
n = 5
k = 2
result = binomial_coefficient(n, k)
print(f"C({n}, {k}) = {result}")

#probability of getting exactly 3 heads in 5 coin tosses (Binomial Distribution)
n_coin_tosses = 5
k_heads = 3
probability_of_k_heads = binomial_coefficient(n_coin_tosses, k_heads) * (0.5 ** k_heads) * (0.5 ** (n_coin_tosses - k_heads))
print(f"Probability of getting exactly {k_heads} heads in {n_coin_tosses} coin tosses: {probability_of_k_heads:.4f}")

#number of ways to select a committee of 3 members from 8 people
n_total_people = 8
k_committee_members = 3
ways_to_select_committee = binomial_coefficient(n_total_people, k_committee_members)
print(f"Number of ways to select a committee of {k_committee_members} from {n_total_people} people: {ways_to_select_committee}")
