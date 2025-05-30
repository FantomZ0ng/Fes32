:- use_module(library(csv)).

suspicious_account(john).
suspicious_account(paul).

suspicious_country('Iran').
suspicious_country('Iraq').
suspicious_country('Russian').
suspicious_country('Syria').


suspicious_type(gambling).




suspicious_transaction(T) :- transaction(T, Account, Amount, Time, Country, Type),(
suspicious_account(Account);
Amount > 20000, Time = night;
suspicious_country(Country);
suspicious_type(Type)).



read_transactions(File) :-
    csv_read_file(File, Rows),

    maplist(convert_to_transaction, Rows).

convert_to_transaction(row(T, Account, Amount, Time, Country, Type)) :-
    assertz(transaction(T, Account, Amount, Time, Country, Type)).
