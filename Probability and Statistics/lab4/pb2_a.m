% 2. Using a U(0,1) (standard uniform) random number generator, generate the common discrete % probability distributions: 

% a. Bernoulli Distribution Bern(p), with parameter p ∈ (0, 1): X = (   0      1)
%								          ( 1-p     p) 


clear
p = input(‘give the probability:’);
N = input(give the number of simulations:’);
U = rand(1, N);
X = (U < p);
U_X = unique(X)
n_X = hist(X, length(U_X));
rel_freq =n_X / N
