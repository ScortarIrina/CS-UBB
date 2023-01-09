x1 = [46, 37, 39, 48, 47, 44, 35, 31, 44, 37];
x2 = [35, 33, 31, 35, 34, 30, 27, 32, 31, 31];

% a
% INPUT : x1 = the first data sample 
%         x2 = the second data sample 
%         alpha = the significance level
% OUTPUT: H = indicator which tells us if we reject or do not reject H_0
%         P = critical value of the test (p-value)
%         CI = confidence interval
%         stats = TS_0 TS when theta = theta0. If TS_0 is in RR => reject H0.

n1 = length(x1); 
n2 = length(x2);
% alpha = input('significance level alpha = ');

alpha = 0.05;

f1 = finv(alpha/2, n1 -1, n2-1);
f2 = finv(1 - alpha/2, n1 -1, n2-1); % quantiles for two-tailed test (for rejection region)

% The null hypothesis H0: sigma1^2 = sigma2^2
% The alt. hypothesis H1: sigma1^2 != sigma2^2
% case: two-tailed for comparing the variances

[H, P, CI, stats] = vartest2(x1, x2,"alpha", alpha);


fprintf('\na) Comparing variances\n')
fprintf('Two-tailed test for comparing variances\n')
if H == 0
    fprintf('H is %d\n', H)
    fprintf('So the null hypothesis is accepted,\n')
    fprintf('i.e. the variances seem to be equal\n')
    fprintf('the rejection region is (%6.4f, %6.4f) U (%6.4f, %6.4f)\n', -inf, f1, f2, inf)
    fprintf('the value of the test statistic is %6.4f\n', stats.fstat)
    fprintf('the P-value for the variances test is %6.4f\n', P)
else
    fprintf('H is %d\n', H)
    fprintf('So the null hypothesis is rejected,\n')
    fprintf('i.e. the variances seem to be different\n')
    fprintf('the rejection region is (%6.4f,%6.4f)U(%6.4f,%6.4f)\n', -inf, f1, f2, inf)
    fprintf('the value of the test statistic is %6.4f\n', stats.fstat)
    fprintf('the P-value for the variances test is %6.4f\n', P)
end

%b


% in our case, the population variances differ

% Difference of two population means
% We don't know sigma and we know they are not equal => it's the third case

% 95% confidence interval => 95 = 100(1-alpha) => alpha = 0.05

% compute the means
m1 = mean(x1); 
m2 = mean(x2);

% compute the variances
v1 = var(x1); 
v2 = var(x2); 

% compute c and n
c = (v1/n1)/(v1/n1+v2/n2);
n = 1/((c^2/(n1-1) + (1-c)^2/(n2-1)));

% and now the quantiles referring to the T(n) distribution
t1 = tinv(1-alpha/2, n);

% compute the limits of the confidence interval
limit1 = m1 - m2 - t1*sqrt((v1/n1)+(v2/n2));
limit2 = m1 - m2 + t1*sqrt((v1/n1)+(v2/n2));

fprintf('\nb) The confidence interval for the difference of the means is: (%6.4f,%6.4f)\n',limit1, limit2);
