% Generate all sub-strings of a length 2*n+1, formed from values of 0, 1 or -1, so a1 = ..., a2n+1 = 0
% and |a(i+1) - ai| = 1 or 2, for every 1 <= i <= 2n.


% contains(E: int, L: list)
% flow model: (i, i), (o, i)
% E - the element to be checked if it is in the list
% L - the list
% check if an elements appears in a list

contains(E, [E|_]).
contains(E, [_|T]) :-
    contains(E, T).


% candidate(E1: int, E: int)
% flow model: (o, i), (i, i), (i, o)
% E1 - possible candidate value
% E - value from the next position
% check if the pair (E1, E) is a candidate partial solution, where (E1 != E)

candidate(E1, E) :-
    contains(E, [-1, 0, 1]),
    contains(E1, [-1, 0, 1]),
    E =\= E1.


% generate(N: int, Pos: int, L: list)
% flow model: (i, i, o), (i, i, i)
% N - given number
% Pos - current position in the list
% L - resulted list
% generate the solution

generate(N, Pos, [0]) :-
    Finish is 2 * N + 1,
    Pos =:= Finish,
    !.
generate(N, Pos, [E|T]) :-
    NewPos is Pos + 1,
    generate(N, NewPos, T),
    T = [E1|_],
    candidate(E1, E).

main(N, R) :-
    generate(N, 1, R).


test_function :-
    findall(S, main(1, S), [[0, -1, 0], [1, -1, 0], [-1, 1, 0], [0, 1, 0]]),
    findall(S, main(2, S), [[0, -1, 0, -1, 0],
                                   [1, -1, 0, -1, 0],
                                   [-1, 1, 0, -1, 0],
                                   [0, 1, 0, -1, 0],
                                   [0, -1, 1, -1, 0],
                                   [1, -1, 1, -1, 0],
                                   [-1, 0, 1, -1, 0],
                                   [1, 0, 1, -1, 0],
                                   [-1, 0, -1, 1, 0],
                                   [1, 0, -1, 1, 0],
                                   [-1, 1, -1, 1, 0],
                                   [0, 1, -1, 1, 0],
                                   [0, -1, 0, 1, 0],
                                   [1, -1, 0, 1, 0],
                                   [-1, 1, 0, 1, 0],
                                   [0, 1, 0, 1, 0]]).




% ------------------------ Mathematical model ------------------------

% contains(E, l1...ln) = { false, if list is empty
%                        { true, if E = l1
%                        { contains(E, l2...ln), if list !empty

% candidate(a_nextPosition) = { a_position from [-1, 0, 1], if a_nextPosition is in [-1, 0, 1] and a_position != a_nextPosition

% generate(n, position) = { 0, if position = 2n + 1
%                         { candidate(a_nextPosition) ∪ generate(n, position + 1) , otherwise
