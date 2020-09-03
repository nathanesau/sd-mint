-- example queries fro sd-mint app

-- passwords are same as account_description
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (1, '123456781234', 'pbkdf2:sha256:150000$n2AuFT22$4a01dd1f4fd8231b8c4ee41500c1fc6d64adf994faf020e471c5029b1083080d', 3012.59, 'xyz_margin_nathan');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (2, '278103213232', 'pbkdf2:sha256:150000$BBgqmwWb$e891a382c56b42b03c7e038762716bd2bd530373a4af5ec56e07c85847157e1f', 6143.41, 'xyz_tfsa_nathan');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (3, '163423343464', 'pbkdf2:sha256:150000$0Ayhmrdz$84c16ad234a5b9b9f8a72f393634096dce688441cf49d6fad744178cb7979afc', 30251.60, 'xyz_margin_jenny');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (4, '243656435347', 'pbkdf2:sha256:150000$1jPziNGI$72e7a5ab09dde3700a2626812b1ec66b6ac3d76419466e60d9e63510152e1fa3', 3752.92, 'xyz_tfsa_jenny');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (5, '165634317799', 'pbkdf2:sha256:150000$XD3Zzp2J$f4bdeb4da631321c20d76c3a2faf244b7c851cee575108ba606e042aafc0d4f0', 27564.89, 'xyz_margin_bob');
insert into account(id, account_login, account_password_hash, account_balance, account_description) values (6, '237545877787', 'pbkdf2:sha256:150000$bdME4R1D$4888f8b1b630791a252669b53d4ab5c8299a36f0f94538f47b70d5b986aab8d1', 4874.13, 'xyz_tfsa_bob');

-- nathan's transactions
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (1, '2020-07-03', 'pizzaville', 18.14, 2);
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
insert into transactions(id, transaction_date, transaction_seller, transaction_amount, account_id) values (11, '2020-07-03', 'pizzaville', 17.39, 3);
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