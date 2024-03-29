% 1.
% A food store owner receives 1-liter bottles from two suppliers.
% After some complaints from customers, he wants to check the accuracy of
% the weigths of 1-liter water bottles. He finds the following weigths (the
% two populations are approximately normally distributed):

x = [1021, 980, 1017, 988, 1005, 998, 1014, 985, 995, 1004, 1030, 1015, 995, 1023];
y = [1070, 970, 993, 1013, 1006, 1002, 1014, 997, 1002, 1010, 975];

n1 = length(x);
n2 = length(y);     % length of each array
mx = mean(x);
my = mean(y);       % mean for each set of values
sx = var(x);
sy = var(y);        % variances for each set of values

alpha = 0.05;       % significance level

% a) At 5% significance level, do the population variances seem to differ?
% Null hypothesis: the population variances are equal.
% Alternative hypothesis: the population variances differ.

typea = 0;          % two tailed test
fprintf('a)\n')
fprintf('SIGNIFICANCE LEVEL %f:\n',alpha)
fprintf("We are doing a two-tailed test for variances.\n");
% find the rejection region
RR_Ftest(alpha, n1-1, n2-1, typea);                                
[ha, pa, cia, valstata] = vartest2(x, y, alpha, typea); 
f = sx / sy;
fprintf('The value of the test statistic f is %f (given by vartest2 %f).\n', f, valstata.fstat)
fprintf('The P-value of the test is %f.\n', pa)
    
if ha == 1
    fprintf('The null hypothesis is rejected (f in RR), i.e. the variances seem to be different.\n')
else
    fprintf('The null hypothesis is NOT rejected (f not in RR), i.e. the variances seem to be equal.\n')
end    

% b) At the same significance level, on average, does Supplier A seem to be more reliable?
% From a), we find if the variances of the populations are equal or not and we have to use this information here.
% In this case, the null hypothesis is that the means are equal.
% The alternative hypothesis is that the mean of the supplier A is greater than the one for supplier B.
    
fprintf('b)\n');
fprintf('SIGNIFICANCE LEVEL %f:\n', alpha)
fprintf('We are doing a right-tailed test for the difference of means.\n');
typeb = 1;          % right-tailed test 
if ha == 0 
   vartype = 'equal';
   n = n1 + n2 - 2;
   t = (mx - my) / sqrt((n1 - 1) * sx + (n2 - 1) * sy) * sqrt((n1 + n2 - 2) / (1 / n1 + 1 / n2));
else
   vartype = 'unequal';
   c = (sx / n1) / (sx / n1 + sy / n2);
   n = ceil(1 / (c^2 / (n1 - 1) + (1 - c)^2 / (n2 - 1)));
   t = (mx - my) / sqrt(sx / n1 + sy / n2);
end

% rejection region 
RR_Ttest(alpha, n, typeb);
[hb, pb, cib, valstatb] = ttest2(x, y, alpha, typeb, vartype);
fprintf('The value of the test statistc t is %f (given by ttest2 %f).\n', t, valstatb.tstat)
fprintf('The P-value of the test is %.10f.\n', pb)
if hb == 1
    fprintf('The null hypothesis is rejected (t in RR), i.e. Supplier A is more reliable.\n')
else
    fprintf('The null hypothesis is NOT rejected (t not in RR), i.e. Supplier A is not more reliable.\n')
end  


% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


% 2.
% A study is conducted to compare the total printing time in seconds of two
% brands of laser printers on serious tasks. Data below are for the printing
% of the charts (normality of the two populations is assumed);

x = [29.8, 30.6, 29.0, 27.7, 29.9, 29.6, 30.5, 31.1, 30.2, 28.1, 29.4, 28.5];
y = [31.5, 30.2, 31.2, 29.0, 31.4, 31.1, 32.5, 33.0, 31.3, 30.9, 30.7, 29.9];

n1 = length(x);
n2 = length(y);     % length of each array
mx = mean(x);
my = mean(y);       % mean for each set of values
sx = var(x);
sy = var(y);        % variances for each set of values

alpha = 0.05;       % significance level

% a) At 5% significance level, do the population variances seem to differ?
% Null hypothesis: the population variances are equal.
% Alternative hypothesis: the population variances differ.

typea = 0;                  % two-tailed test
fprintf('a)\n')
fprintf('SIGNIFICANCE LEVEL %f:\n', alpha)
fprintf("We are doing a two-tailed test for variances.\n");
RR_Ftest(alpha, n1-1, n2-1, typea);                             % find the rejection region
[ha, pa, cia, valstata] = vartest2(x, y, alpha, typea); 
f = sx / sy;
fprintf('The value of the test statistic f is %f (given by vartest2 %f).\n', f, valstata.fstat)
fprintf('The P-value of the test is %f.\n', pa)
    
