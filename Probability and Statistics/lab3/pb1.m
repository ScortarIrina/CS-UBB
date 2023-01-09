% 1. Let X have one of the following distributions: X ∈ N(μ,σ) (normal), X ∈ T(n) (Student), X ∈ χ2(n), 
% or X ∈ F(m,n) (Fischer). Compute the following:
% a) P(X ≤ 0) and P(X ≥ 0); 
% b)P(−1≤X≤1)andP(X≤−1or X≥1);
% c) the value xα such that P(X < xα) = α, for α ∈ (0,1) (xα is called the quan- tile of order α);
% d) the value xβ such that P(X > xβ) = β, for β ∈ (0,1) (xβ is the quantile of order 1 − β).


u = input("Please input miu: ");
o = input("Please input sigma: ");

printf("%f\n", normcdf(0, miu, sigma));
printf("%f\n", normcdf(1, miu, sigma) - normcdf(-1, miu, sigma));
alfa = input("Please input alfa: ");
printf("%f\n", norminf(alfa, miu, 0));
printf("%f\n", norminf(1 - alfa, miu, 0));
