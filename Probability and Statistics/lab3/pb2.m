% 1. Let X have one of the following distributions: X ∈ N(μ,σ) (normal), X ∈ T(n) (Student), 
% X ∈ χ2(n), or X ∈ F(m,n) (Fischer). Compute the following:
% a) P(X ≤ 0) and P(X ≥ 0); 
% b)P(−1≤X≤1)andP(X≤−1or X≥1);
% c) the value xα such that P(X < xα) = α, for α ∈ (0,1) (xα is called the quan- tile of order α);
% d) the value xβ such that P(X > xβ) = β, for β ∈ (0,1) (xβ is the quantile of order 1 − β).

% ~~~ STUDENT DISTRIBUTION ~~~

n = input("Please input n: ");
p = input("Please input p: ");
X = 0:1:n;
plot(X, binopdf(X, n, p), 'g');
hold on;
plot(X, normpdf(X, n * p, sqrt(n * p * (1 - p))), 'r');
hold on;
plot(X, poisspdf(X, n * p), 'b');