if ha == 1
    fprintf('The null hypothesis is rejected (f in RR), i.e. the variances seem to be different.\n')
else
    fprintf('The null hypothesis is NOT rejected (f not in RR), i.e. the variances seem to be equal.\n')
end    


% b) At the same significance level, on average, does the Brand A printer seem to be faster?
% From a), we find if the variances of the populations are equal or not and
% we have to use this information here.
% In this case, the null hypothesis is that the means are equal.
% The alternative hypothesis is that the mean of the supplier A is greater
% than the one for supplier B.
    
fprintf('b)\n');
fprintf('SIGNIFICANCE LEVEL %f:\n', alpha)
fprintf('We are doing a right-tailed test for the difference of means.\n');
typeb=1;                % right-tailed test 

if ha == 0 
   vartype = 'equal';
   n = n1 + n2 - 2;
   t = (mx - my) / sqrt((n1 - 1) * sx + (n2 - 1) * sy) * sqrt((n1 + n2 - 2) / (1 / n1 + 1 / n2));
else
   vartype = 'unequal';
   c = (sx / n1) / (sx / n1 + sy / n2);
   n = ceil(1 / (c^2 / (n1 - 1) + (1 - c)^2 / (n2 - 1)));
   t = (mx - my) / sqrt(sx / n1 + sy / n2);
end

RR_Ttest(alpha, n, typeb);                              % rejection region 
[hb, pb, cib, valstatb] = ttest2(x, y, alpha, typeb, vartype);
fprintf('The value of the test statistc t is %f (given by ttest2 %f).\n', t, valstatb.tstat)
fprintf('The P-value of the test is %.10f.\n', pb)
    
if hb == 1
    fprintf('The null hypothesis is rejected (t in RR), i.e. Brand A seems to be faster.\n')
else
    fprintf('The null hypothesis is NOT rejected (t not in RR), i.e. Brand A seems to not be faster.\n')
end  


% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



% 3.
% Nickel powders are used in coatings used to shield electronic equipment.
% A random sample is selected and the sizes of nickel particles in each
% coating are recorded (they are assumed to be approximately normally
% distributed):

x = [3.26, 1.89, 2.42, 2.03, 3.07, 2.95, 1.39, 3.06, 2.46, 3.35, 1.56, 1.79, 1.76, 3.82, 2.42, 2.96];

n = length(x);
m = mean(x);
s = std(x);

% a) At the 5% significance level, on average, do these nickel particles seem to be smaller than 3?
% Null hypothesis: The mean is equal to 3. 
% Alternative hypothesis: The mean is smaller than 3.
    
m0 = 3;
fprintf('a)\n');
fprintf('We are doing a left-tailed test for the mean when we do not know the standard deviation.\n');
type =- 1;
alpha1 = 0.05;                               % significance level
fprintf('SIGNIFICANCE LEVEL %f:\n', alpha1)
[h, p, ci, valstat] = ttest(x, m0, alpha1, type);
t1 = (m - m0) / s * sqrt(n);
RR_Ttest(alpha1, n, type);
fprintf('The value of the test statistic t is %f (given by ttest %f).\n', t1, valstat.tstat);
fprintf('The P-value of the test is %.10f.\n', p)
    
if h == 1
    fprintf('The null hypothesis is rejected (t in RR), i.e. the nickel particles seem to be smaller than 3.\n')
else
    fprintf('The null hypothesis is not rejected (t not in RR), i.e. the nickel particles seem to not be smaller than 3.\n')
end

% b) Find a 99% confidence interval for the standard deviation of the size of the nickel particles.
    
fprintf('b)\n');
alpha2 = 0.01;
[li, ri] = ConfIntVar(x, alpha2);
fprintf('Confidence interval for the standard deviation:\n')
fprintf('(%.4f, %.4f)\n', sqrt(li), sqrt(ri))


% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



% 4.
% A study is conducted to compare heat loss in glass pipes versus steel pipes
% of the same size. Various liquids at identical starting temperatures are
% run through segments of each type and the heat loss (in Celsius) is
% measured. These data result (normality of the two populations is assumed):

x = [4.6, 0.7, 4.2, 1.9, 4.8, 6.1, 4.7, 5.5, 5.4];
y = [2.5, 1.3, 2.0, 1.8, 2.7, 3.2, 3.0, 3.5, 3.4];

