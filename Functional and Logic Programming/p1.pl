% 11. a) Write a predicate to substitute an element from a list
%        with another element in the list.


contains([X|_], X).         % true, the element we want to check is the head of the list
contains([_|T], X) :-
    contains(T, X).         % recursive call to the tail of the list
                            % % false otherwise

% call the auxiliary function
substitute(L1, O, N, L2):-
    substitute1(L1, O, N, L2, L1).

% if the list is empty, then the resulted list is also empty
substitute1([], _, _, [], _).

substitute1(L, OLD, _, L, _):-  % result is initial list if
    \+ contains(L, OLD).        % the element we want to change is not in the list

% the case where the OLD element is the head of the list
substitute1([OLD|T], OLD, NEW, [NEW|R], L1):-   % we substitute the old elem with new if
    contains(L1, NEW),                          % the list contains the new one
    substitute1(T, OLD, NEW, R, L1).            % recursive call on the tail of the list

% the case where the OLD element is NOT the head of the list
substitute1([H|T], OLD, NEW, [H|R], L1):-
    contains(L1, NEW),                      % if the list original list contains NEW
    substitute1(T, OLD, NEW, R, L1).        % recursive call

test_substitute:-
    substitute([], 1, 2, []),
    substitute([1, 2, 2], 1, 2, [2, 2, 2]),
    \+substitute([1, 2, 5, 7, 9], 2, 3, [1, 3, 5, 7, 9]),
    substitute([2, 2, 1], 2, 1, [1, 1, 1]),
    \+substitute([1, 1, 1], 1, 2, [2, 2, 2]).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%     b) Write a predicate to create the sublist (lm, ..., ln)
%        from the list (l1, ..., lk).

% base case: the list is empty => the result is also the empty list
sublist([], _, _, _, []).

% the case when the current position in the list is
% between the bounds of the resulted list
sublist([H|T], Pos, M, N, [H|R]):-
    Pos > M-1,
    Pos < N+1,
    Pos1 is Pos+1,    % increment the position
    sublist(T, Pos1, M, N, R).

% case when the current position is not bewteen the bounds
sublist([_|_], Pos, M, N, R):-
    Pos1 is Pos+1,
    sublist(_, Pos1, M, N, R).

test_sublist:-
    sublist([1, 2, 3, 4, 5], 1, 2, 4, [2, 3, 4]),
    sublist([1, 2, 3, 4, 5], 1, 1, 4, [1, 2, 3, 4]),
    sublist([1, 2, 3, 4, 5], 1, 2, 5, [2, 3, 4, 5]),
    sublist([1, 2, 3], 1, 2, 5, []),
    sublist([1, 2, 3, 4, 5], 1, 7, 8, []).
