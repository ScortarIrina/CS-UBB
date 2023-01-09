% 2. Using a U(0,1) (standard uniform) random number generator, generate the common discrete probability distributions:
% b. Binomial Distribution Bino(p)

clear
n = input('give the number of trials: ');        % number of trials in binomial distribution
p = input('give the probability: ');             % probability
N = input('give the number of simulations: ');   % number of simulations

% for each simulation, generate a random number and build a vector out of the results
for i = 1 : N
    U = rand(n, 1);
    X(i) = sum(U < p);
endfor

K = 0 : n;
U_X = unique(X);                % keep only the unique values from X
n_X = hist(X, length(U_X));     % draw the histogram
rel_freq = n_X/N;

% plot the graph containing the simulations and the binopdf
plot(U_X, rel_freq, "b*", K, binopdf(K, n, p), "r*")
legend("simulation", "binopdf")
