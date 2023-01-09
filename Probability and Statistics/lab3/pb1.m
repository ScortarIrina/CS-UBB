% Compute P(X ≤ 0) and P(X ≥ 0) for the normal distribution X ∈ N(μ,σ)

u = input("Please input miu: ");
o = input("Please input sigma: ");

printf("%f\n", normcdf(0, miu, sigma));
printf("%f\n", normcdf(1, miu, sigma) - normcdf(-1, miu, sigma));
alfa = input("Please input alfa: ");
printf("%f\n", norminf(alfa, miu, 0));
printf("%f\n", norminf(1 - alfa, miu, 0));
