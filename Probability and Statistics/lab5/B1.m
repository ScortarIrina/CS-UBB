% In a study of the size of various computer systems, the random variable X, the number of files % stored (in hundreds of thousands), is considered. This data is obtained:

%	 7     7    4    5    9    9
%	 4    12    8    1    8    7
%	 3    13    2    1   17    7
%	12     5    6    2    1   13
%	14    10    2    4    9   11 
%	 3     5   12    6   10    7

% a) Assuming that past experience indicates that σ = 5, find a 100(1−α)% confidence interval for % the average number of files stored.

x = [7 7 4 5 9 9 4 12 8 1 8 7 3 13 2 1 17 7 12 5 6 2 1 13 14 10 2 4 9 11 3 5 12 6 10 7];
n = length(x);      % the length of X
x_bar = mean(x);    % the mean of X
sigma = 5;
confidence_level = input(“Enter value of 1-alpha: “);     % we ask the user for the confidence level
alpha = 1 - confidence_level;                             % compute alpha based on the input
z = norminv(1 - alpha / 2);                               % inverse of the CDF of the normal distribution
Z = norminv(alpha / 2);
m1 = x_bar - sigma / sqrt(n) * z;                         % the margins of the confidence interval
m2 = x_bar - sigma / sqrt(n) * Z;

printf(“Confidence interval with known sigma is %d %d \n”, m1, m2);



% b) Assuming nothing is known about σ, find a 100(1 − α)% confidence interval for the average % number of files stored.

s = std(x);                             % stndard deviation of x
t = tinv(1 - alpha / 2, n-1);           % inverse of the CDF of the student distribution
T = tinv(alpha / 2, n-1);
m3 = x_bar - s / sqrt(n) * t;           % the margins of the confidence interval
m4 = x_bar - s / sqrt(n) * T;

printf(“Confidence interval with unknown sigma is %d %d\n”, m3, m4);

 
% c) Assuming the number of fies stored are approximately normally distributed, find 100(1 − α)% 
% confidence intervals for the variance and for the standard deviation.

s2 = var(x);                              % compute the variance of x
_chai1 = chi2inv(1- alpha / 2, n - 1);    % the inverse of the CDF at X of the chi2 distribution with N degrees of freedom
_chai2 = chi2inv(alpha / 2, n - 1);
m5 = (n - 1) * s2 / _chai1;               % the margins of the confidence interval
m6 = (n - 1) * s2 / _chai2;

printf(“Confidence interval for variance is %d %d\n”, m5, m6);
printf(“Confidence interval for the theoretical standard deviation is %d %d\n”, sqrt(m5), sqrt(m6));
