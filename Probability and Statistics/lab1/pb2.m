% For x ∈ [0, 3], graph on the same set of axes the functions x5/10, x*sin x and cos x,
% in different colours and line-styles. Display a title and a legend on your graph. Then plot them % on different pictures.

x=-1:0.1:1
plot(x, x.^5/10, x, x.*sin(x), x, cos(x))
title("Multiple plots")
legend("x^5/10", "xsinx", "cosx")
