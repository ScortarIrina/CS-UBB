% For the matrices 
%               [1  0 -2] 		        [2  1  1]
%	        A = [2  1  3]		      B = [1  0 -1]
%	            [0  1  0]		          [1  1  0]
% print the matrices C = A−B, D = A·B and E = [eij], where eij =aij ·bij.

A = [1 0 -2; 2 1 3; 0 1 0]
B = [2 1 1; 1 0 -1; 1 1 0]
C = A - B
D = A * B
E = A .* B 
