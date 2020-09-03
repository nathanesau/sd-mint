-- example queries fro sd-mint app

-- passwords are same as account_description
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (1, '123456781234', 'pbkdf2:sha256:150000$FRb1SnZg$6174439c41665d33166cae4ce22a5c080dbcdd73813712f1123180be08271188', 3012.59, 'xyz_savings_nathan');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (2, '278103213232', 'pbkdf2:sha256:150000$4mKnoNVo$8d774407e838ee8c2698a4cc525d9e6baa93aa2340857a6cd400ef34855cce38', 6143.41, 'xyz_chequing_nathan');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (3, '163423343464', 'pbkdf2:sha256:150000$iDNeTWqu$86980e7bc05ae6671407c6a4358e34f85b9324baa05f0e02d710927aa30f90b1', 30251.60, 'xyz_savings_jenny');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (4, '243656435347', 'pbkdf2:sha256:150000$r9onaex6$9fb2aaf0a4efecac050019e4c5ec9868bb7958e69ef19c392428bbf996ddbf03', 3752.92, 'xyz_chequing_jenny');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (5, '165634317799', 'pbkdf2:sha256:150000$cyunwzZq$84b5374e65f0a20a040bb95ad4c27fa5b69d1c1cf5196a48a22c74407b713c34', 27564.89, 'xyz_savings_bob');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (6, '237545877787', 'pbkdf2:sha256:150000$Yd9wRv8S$2b14728fb41fc669d2349824ba684671ee1bfc1210645341c07435f5a8fb120f', 4874.13, 'xyz_chequing_bob');

-- nathan's transactions
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (1, '2020-07-03', 'dominos', 15.14, 2);
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
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (11, '2020-07-03', 'dominos', 18.27, 3);
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