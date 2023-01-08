% In a study of the size of various computer systems, the random variable X, the number of files % stored (in hundreds of thousands), is considered. If a computer system cannot store at least 9, % on average, it doesn’t meet the efficiency standard and has to be replaced. These data are 
% obtained: 

%	 7     7    4    5    9    9
%	 4    12    8    1    8    7
%	 3    13    2    1   17    7
%	12     5    6    2    1   13
%	14    10    2    4    9   11 
%	  3    5   12    6   10    7

% a) Assuming that past experience indicates that σ = 5, at the 5% significance level, does the 
% data suggest that the standard is met? What about at 1%?


alpha = input("Input the significance level");
x = [7, 7, 4, 5, 9, 9, 4, 12, 8, 1, 8, 7, 3, 13, 2, 1, 17, 7, 12, 5, 6, 2, 1, 13, 14, 10, 2, 4, 9, 11, 3, 5, 12, 6, 10, 7];
n = length(x); 
% the null hypothesis H0: mu = 9
% the alternative hyp is H1: mu < 9
% left-tailed test for the mean when sigma is known

printf("Solving 1a)");
printf("Left-tailed test for mu when sigma is known");

mu = 9;
sigma = 5;

[h, p, ci, z, crit] = ztest(x, mu, sigma, "alpha", alpha, "tail", "left");

z2 = norminv(alpha) # tt_\alpha, the quantile of order \alpha
RR = [-inf, z2]; # from the cheatsheet 1a

printf("The value of H is %d\n", h);
if h == 1
    printf("The null hypothesis H0 is rejected\n");
    printf("The data suggests that the standard is not met\n"); % this depends on the problem
else
    printf("The null hypothesis H0 is not rejected\n");
    printf("The data suggests that the standard is met\n"); % this also
endif

printf("The rejection region is (%4.4f, %4.4f)\n", RR);
printf("The observed value of the test statistic is %4.4f\n", z);
printf("The P-value for the test is %4.4f\n", p);



% b) Without the assumption on sigma, does the data suggest that, on average, the number of files stored exceeds 5.5? (same significance level) 

alpha = input("Input the significance level");
x = [7, 7, 4, 5, 9, 9, 4, 12, 8, 1, 8, 7, 3, 13, 2, 1, 17, 7, 12, 5, 6, 2, 1, 13, 14, 10, 2, 4, 9, 11, 3, 5, 12, 6, 10, 7];
n = length(x); 
% the null hypothesis H0: mu = 9
% the alternative hyp is H1: mu < 9
% left-tailed test for the mean when sigma is known

printf("Solving 1a)");
printf("Left-tailed test for mu when sigma is known");

mu = 5.5;

[h, p, ci, stats] = ttest(x, mu, "alpha", alpha, "tail", "right");

TS0 = stats.tstat;
t2 = tinv(1 - alpha, n - 1) # tt_{1 - alpha}, the quantile of order 1 - \alpha
# n - 1 from the law T(n-1)
RR = [t2, inf]; # from the cheatsheet 1a

printf("The value of H is %d\n", h);
if h == 1
    printf("The null hypothesis H0 is rejected\n");
    printf("The data suggests that the standard is not met\n"); % this depends on the problem
else
    printf("The null hypothesis H0 is not rejected\n");
    printf("The data suggests that the standard is met\n"); % this also
endif

printf("The rejection region is (%4.4f, %4.4f)\n", RR);
printf("The observed value of the test statistic is %4.4f\n", stats.tstat);
printf("The P-value for the test is %4.4f\n", p);
