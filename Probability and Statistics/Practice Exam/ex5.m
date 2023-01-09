x1 = [4.6 0.7 4.2 1.9 4.8 6.1 4.7 5.5 5.4];
x2 = [2.5 1.3 2.0 1.8 2.7 3.2 3.0 3.5 3.4];

n1 = length(x1); n2 = length(x2);
alpha = input('significance level alpha = ');
m1 = mean(x1); m2 = mean(x2);
v1 = var(x1); v2 = var(x2); 

f1 = finv(alpha/2, n1 - 1, n2 - 1);
f2 = finv(1 - alpha/2, n1 - 1, n2 - 1); % quantiles for two-tailed test (for rejection region)

% The null hypothesis H0: sigma1^2 = sigma2^2
% The alt. hypothesis H1: sigma1^2 != sigma2^2
[h, p, ci, stats] = vartest2(x1, x2, "alpha", alpha);

m1 = mean(x1); m2 = mean(x2);
mdiff = m1 - m2;
v1 = var(x1); v2 = var(x2);

fprintf('\n part a. Comparing variances\n')
fprintf('Two-tailed test for comparing variances\n')
if h==0
    fprintf('h is %d\n', h)
    fprintf('So the null hypothesis is not rejected,\n')
    fprintf('i.e. the variances seem to be equal\n')
    fprintf('the rejection region for F is (%6.4f, %6.4f) U (%6.4f, %6.4f)\n', -inf, f1, f2, inf)
    fprintf('the value of the test statistic F is %6.4f\n', stats.fstat)
    fprintf('the P-value for the variances test is %6.4f\n', p)

    sp = sqrt(((n1 - 1) * v1 + (n2 - 1) * v2)/(n1 + n2 - 2)); % pooled std. dev.
    n = n1 + n2 - 2;
    q = tinv(1 - alpha / 2, n);
    m1 = mdiff - q * sp * sqrt(1/n1 + 1/n2);
    m2 = mdiff + q * sp * sqrt(1/n1 + 1/n2);
    fprintf('a) Conf. interval for diff. of means, variances equal (m1, m2) = (%4.3f, %4.3f)\n',m1, m2)

else
    fprintf('h is %d\n', h)
    fprintf('So the null hypothesis is rejected,\n')
    fprintf('i.e. the variances seem to be different\n')
    fprintf('the rejection region for F is (%6.4f,%6.4f)U(%6.4f,%6.4f)\n', -inf, f1, f2, inf)
    fprintf('the value of the test statistic F is %6.4f\n', stats.fstat)
    fprintf('the P-value for the variances test is %6.4f\n', p)

    c = (v1 / n1)/(v1 / n1 + v2/n2);
    nn=1/(c^2/(n1-1)+(1-c)^2/(n2-1));
    rad=sqrt(v1/n1+v2/n2);
    qq=tinv(1 - alpha/2, nn);

    li=mdiff-qq*rad;
    ri=mdiff+qq*rad;

    fprintf('b) Conf. interval for diff. of means, variances not equal (li, ri) = (%4.3f, %4.3f)\n',li, ri)


end
