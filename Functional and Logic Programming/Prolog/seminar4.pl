% ----------------------------------------------------------------------------------------------------------------

% Given a list L, generate the list of all arrangements of K elements from the list that have product P and sum S.
% Ex:       L=[1,2,3,10], K=2, P=30, S=13  =>  R = [[3, 10], [10, 3]].



% product of the elements of a list using the collector variable
% prod(L-list, C-collector variable, P-resulted product)
% prod(i,i,o)

prod([], C, C).
prod([H|T], C, P) :-
    P1 is C * H,
    prod(T, P1, P).


% sum of the elements of a list using the collector variable
% sum(L-list, SC-collector variable, S-resulted sum)
% sum(i,i,o)

sum([], SC, SC).
sum([H|T], SC, S) :-
    SC1 is SC + H,
    sum(T, SC1, S).


% insert an element in a list
% insert(E-element, L-list, R-resulted list)
% insert(i,i,o)

insert(E, L, [E|L]).
insert(E, [H|T], [H|R]) :-
    insert(E, T, R).


% permutations of a linear list (uses insert)
% perm(L-list, R-resulted list)
% perm(i,o)

perm([], []).
perm([H|T], P) :-
    perm(T, R),
    insert(H, R, P).


% arrangements ok K elements from a list L (uses insert)
% arr(L-list, K-number of elements, R-resulted list)
% arr(i, i, o)

arr([E|_], 1, [E]).
arr([_|T], K, R) :-
    arr(T, K, R).
arr([H|T], K, R1) :-
    K > 1,
    K1 is K-1,
    arr(T, K1, R),
    insert(H, R, R1).


% combinations of K elements from the list L
% comb(L-list, K-number of elements, R-resulted list)
% comb(i,i,o)

comb([E|_], 1, [E]).
comb([_|T], K, R) :-
    comb(T, K, R).
comb([H|T], K, [H|R]) :-
    K > 1,
    K1 is K-1,
    comb(T, K1, R).


% arrangements by creating permutations of combinations

lazyArrangements(L, K, R) :-
    comb(L, K, A),
    perm(A, R).


% determine a solution for our problem
% oneSol(L-list, K-number elements, P-product, S-sum, R-resulted list)
% oneSol(i,i,i,i,o)

oneSol1(L, K, P, S, RL) :-
    arr(L, K, RL),
    prod(RL, 1, P),
    sum(RL, 0, S).


% determine all solutions in a resulted list by using the predicate FINDALL
% allSols(L-list, K-number of elements, P-product, S-sum, R-resulted list)
% allSols(i,i,i,i,o)

allSols1(L, K, P, S, R) :-
    findall(RL, oneSol(L, K, P, S, RL), R).





% ----------------------------------------------------------------------------------------------------------------

% We are given a sequence a1 ... an composed of distinct integer numbers. Display all subsequences which have a
% valley aspect.
% Ex:   [5, 3, 4, 2, 7, 11, 1, 8, 6]    =>   [5, 4, 3, 11], [3, 2, 1, 4, 5, 7, 8], [11, 6, 1, 3, 4, 5], ...



% element2(l1 l2 ... ln) = { (l1, l2 ... ln)
%                        = {(e, l1 U Rest),   if element2(l2 ... ln) = (e, Rest)
% element2(i, i, o)

element2([H|T], H, T).
element2([H|T], E, [H|Rest]) :-
    element2(T, E, Rest).


% 1 for decreasing, 0 for increasing
% generate(l1 l2 ... ln, c1 c2 ... cm, Flag) = { c1 c2 ... cm,  if Flag = 1
%                                            = { generate(Rest, e U c1 c2 ... cm, 0),  if Flag = 0, e < c1, element2(L) = (e, Rest)
%                                            = { generate(Rest, e U c1 c2 ... cm, 1),  if (Flag = 0 OR 1), e > c1, element2(L) = (e, Rest)
        
% start(l1 l2 ... ln) = generate(Rest2, [e1, e2], 0),  if element2(L) = (e1, Rest)
%                                                         element2(Rest) = (e2, Rest2), e1 < e2
            
            
% generate(L-list, Cand-list, Flag-number, R-list)
    
generate(_, Cand, 1, Cand).
generate(L, [C1|Cand], 0, R) :-
    element2(L, E, Rest),
    E < C1,
    generate(Rest, [E,C1|Cand], 0, R).
generate(L, [C1|Cand], _, R) :-
    element2(L, E, Rest),
    E > C1,
    generate(Rest, [E,C1|Cand], 1, R).

start(L, R) :-
    element2(L, E1, Rest),
    element2(Rest, E2, Rest2),
    E1 < E2,
    generate(Rest2, [E1, E2], 0, R).
    
allSols2(L, R) :-
    findall(X, start(L, X), R).


