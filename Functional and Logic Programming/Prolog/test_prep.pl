% Check if a number is a lucky number. A number is considered lucky if it contains only the digits 4 and 7.

lucky(N) :-
    N =:= 4.

lucky(N) :-
    N =:= 7.

lucky(N) :-
    UC is N mod 10,
    UC =:= 4,
    N1 is N div 10,
    lucky(N1).

lucky(N) :-
    UC is N mod 10,
    UC =:= 7,
    N1 is N div 10,
    lucky(N1).


% ----------------------------------------------------------------------------------------------

% Compute the sum of the proper divisors of a number n.
% Ex:   n = 20      =>      2 + 4 + 5 + 10 = 21.


divisorsSum(N, CurrDiv, 0) :-
    N2 is N div 2,
    CurrDiv > N2.

divisorsSum(N, CurrDiv, S) :-
    N mod CurrDiv =:= 0,
    NextDiv is CurrDiv + 1,
    divisorsSum(N, NextDiv, SP),
    S is CurrDiv + SP.

divisorsSum(N, CurrDiv, S) :-
    N mod CurrDiv =\= 0,
    NextDiv is CurrDiv + 1,
    divisorsSum(N, NextDiv, S).

divisorsSumMain(N, S) :-
    divisorsSum(N, 2, S).


% ----------------------------------------------------------------------------------------------

% Multiply the elements of a list with a constant value.

list_mul(_, [], []).

list_mul(K, [H|T], [HR|TR]) :-
    HR is K * H,
    list_mul(K, T, TR).


% ----------------------------------------------------------------------------------------------

% Add an element at the end of a list.

addEnd([], E, [E]).

addEnd([H|T], E, [H|R]) :-
    addEnd(T, E, R).


% ----------------------------------------------------------------------------------------------

% Compute the sum of elements in a list.

sumList([], 0).

sumList([H|T], S) :-
    sumList(T, ST),
    S is H + ST.


% ----------------------------------------------------------------------------------------------

% Compute the product of the even numbers from a list

prodEven([], 1).

prodEven([H|T], R) :-
    H mod 2 =:= 0,
    prodEven(T, RT),
    R is RT * H.

prodEven([H|T], R) :-
    H mod 2 =\= 0,
    prodEven(T, R).
    

% ----------------------------------------------------------------------------------------------

% Insert a value e on position m (m >=1) in a list (indexing starts from 1).
% Ex:   we insert in list [1, 2, 3, 4, 5, 6], e = 11 on m = 4    =>    [1, 2, 3, 11, 4, 5, 6]

insertOnPos([], _, M, []) :-
    M > 1.

insertOnPos([], E, M, [E]) :-
    M =:= 1.

insertOnPos(L, E, M, R) :-
    M =:= 1,
    R = [E|L].

insertOnPos([H|T], E, M, [H|R]) :-
    M1 is M - 1,
    insertOnPos(T, E, M1, R).


% ----------------------------------------------------------------------------------------------

% Insert a value e in a list from m to m(m >=2).
% Eg:   for the list: [1,2,3,4,5,6,7,8,9,10], e = 11 and m = 4      =>      [1,2,3,11,4,5,6,11,7,8,9,11,10].

insertFromMToM([], _, M, _, []) :-
    M > 1.

insertFromMToM([], E, M, _, [E]) :-
    M =:= 1.

insertFromMToM(L, E, M, CM, [E|R]) :-
    M =:= 1,
    insertFromMToM(L, E, CM, CM, R).

insertFromMToM([H|T], E, M, CM, [H|R]) :-
    M > 1,
    M1 is M - 1,
    insertFromMToM(T, E, M1, CM, R).

insertFromMToMMain(L, E, M, R) :-
    insertFromMToM(L, E, M, M, R).


% ----------------------------------------------------------------------------------------------

% Delete the first occurrence of an element e from a list.

deleteFirst(_, [], []).

deleteFirst(E, [H|T], R) :-
    H =:= E,
    R = T.

deleteFirst(E, [H|T], R) :-
    H =\= E,
    deleteFirst(E, T, RT),
    R = [H|RT].


% ----------------------------------------------------------------------------------------------

% Delete all occurrences of an element e from a list.

deleteAll(_, [], []).

deleteAll(E, [H|T], R) :-
    H =:= E,
    deleteAll(E, T, R).

deleteAll(E, [H|T], R) :-
    H =\= E,
    deleteAll(E, T, RT),
    R = [H|RT].


% ----------------------------------------------------------------------------------------------

% Compute number of occurrences of an element in a list.

noOcc(_, [], 0).

noOcc(E, [H|T], N) :-
    H =:= E,
    noOcc(E, T, N1),
    N is N1 + 1.

noOcc(E, [H|T], N) :-
    H =\= E,
    noOcc(E, T, N).


% ----------------------------------------------------------------------------------------------

% Write a predicate to determine the lowest common multiple of a list formed from integer numbers.

% abs(X: int, Y: int)
% flow model: (i, i), (o, i), (i, o)
% X-number, Y-absolute value of X
abs(X, X) :-
    X >= 0,
    !.
abs(X, Y) :-
    X < 0,
    Y is -X.

% gcd(X: int, Y: int, Z: int)
% flow model: (i, i, o) or (i, i, i).
% X-first number, Y-second number, Z-result
gcd(0, X, X).
gcd(X, 0, X).
gcd(X, X, X).
gcd(X, Y, Z) :-
    Y > X,
    Y1 is Y - X,
    gcd(X, Y1, Z).
gcd(X, Y, Z) :-
    Y < X,
    X1 is X - Y,
    gcd(X1, Y, Z).

% lcm(X: int, Y: int, Z: int)
% flow model: (i, i, o) or (i, i, i).
% X-first number, Y-second number, Z-result
lcm(0, _, 0).
lcm(_, 0, 0).
lcm(X, Y, Z) :-
    abs(X * Y, P),
    gcd(X, Y, D),
    Z is P / D.

% lcm_list(L: list, R: int)
% flow model: (i,o) or (i,i)
% L - the list for which we compute the lowest common multiple
% R - the result
lcm_list([E], E).
lcm_list([H|T], R) :-
    lcm_list(T, R1),
    lcm(H, R1, R).


% ----------------------------------------------------------------------------------------------

% Write a predicate to add a value v after 1-st, 2-nd, 4-th, 8-th, É element in a list.

% pow2(X: int, R: int)
% flow model: (i,o) or (i,i)
% X - the number to be checked, R - result(0 only if X is a power of two)
pow2(X, R) :-
    X > 0,
    R is X /\ (X-1).

% add_after(List: list, Position: int, V: int, Result: list)
% flow model: (i,i,i,o), (i,i,o,i), (i,i,i,i), (o,i,i,i), (o,i,o,i)
% List - initial list, Position - the current position, V - the element to be added, Result - the final list
add_after([], _, _, []).
add_after([H1|T1], Position, V, [H1|[V|T2]]) :-
    pow2(Position, R),
    R =:= 0,
    Position1 is Position + 1,
    add_after(T1, Position1, V, T2).
add_after([H1|T1], Position, V, [H1|T2]) :-
    pow2(Position,R),
    R =\= 0,
    Position1 is Position + 1,
    add_after(T1, Position1, V, T2).
    

add_after(List, V, Result) :- add_after(List, 1, V, Result).
