% Remove sublist from heterogeneous list

% process1(L - list, R - list)

process1([],[]).
process1([H|T], R) :-
    is_list(H),
    process1(T, R).
process1([H|T], [H|R]) :-
    atomic(H),    % OR \+ is_list(H)  OR  not(is_list(H))
    process1(T, R).



% --------------------------------------------------------


% Given a list of numbers and sublists of numbers, substitute each sublist in which the sum of the elements is odd
% with the first element of that sublist.

%    [1, 2, [2, 4], 7, 3, [4, 6, 7], [1], 8, 10, [3, 2]]   =>
%        [1, 2, [2, 4], 7, 3, 4, 1, 8, 10, 3]

%process(l1 l2 É ln)    = [ ], if n = 0
%            = l1 U process(l2 .. ln), if number(l1)
%            = l11 U process(l2 É ln), if is_list(l1) and sum(l1) odd
%            = l1 U process(l2 É ln), if is_list(l1) and sum(l1) even

% process(L - list, R - list)
% flow model: (i, i), (i, o)

process2([], []).
process2([H|T], [HH|R]) :-
    is_list(H),
    sum(H, S),
    S mod 2 =\= 0,
    !,
    H1 = [HH|_],
    process2(T, R).
process1([H|T], [H|R]) :-
    process2(T, R).


% -------------------------------------------------------------------

% Given a heterogeneous list composed of numbers and lists of numbers,
% remove the odd numbers from the sublists that have a mountain aspect.

% mountain(L - list, F - flag)
% flow model: (i, i), (i, o)


mountain([_], 1).
mountain([H1, H2| T], 0) :-
    H1 < H2,
    mountain([H2|T], _).
mountain([H1, H2|T], _) :-
    H1 > H2,
    mountain([H2|T], 1).
main([H1, H2|T]) :-
    H1 < H2,
    mountain([H1, H2|T], 0).

removeOdd([], []).
% the head is an even number, so we keep it
removeOdd([H|T], [H|R]) :-
    H mod 2 =:= 0,
    !,
    removeOdd(T, R).
removeOdd([_|T], R) :-
    removeOdd(T, R).

process3([], []).
process3([H|T], [H|R]) :-
    is_list(H),
    main(H),
    !,
    removeOdd(H, H1),
    process3(T, R).
process3([H|T], [H|R]) :-
    process3(T, R).
