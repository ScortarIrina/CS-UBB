% isNumber(N) :- number(N).

% isEvenNumber(N):-
%     N mod 2 =:= 0.

%female(alice).
%female(judy).
%female(cara).
%male(bob).
%male(chris).

%stabs(tybalt, mercutio, sword).
%hates(romeo, X) :-
%    stabs(X, mercutio, sword).

%parent(albert, bob).
%parent(albert, betty).
%parent(albert, bill).

%parent(alice, bob).
%parent(alice, betty).
%parent(alice, bill).

%parent(bob, carl).
%parent(bob, charlie).

%related(X, Y) :-
%    parent(X, Y).

%related(X, Y) :-
%    parent(X, Z),
%    related(Z, Y).

% Multiply the elements of a list with a constant value.
% flow model: (i i i) => (i i o)
%mmul(2,[1,2,3],R).

mmul(_, [], []).
mmul(K, [H|T], [HR|TR]) :-
    HR is K*H,
    mmul(K, T, TR).
