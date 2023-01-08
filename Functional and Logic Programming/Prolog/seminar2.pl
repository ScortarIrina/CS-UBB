suma([], 0).
suma([H|T], S) :-
    suma(T, TS),
    S is H + TS.


% sumaC(L-list, C-col number, R-number)
% (i, i, o)
sumaC([], C, C).
sumaC([H|T], C, R) :-
    CNew is C + H,
    sumaC(T, CNew, R).

mainSC(L, R) :-
    sumaC(L, 0, R).