n1 = length(x);
n2 = length(y);
mx = mean(x);
my = mean(y);
sx = var(x);
sy = var(y);

% a) At the 5% significance level, do the population variances seem to differ?
% Null hypothesis: the variances are equal.
% Alternative hypothesis: the variances are different.
    
fprintf('a)\n');
fprintf('We are doing a two-test for the variances.\n');
typea = 0;
alpha = 0.05;
RR_Ftest(alpha, n1-1, n2-1, typea);                     % find the rejection region
[ha, pa, cia, valstata] = vartest2(x, y, alpha, typea); 
f = sx / sy;
fprintf('The value of the test statistic f is %f (given by vartest2 %f).\n', f, valstata.fstat)
fprintf('The P-value of the test is %f.\n', pa)
    
if ha == 1
    fprintf('The null hypothesis is rejected (f in RR), i.e. the variances seem to be different.\n')
else
    fprintf('The null hypothesis is NOT rejected (f not in RR), i.e. the variances seem to be equal.\n')
end    


% b) At the same significance level, does it seem that on average, steel pipes lose more heat than glass pipes?
% Null hypothesis: the means are equal.
% Alternative hypothesis: the means are not equal.
    
fprintf('b)\n');
fprintf('SIGNIFICANCE LEVEL %f:\n', alpha)
fprintf('We are doing a right-tailed test for the difference of means.\n');
typeb = 1;                  % right-tailed test 

if ha == 0 
   vartype = 'equal';
   n = n1 + n2 - 2;
   t = (mx - my) / sqrt((n1 - 1) * sx + (n2 - 1) * sy) * sqrt((n1 + n2 - 2) / (1 / n1 + 1 / n2));
else
   vartype = 'unequal';
   c = (sx / n1) / (sx / n1 + sy / n2);
   n = ceil(1 / (c^2 / (n1 - 1) + (1 - c)^2 / (n2 - 1)));
   t = (mx - my) / sqrt(sx / n1 + sy / n2);
end

RR_Ttest(alpha,n,typeb);                                 % rejection region 
[hb, pb, cib, valstatb] = ttest2(x, y, alpha, typeb, vartype);
fprintf('The value of the test statistc t is %f (given by ttest2 %f).\n', t, valstatb.tstat)
fprintf('The P-value of the test is %.10f.\n', pb) 
    
if hb == 1
    fprintf('The null hypothesis is rejected (t in RR), i.e. steel pipes seem to lose more heat.\n')
else
    fprintf('The null hypothesis is NOT rejected (t not in RR), i.e. steel pipes seem to not lose more heat than glass pipes.\n')
end  


% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



% 5.
% To reach the maximum efficiency in performing an assembling operation in a
% manufacturing plant, new employees are required to take a 1-month training
% course. A new method was suggested, and the manager wants to compare the
% new method with the standard one, by looking at the lengths of time
% required for employees to assemble a certain device. They are given below
% (and assumed approximately normally distributed):

x = [46, 37, 39, 48, 47, 44, 35, 31, 44, 37];
y = [35, 33, 31, 35, 34, 30, 27, 32, 31, 31];
n1 = length(x);
n2 = length(y);
mx = mean(x);
my = mean(y);
sx = var(x);
sy = var(y);

% a) At the 5% significance level, do the population variances seem to differ?
% Null hypothesis: the variances are equal.
% Alternative hypothesis: the variances are different.
    
fprintf('a)\n');
fprintf('We are doing a two-test for the variances.\n');
typea = 0;
alpha = 0.05;
RR_Ftest(alpha, n1-1, n2-1, typea);                     % find the rejection region
[ha, pa, cia, valstata] = vartest2(x, y, alpha, typea); 
f = sx / sy;
fprintf('The value of the test statistic f is %f (given by vartest2 %f).\n', f, valstata.fstat)
fprintf('The P-value of the test is %f.\n', pa)
    
if ha == 1
    fprintf('The null hypothesis is rejected (f in RR), i.e. the variances seem to be different.\n')
else
    fprintf('The null hypothesis is NOT rejected (f not in RR), i.e. the variances seem to be equal.\n')
end    


% b) Find a 95% confidence interval for the difference of the average assembling times.
    
fprintf('b)\n');
if ha == 1
    [li, ri] = ConfIntDifMeanNotVarDif(x, y, alpha);
else
    [li, ri] = ConfIntDifMeanNotVarEq(x, y, alpha);
end
fprintf('Confidence interval for the difference of the means(%.4f,%.4f)\n', li, ri)
    
    
    
