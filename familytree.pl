% =========================================
% FAMILY TREE ASSIGNMENT (PROLOG)
% =========================================

% -------- FACTS --------

% Gender
male(john).
male(peter).
male(mike).
male(david).
male(mark).

female(mary).
female(linda).
female(susan).
female(anna).
female(jane).

% Parents (Grandparents → Parents → Children)

parent(john, peter).
parent(mary, peter).

parent(john, susan).
parent(mary, susan).

parent(peter, mike).
parent(linda, mike).

parent(peter, david).
parent(linda, david).

parent(susan, mark).
parent(jane, mark).

parent(susan, anna).
parent(jane, anna).

% -------- RULES --------

% Father
father(X, Y) :-
    male(X),
    parent(X, Y).

% Mother
mother(X, Y) :-
    female(X),
    parent(X, Y).

% Grandparent
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Grandchild
grandchild(X, Y) :-
    grandparent(Y, X).

% Siblings
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Uncle
uncle(X, Y) :-
    male(X),
    sibling(X, Z),
    parent(Z, Y).

% Aunt
aunt(X, Y) :-
    female(X),
    sibling(X, Z),
    parent(Z, Y).

% Cousin
cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).