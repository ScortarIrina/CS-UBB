% Given a numerical linear list consisting of integers, substitute all the occurrences of the maximum element
% of the list with another list.

% [1 -2 1 -3 1 -4] [10 11] -> [10 11 -2 10 11 -3 10 11 4]
% [6 3 8 1] [10 11] -> [6 3 10 11 1]
% [4 4 4 4] [10 11] -> [10 11 10 11 10 11 10 11]
% [7 3 4 2 7] [10 11] -> [10 11 3 4 2 10 11]


% my_insert(L: list, List: list, R: list)

my_insert([], L, L).
my_insert([H|T], L, [H|R]) :-
    my_insert(T, L, R).


% maxOfTwo(X: int, Y: int, Z: result)

maxOfTwo(X, Y, X) :-
    X >= Y.
maxOfTwo(X, Y, Y) :-
    X < Y.

% maxL(L: list, X: int)

maxL([X], X).
maxL([H | T], X) :-
    maxL(T, I),
    maxOfTwo(H, I, X).


% substituteElem(L: list, E: int, List: list, R: list)
% substituteElem(i, i, i, o), (i, i, i, i)

substituteElem([], _, _, []).
substituteElem([H|T], E, List, R) :-
    H =:= E,
    my_insert(List, T, RI),
    substituteElem(RI, E, List, R).
substituteElem([H|T], E, List, [H|R]) :-
    H =\= E,
    substituteElem(T, E, List, R).


main(L1, L2, R) :-
    maxL(L1, MAX),
    substituteElem(L1, MAX, L2, R).


test_fct :-
    main([1, -2, 1, -3, 1, -4], [10, 11], [10, 11, -2, 10, 11, -3, 10, 11, -4]),
    main([6, 3, 8, 1], [10, 11],[6, 3, 10, 11, 1]),
    main([4, 4, 4, 4], [10, 11], [10, 11, 10, 11, 10, 11, 10, 11]),
    main([7, 3, 4, 2, 7], [10, 11], [10, 11, 3, 4, 2, 10, 11]).
