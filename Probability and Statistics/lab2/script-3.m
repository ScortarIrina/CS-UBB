% 2. Plot the graphs of the pdf and the cdf of a random variable X having a binomial distribution of parameters n and p (given by the user).
% A coin is tossed 3 times. Let X denote the number of heads that appear.
% a) Find the probability distribution function of X. What type of distribution does X have?
% b) Find the cumulative distribution function of X, FX. c) Find P(X = 0) and P(X ̸= 1).
% d) Find P(X ≤ 2), P(X < 2).
% e) Find P(X ≥ 1), P(X > 1).
% f) Write a Matlab code that simulates 3 coin tosses and computes the value of the variable X.

% a) Bino(3, 0.5)
% P(X = 0) = binopdf(0, 3, 0.5)
%	0	1	2	3
%      1/8       3/8       3/8       1/8
binopdf(0:1:3, 3, 0.5)


% b) Find the cdf of X, FX 
binocdf(0:1:3, 3, 0.5)

% c) P(X = 0) and P(X != 1)
binopdf(0, 3, 0.5)
1 - binopdf(1, 3, 0.5)

% d) P(X ≤ 2) and P(X < 2)
binocdf(2, 3, 0.5);
binocdf(1, 3, 0.5);

% e) P(X ≥ 1) and P(X > 1)
1 - binocdf(0, 3, 0.5);
1 - binocdf(1, 3, 0.5);

% f) Write a Matlab code that simulates 3 coin tosses and computes the value of the variable X.
ans = 0;
for i = 1:3
    ans += (rand() <= 0.5);
endfor
printf("The result is %d\n", ans);

%N = input("N? ");
%C = rand(3, N);
%Y = (C < 0.5);
%X = sum(Y);
%hist(X);
