% 2. Using a U(0,1) (standard uniform) random number generator, generate the common discrete % probability distributions: 

% a. Bernoulli Distribution Bern(p), with parameter p ∈ (0, 1): 
%                     X = ( 0      1)
%                         ( 1-p     p) 


clear
p = input(‘give the probability:’);             % asking the user for the probability
N = input(give the number of simulations:’);    % and number of simulations
U = rand(1, N);                                 % generate a random number between 1 and N
X = (U < p);                                    % X is a vector
U_X = unique(X)                                 % keep only the unique values from X
n_X = hist(X, length(U_X));                     % draw the histogram
rel_freq = n_X / N
