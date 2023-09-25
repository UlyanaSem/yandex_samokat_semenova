Нужно было проверить, отображается ли созданный заказ в базе данных
Для этого был выведен список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 
Действия выполнялись в следующем порядке:
Подключение к серверу через ssh, а далее решение задачи: 

morty=# \c scooter_rent
You are now connected to database "scooter_rent" as user "morty".
$ ssh fe7ee63b-381e-4400-8df2-c02304918d25@serverhub.praktikum-services.ru -p 4554
morty@1f953c066b8e:~$ psql -U morty
Password for user morty:
psql (11.18 (Debian 11.18-0+deb10u1))
Type "help" for help.

morty=# \l
                               List of databases
     Name     |  Owner   | Encoding | Collate |  Ctype  |   Access privileges
--------------+----------+----------+---------+---------+-----------------------
scooter_rent=#  postgres | UTF8     | C.UTF-8 | C.UTF-8 |
 postgres     | postgres | UTF8     | C.UTF-8 | C.UTF-8 |
 scooter_rent | postgres | UTF8     | C.UTF-8 | C.UTF-8 |
 template0    | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
              |          |          |         |         | postgres=CTc/postgres
 template1    | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
              |          |          |         |         | postgres=CTc/postgres
(5 rows)


scooter_rent=# \dt
           List of relations
 Schema |     Name      | Type  | Owner
--------+---------------+-------+-------
 public | Couriers      | table | root
 public | Orders        | table | root
 public | SequelizeMeta | table | root
(3 rows)

scooter_rent=# SELECT * FROM "Couriers";


id |   login    |           passwordHash           | firstName |         createdAt          |         updatedAt
----+------------+----------------------------------+-----------+----------------------------+----------------------------
  1 | Ulyana1002 | 81dc9bdb52d04dc20036dbd8313ed055 | Ulyana    | 2023-09-20 20:09:27.117+00 | 2023-09-20 20:09:27.117+00
  2 | Denis2013  | 81dc9bdb52d04dc20036dbd8313ed055 | Denis     | 2023-09-20 20:09:35.901+00 | 2023-09-20 20:09:35.901+00
  3 | Anna1970   | 81dc9bdb52d04dc20036dbd8313ed055 | Anna      | 2023-09-20 20:09:44.543+00 | 2023-09-20 20:09:44.543+00
  4 | Anatoliy70 | 81dc9bdb52d04dc20036dbd8313ed055 | Anatoliy  | 2023-09-20 20:09:53.292+00 | 2023-09-20 20:09:53.292+00
(4 rows)




SELECT c.login, COUNT(*)
FROM "Couriers" c
INNER JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;

СРАБОТАЛ ЭТОТ
scooter_rent=# SELECT c.login, COUNT(*)
scooter_rent-#   FROM "Couriers" AS c
scooter_rent-#   INNER JOIN "Orders" AS o ON c.id = o."courierId"
scooter_rent-#   WHERE o."inDelivery" = true
scooter_rent-#   GROUP BY c.login;
   login    | count
------------+-------
 Anatoliy70 |     2
(1 row)






SELECT track,
  CASE 
    WHEN finished = true THEN 2
    WHEN cancelled = true THEN -1
    WHEN "inDelivery" = true THEN 1
    ELSE 0
  END AS status
FROM "Orders";



scooter_rent=# SELECT track,
scooter_rent-#   CASE
scooter_rent-#     WHEN finished = true THEN 2
scooter_rent-#     WHEN cancelled = true THEN -1
scooter_rent-#     WHEN "inDelivery" = true THEN 1
scooter_rent-#     ELSE 0
scooter_rent-#   END AS status
scooter_rent-# FROM "Orders";
 track  | status 
 
--------+--------
 713473 |      0
 911199 |      0
 678434 |      0
 189015 |      1
 189015 |      2
 199858 |     -1
(6 rows)


 Знакомство с API Яндекс Самоката для курьеров: 
Документация API расположена по пути <url запущенного сервера>/docs/>
Изучение документации разделов
Определение путей к созданию заказа и к взаимодейтсвию с ними, их оформление в Python File- config.py
Занесение обязательных данных разделов в Python File - data_orders.py

 Задача тестирования: 
Проверить, что по треку заказа можно получить данные о заказе.
Выполнить запрос на создание заказа.
Сохранить номер трека заказа.
Выполнить запрос на получения заказа по треку заказа.
Проверить, что код ответа равен 200.

 Тестирование чек-листа в файле request_receive_order_data.py
Тестирование на создание заказа и получения номер трека
Получение информации о заказе с использованием номера трека
Вызываем функцию test_create_orders() для выполнения теста
Проверка, что код ответа равен 200 
<img width="960" alt="pycharm64_2S9OeiyqrN" src="https://github.com/UlyanaSem/yandex_samokat_semenova/assets/143070602/9d661a21-de50-42d2-963f-626dc016c027">


https://github.com/UlyanaSem/yandex_samokat_semenova/assets/143070602/6971fee0-82ae-44e5-bf1c-8a1a463035f2


