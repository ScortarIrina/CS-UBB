% 2. Using a U(0,1) (standard uniform) random number generator, generate the common discrete probability distributions:
% d. Pascal Distribution NB(n, p) 

clear
n = input('n = ');   % number of trials in bino
p = input('p = ');   % probability
N = input('N = ');   % number of simulations

for i = 1 : N
    for j = 1 : n
        X(j) = 0;
        while rand >= p
            X(j) = X(j) + 1;
        endwhile
    endfor
    Y(i) = sum(X);
endfor

K = 0 : 150;
U_Y = unique(Y);
n_Y = hist(Y, length(U_Y));
rel_freq = n_Y/N;

plot(U_Y, rel_freq, "b*", K, nbinpdf(K, n, p), "r*")
legend("neg.bino.", "geopdf")
