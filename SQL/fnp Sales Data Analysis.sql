-- Creating Dabase Structure --

create database fnp_sales_data;

use fnp_sales_data;

create table customers(
	customer_id varchar(5) primary key,
    customer_name varchar(50) not null,
    city varchar(50) not null,
    contact_number varchar(15) not null,
    email varchar(100) not null,
    gender varchar(10) not null,
    address varchar(200) not null
);

create table products(
	product_id int primary key,
    product_name varchar(50) not null,
    category varchar(50) not null,
    price int not null,
    occasion varchar(30) not null
);

create table orders(
	order_id int primary key,
    customer_id varchar(5) not null,
    product_id int not null,
    quantity int not null,
    order_date varchar(15) not null,
    order_time time not null,
    delivery_date varchar(15) not null,
    delivery_time time not null,
    location varchar(50) not null,
    occasion varchar(30) not null,
    foreign key(customer_id) references customers(customer_id),
    foreign key(product_id) references products(product_id)
);

-- Quering the tables

select * from customers;

select * from products;

select * from orders;

-- Transforming Data

alter table orders add column order_date2 date;

update orders set order_date2 = str_to_date(order_date, '%d-%m-%Y');

alter table orders drop column order_date;

alter table orders rename column order_date2 to order_date;

alter table orders add column delivery_date2 date;

update orders set delivery_date2 = str_to_date(delivery_date, '%d-%m-%Y');

alter table orders drop column delivery_date;

alter table orders rename column delivery_date2 to delivery_date;

-- Answers to find

# Q1. Find the total revenue generated across all the products.
SELECT 
    SUM(orders.quantity * products.price) AS 'Total Revenue Generated'
FROM
    orders
        JOIN
    products ON orders.product_id = products.product_id;
    
# Q2. Calculate the average time taken in days for orders to deliver.
SELECT 
    ROUND(AVG(DATEDIFF(delivery_date, order_date)),
            2) AS 'Average Delivery Time in Days'
FROM
    orders;

    
# Q3. Find the average of customers spending on products.
SELECT 
    ROUND(AVG(orders.quantity * products.price), 2) AS 'Average of Customer Spending'
FROM
    products
        JOIN
    orders ON products.product_id = orders.product_id;

    
# Q4. List total revenue generated from every months of 2023.
SELECT 
    MONTHNAME(order_date) AS 'Month Name',
    SUM(orders.quantity * products.price) AS 'Total Revenue'
FROM
    orders
        JOIN
    products ON orders.product_id = products.product_id
GROUP BY MONTHNAME(order_date) , MONTH(order_date)
ORDER BY MONTH(order_date);

    
# Q5. Determine which 10 products are giving the most revenue.
SELECT 
    products.product_name AS `Product Name`,
    SUM(products.price * orders.quantity) AS `Total Revenue`
FROM
    products
        JOIN
    orders ON products.product_id = orders.product_id
GROUP BY `Product Name`
ORDER BY `Total Revenue` DESC
LIMIT 10;

# Q6. Calculate which product categories gave what revenue.
SELECT 
    products.category AS `Product Category`,
    SUM(products.price * orders.quantity) AS `Total Revenue`
FROM
    orders
        JOIN
    products ON orders.product_id = products.product_id
GROUP BY `Product Category`;

# Q7. List which 10 cities are placing the highest number of orders.
SELECT 
    customers.city AS `Customer City`,
    COUNT(orders.order_id) AS `Number of Orders`
FROM
    customers
        JOIN
    orders ON customers.customer_id = orders.customer_id
GROUP BY `Customer City`
ORDER BY `Number of Orders` DESC
LIMIT 10;

# Q8. Find the average revenue by morning, afternoon and evening.
SELECT 
    CASE
        WHEN orders.order_time < '12:00:00' THEN 'Morning'
        WHEN orders.order_time < '18:00:00' THEN 'Afternoon'
        ELSE 'Evening'
    END AS `Time of Day`,
    ROUND(AVG(orders.quantity * products.price), 2) AS `Average Revenue`
FROM
    orders
        JOIN
    products ON orders.product_id = products.product_id
GROUP BY `Time of Day`;

# Q9. Compare the total revenue generated from different occasions.
SELECT 
    o.occasion AS `Occasion`,
    SUM(o.quantity * p.price) AS `Total Revenue`
FROM
    orders AS o
        JOIN
    products AS p ON o.product_id = p.product_id
GROUP BY `Occasion`
ORDER BY `Total Revenue` DESC;

# Q10. Find out which products are most popular during specific occasions.
select
*
from
(
	SELECT 
    o.occasion AS `Occasion`,
    p.product_name AS `Product`,
    COUNT(o.order_id) AS `Number of Orders`,
    dense_rank() over(partition by o.occasion order by COUNT(o.order_id) desc) 
    as `Rank by Occasion`
FROM
    orders o
        JOIN
    products p ON o.product_id = p.product_id
GROUP BY `Product` , `Occasion`
) as `Products by Occasions`
where `Rank by Occasion` <= 5;

with Product_by_Occasions as
(
	SELECT 
		o.occasion AS `Occasion`,
		p.product_name AS `Product`,
		COUNT(o.order_id) AS `Number of Orders`,
		dense_rank() over(partition by o.occasion order by COUNT(o.order_id) desc) 
		as `Rank by Occasion`
	FROM
		orders AS o
			JOIN
		products AS p ON o.product_id = p.product_id
	GROUP BY `Product` , `Occasion`
)
SELECT * FROM Product_by_Occasions WHERE `Rank by Occasion` <= 5;
