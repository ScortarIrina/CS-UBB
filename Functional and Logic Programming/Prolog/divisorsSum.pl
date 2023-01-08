divisorsSum(N, CurrDiv, 0):-
    N2 is N div 2,
    CurrDiv > N2.

divisorsSum(N, CurrDiv, S):-
    N mod CurrDiv =:= 0,
    NextDiv is CurrDiv + 1,
    divisorsSum(N, NextDiv, SP),
    S is CurrDiv + SP.

divisorsSum(N, CurrDiv, S):-
    N mod CurrDiv =\= 0,
    NextDiv is CurrDiv + 1,
    divisorsSum(N, NextDiv, S).

divisorSumMain(N, S):-
    divisorsSum(N, 2, S).
