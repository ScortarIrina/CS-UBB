clear
p = input('p = ');   % probability
N = input('N = ');   % number of simulations

for i = 1 : N
    X(i) = 0;
    while rand >= p
        X(i) = X(i) + 1;
    endwhile
endfor

K = 0 : 20;
U_X = unique(X);
n_X = hist(X, length(U_X));
rel_freq = n_X/N;

plot(U_X, rel_freq, "b*", K, geopdf(K, p), "r*")
legend("simulation", "geopdf")
