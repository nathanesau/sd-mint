create table account
(
    id integer primary key not null,
    account_login varchar(32) not null,
    account_password_hash varchar(128) not null,
    account_balance float not null,
    account_description varchar(32) not null
);
