adjacent(X,Y) :- X =:= Y+1 .
adjacent(X,Y) :- X =:= Y-1 .

building([office(_, 5), office(_, 4), office(_, 3),
	       	office(_, 2), office(_, 1)]).

layout(X) :- building(X),
	     member(office(hunter, A), X), A\==5,
	     member(office(laura, B), X), B\==1, B\==5,
	     member(office(jack, C), X),
	     member(office(jim, D), X), D\==1, D\==5, \+(adjacent(D,B)), 
	     					      \+(adjacent(D,C)),
	     member(office(sally, E), X), E@>B.
