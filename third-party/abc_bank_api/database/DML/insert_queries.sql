-- example queries for sd-mint app

-- passwords are same as account_description
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (1, '123456781234', 'pbkdf2:sha256:150000$lEFOkCJM$6a8c24faf7db28b9f507fb6d0f8d202c1c0132d5c29748daea1baebab8fa8dea', 1012.57, 'abc_savings_nathan');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (2, '278103213232', 'pbkdf2:sha256:150000$Dq3lNO7M$14cf6945160aba71ea791925ba23d0fb01a379ba7f2f06a3e4ef7ff95099403b', 2143.31, 'abc_chequing_nathan');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (3, '163423343464', 'pbkdf2:sha256:150000$pViNMr3b$2efd86f5bf6e7305e444ce96083b019284653c7dff6a285d9aa5b6067810f91d', 20251.10, 'abc_savings_jenny');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (4, '243656435347', 'pbkdf2:sha256:150000$9x2P8MBc$5b82aabe40a3ebb6feef87b08c8c3495d39a92bd47787021decbf12e6974548a', 13752.98, 'abc_chequing_jenny');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (5, '165634317799', 'pbkdf2:sha256:150000$c9FNfVnk$85aec8b7c5cc87c0d5eae8d966b810244b1b9af8ba4cd83e07b8bf9835946922', 17564.99, 'abc_savings_bob');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (6, '237545877787', 'pbkdf2:sha256:150000$njHUbglC$2f16d3c30ea8d1006338c0d28045c7c6a35d286de1dde1175aa1115ee0975faf', 5814.13, 'abc_chequing_bob');

-- nathan's transactions
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (1, '2020-07-03', 'panago', 15.14, 2);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (2, '2020-07-03', 'mcdonalds', 9.13, 2);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (3, '2020-07-14', 'ikea', 200.16, 2);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (4, '2020-07-15', 'ikea', 13.13, 2);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (5, '2020-08-03', 'walmart', 104.32, 2);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (6, '2020-08-03', 'costco', 288.21, 2);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (7, '2020-08-09', 'esso', 40.12, 2);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (8, '2020-08-15', 'esso', 13.15, 2);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (9, '2020-08-17', 'amazon', 102.13, 1);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (10, '2020-08-19', 'amazon', 100.15, 2);

-- jenny's transactions
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (11, '2020-07-03', 'panago', 18.27, 3);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (12, '2020-07-03', 'arbys', 19.18, 3);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (13, '2020-07-14', 'ikea', 300.18, 3);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (14, '2020-07-15', 'ikea', 17.13, 3);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (15, '2020-08-03', 'walmart', 231.21, 3);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (16, '2020-08-03', 'costco', 55.52, 4);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (17, '2020-08-09', 'esso', 70.13, 3);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (18, '2020-08-15', 'esso', 27.18, 4);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (19, '2020-08-17', 'alibaba', 42.99, 3);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (20, '2020-08-19', 'amazon', 200.15, 3);

-- bob's transactions
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (21, '2020-07-03', 'chatime', 8.28, 5);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (22, '2020-07-03', 'chipotle', 9.26, 6);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (23, '2020-07-14', 'ikea', 500.18, 5);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (24, '2020-07-15', 'ikea', 27.13, 5);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (25, '2020-08-03', 'walmart', 1231.21, 6);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (26, '2020-08-03', 'costco', 75.52, 6);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (27, '2020-08-09', 'esso', 79.18, 5);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (28, '2020-08-15', 'esso', 38.18, 5);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (29, '2020-08-17', 'walmart', 52.99, 5);
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (30, '2020-08-19', 'amazon', 300.15, 6);