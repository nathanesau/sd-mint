-- transaction is a reserved word
create table transactions
(
    id integer primary key not null,
    transaction_date date not null,
    transaction_seller varchar(32) not null,
    transaction_amount float not null,
    account_id integer not null,
    foreign key (account_id) references account(id)
);