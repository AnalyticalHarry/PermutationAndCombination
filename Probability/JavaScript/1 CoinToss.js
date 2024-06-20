// When throwing a dice twice, what is the probability of getting exactly two 5's?

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

const binomial_coefficient = (n, k) => {
    return factorial(n) / (factorial(k) * factorial(n - k));
};

const probability_exact_k_outcomes = (n, k, p) => {
    let coeff = binomial_coefficient(n, k);
    let probability = coeff * (p ** k) * ((1 - p) ** (n - k));
    return probability;
};

let n = 2;
let k = 2;
let p = 1/6; 
let prob = probability_exact_k_outcomes(n, k, p)  
console.log(`The probability of rolling exactly {k} 5's in {n} rolls is ${prob}`)
