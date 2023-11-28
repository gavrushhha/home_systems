CREATE TABLE customers (
    customer_id int primary key,
    firstName text,
    lastName text,
    email text
);

create table products (
    product_id int primary key,
    productName text,
    productPrice int
);

create table orders (
  order_id int primary key,
  customer_id int,
  orderDate date,
  totalAmount int,
  constraint fk_customer foreign key (customer_id) references customers(customer_id)
);

create table orderItems (
    orderItem_id int primary key,
    order_id int references orders(order_id),
    product_id int references products(product_id),
    quantity int,
    subtotal int
);


insert into products 
(product_id, productName, productPrice) VALUES 
                                                (1, 'Печенье Farella', 456),
                                                (2, 'Мармелад Frutty', 120),
                                                (3, 'Яблоки Грин', 230),
                                                (4, 'Вода фильрованная', 45),
                                                (5, 'Конфетки', 130); 

insert into customers 
(customer_id, firstName, lastName, email) VALUES 
                                                    (1, 'Ivan', 'Ivanov', 'ivanivivan@gmail.com'),
                                                    (2, 'Pavel', 'Rogin', 'pavlik@gmail.com'),
                                                    (3, 'Roman', 'Gromov', 'grooooom@gmail.com'),
                                                    (4, 'Sofia', 'Iakovleva', 'sofja.iakovleva@gmail.com'), 
                                                    (5, 'Dima', 'Pupkin', 'pupok@gmail.com');

-- сценарий 1
begin;
insert into orders (order_id, customer_id, orderDate, totalAmount)
VALUES (2, 2, current_timestamp, 120);

insert into orderItems (orderItem_id, order_id, product_id, quantity, subtotal) VALUES (2, 2, 2, 2, 120);
update orders set totalAmount = (select sum(subtotal) from orderItems where orderItems.order_id = 1) where order_id=1;
commit;

-- сценарий 2
begin;
update customers set email='iakovleva.sofja@gmail.com' where customer_id=4;
commit;

-- сценарий 3
begin;
insert into products (product_id, productName, productPrice) VALUES (6, 'Кофе', 300);
commit;
abort;