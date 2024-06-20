// When throwing a dice twice, what is the probability of getting exactly two 5's?

// function to calculate factorial
const factorial = (n) => {
    if (n === 0 || n === 1) {
        return 1;
    }
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
};

// function to calcualte binomial coefficient 
const binomial_coefficient = (n, k) => {
    return factorial(n) / (factorial(k) * factorial(n - k));
};

// function to calculate probability
const probability_exact_k_outcomes = (n, k, p) => {
    let coeff = binomial_coefficient(n, k);
    let probability = coeff * (p ** k) * ((1 - p) ** (n - k));
    return probability;
};

// number of rolls
let n = 2;
// number of specific outcoms
let k = 2;
// probability of rolling a 5 on a single roll
let p = 1/6; 
let prob = probability_exact_k_outcomes(n, k, p)  
console.log(`The probability of rolling exactly {k} 5's in {n} rolls is ${prob}`)



// Probability of getting exactly five 5's when throwing a dice five times
// numbe of dice rolls
let n = 5
// number of specific outcomes (rolling a 5)
let k = 5
// probability of rolling a specific number on a single roll
let p = 1/6
let prob = probability_exact_k_outcomes(n, k, p)  
console.log(`The probability of rolling exactly {k} 5's in {n} rolls is ${prob}`)
