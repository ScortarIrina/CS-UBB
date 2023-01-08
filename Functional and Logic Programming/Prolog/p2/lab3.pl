% a. Sort a list with removing the double values.
%            [4 2 6 2 3 4] --> [2 3 4 6]


% the head is the element we are searching for
search([H|_], X) :-
    H =:= X.

% the head is not the element we are searching for
search([H|T], X) :-
    H =\= X,
    search(T, X).

% nothing to remove is the list is empty
remove_duplicates([], []).

% element is not repeated in the list, so we put it in the result
remove_duplicates([H|T], [H|R]) :-
    \+search(T, H),
    remove_duplicates(T, R).

% element is repeated in the list, so we do not put it in the result
remove_duplicates([H|T], R) :-
    search(T, H),
    remove_duplicates(T, R).

% searching for the position to insert the element
insert(X, [Y|T], [Y|NT]) :-
    X > Y,
    insert(X, T, NT).

% position to insert is found
insert(X, [Y|T], [X,Y|T]) :-
    X =< Y.

% insert in an empty list
insert(X, [], [X]).

i_sort([], Acc, Acc).
i_sort([H|T], Acc, Sorted) :-
    insert(H, Acc, NAcc),
    i_sort(T, NAcc, Sorted).

% wrapper function
sort_and_remove(L, S) :-
    remove_duplicates(L, R),
    i_sort(R, [], S).

test_sort_and_remove :-
    sort_and_remove([4, 2, 6, 2, 3, 4], [2, 3, 4, 6]),
    sort_and_remove([], []),
    sort_and_remove([3], [3]),
    sort_and_remove([3, 3, 2, 2, 1, 1], [1, 2, 3]),
    sort_and_remove([1, 1, 1], [1]),
    sort_and_remove([1, 2, 3], [1, 2, 3]).




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



% b. For a heterogeneous list, formed from integer numbers and list of numbers,
%    write a predicate to sort every sublist with removing the doubles.
%
%   Eg.: [1, 2, [4, 1, 4], 3, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7]
%            =>   [1, 2, [1, 4], 3, 6, [1, 3, 7, 9, 10], 5, [1], 7].



% predicates for the length of a list
list_length([], 0).
list_length([_|Xs], L):-
    list_length(Xs, N),
    L is N+1.


% --- the case when the list is empty
sort_sublist_remove_duplicates([], []).

% --- the case when the list has only one element
sort_sublist_remove_duplicates([_], [_]).

sort_sublist_remove_duplicates([H|T], [RCPY|[]]) :-     % append to the result the empty list since we are at the end of the big list
    is_list(H),                                         % the head of the big list is also a list
    sort_and_remove(H, RCPY),                           % sort and remove duplicates of the inner list
    list_length(T, 0).                                  % there are no more elements in the big list after the current head

sort_sublist_remove_duplicates([H|T], [RCPY|R]) :-
    is_list(H),                                         % the head of the big list is also a list
    sort_and_remove(H, RCPY),                           % sort and remove duplicates of the inner list
    \+list_length(T, 0),                                % we are not at the end of the big list
    sort_sublist_remove_duplicates(T, R).               % recursive call on the tail of the big list

sort_sublist_remove_duplicates([H|T], [H|R]) :-
    number(H),                                          % the head of the list is an integer number
    sort_sublist_remove_duplicates(T, R).               % recursive call on the tail of the big list


wrapper_function(L, R) :-
    sort_sublist_remove_duplicates(L, R).


test_function :-
    wrapper_function([], []),
    wrapper_function([1], [1]),
    wrapper_function([[1]], [[1]]),
    wrapper_function([1, 2, 3], [1, 2, 3]),
    wrapper_function([3, 3, 2, 1, 3], [3, 3, 2, 1, 3]),
    wrapper_function([1, 2, [4, 1, 4]], [1, 2, [1, 4]]),
    wrapper_function([1, 2, [4, 1, 4], 5, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7], [1, 2, [1, 4], 5, 6, [1, 3, 7, 9, 10], 5, [1], 7]),
    wrapper_function([1, 2, [3, 22, 3, 1, 2], 1, 2, [9, 9, 5, 5, 7, 7]], [1, 2, [1, 2, 3, 22], 1, 2, [5, 7, 9]]),
    wrapper_function([1, 2, [4, 1, 4], 3, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7], [1, 2, [1, 4], 3, 6, [1, 3, 7, 9, 10], 5, [1], 7]).
    
