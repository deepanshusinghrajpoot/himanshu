

'''

What is view
------------

View is a Database Object and view is created over an SQL query.

View does not store any data.
View is like a virtual table.


SELECT * FROM tb_customer_data;

Gpt give a table tb_customer_data have columns cust_id, cust_name, phone, email, address and it has 4 row 


SELECT * from tb_product_info;

Gpt give a table tb_product_info have columns prod_id, prod_name, brand, price and it has 6 row 

SELECT * from tb_order_details;

Gpt give a table tb_order_details have columns ord_id, prod_id, quantity, cust_id, disc_percent, date and it has 6 row 




SELECT o.ord_id, o.date, p.prod_name, c.cust_name,
       (p.price * o.quantity) - ((p.price * o.quantity) * disc_percent::float/100) as cost
FROM tb_customer_data c
JOIN tb_order_details o ON o.cust_id = c.cust_id
JOIN tb_product_info p ON p.prod_id = o.prod_id;


gpt show result



If client/vender required fetch the order summary in a given day

First Option
------------

we are share sql query to client/vender he is execute and see resut which is required
but this is not good way because here we are share some information about data set



Second Option
-------------

Second option is just we are create a view



CREATE VIEW order_summary
AS
SELECT o.ord_id, o.date, p.prod_name, c.cust_name,
       (p.price * o.quantity) - ((p.price * o.quantity) * disc_percent::float/100) as cost
FROM tb_customer_data c
JOIN tb_order_details o ON o.cust_id = c.cust_id
JOIN tb_product_info p ON p.prod_id = o.prod_id;



SELECT * FROM order_summary;

Every time when we are call the created view sql internaly execute that query


So, View does not improve any performance because it exactly exectute same query
If we call 100 time view then query execute 100 times


but there is one type of view that is call Materialized view which can improve performance





Why use VIEW?
What is the purpose of creating a view?
What are its advantages?


What is the main purpose of using a view/advantages of views.
1) Security
2) To simplyfiy complex sql queries.


1) Security
-----------

Here we do not share database credential with any third party
We share database credential only with team member


We create user for client annd then user have only eccess to specific database object which like them to access


CREATE USER james       -- In postregeSQL : CREATE ROLE james
LOGIN
PASSWORD 'james';




'''