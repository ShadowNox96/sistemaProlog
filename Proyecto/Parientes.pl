progenitor(pedro,teresa).
progenitor(maria,teresa).
progenitor(maria,elena).
progenitor(teresa,jorge).
progenitor(teresa,raquel).
progenitor(raquel,miguel).
descendiente(X,Y) :- progenitor(Y,X).
hombre(pedro).
hombre(jorge).
hombre(miguel).
mujer(raquel).
mujer(maria).
mujer(elena).
mujer(terea).
hermana(X,Y) :- progenitor(Z,X) , progenitor(Z,Y), mujer(X).
nieto(X,Y) :- progenitor(Y,W),progenitor(W,X).
tio(X,Y) :- progenitor(W,X), nieto(Y,W).
hijo(X,M) :- progenitor(M,X).
mama(M,X) :- progenitor(M,X), mujer(M).
esposo(X,Y) :- progenitor(X,M), progenitor(Y,M), hombre(X).
papa(X,Y) :- progenitor(X,Y) , hombre(X).


