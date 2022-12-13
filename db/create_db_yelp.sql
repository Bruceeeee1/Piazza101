CREATE DATABASE yelp_db;
CREATE USER 'Restaurant'@'%' IDENTIFIED BY 'Restaurant123';
GRANT ALL PRIVILEGES ON yelp_db.* TO 'Restaurant'@'%';
FLUSH PRIVILEGES;

CREATE USER 'Customer'@'%' IDENTIFIED BY 'Customer123';
GRANT ALL PRIVILEGES ON yelp_db.* TO 'Customer'@'%';
FLUSH PRIVILEGES;

CREATE USER 'Critic'@'%' IDENTIFIED BY 'Critic123';
GRANT ALL PRIVILEGES ON yelp_db.* TO 'Critic'@'%';
FLUSH PRIVILEGES;

-- Move into the database we just created
-- TO DO: if you changed the name of the
-- database above, you need to change it here too
Use yelp_db;

-- Put your DDl
CREATE TABLE RESTAURANT(
    restaurant_ID VARCHAR(20),
    city VARCHAR(30),
    zip INTEGER(10),
    street VARCHAR(30),
    states VARCHAR(20),
    emails VARCHAR(40),
    numbers VARCHAR(10),
    cuisine VARCHAR(20),
    names VARCHAR(30),
    descriptions VARCHAR(300),
    openinghours VARCHAR(30),
    PRIMARY KEY(restaurant_ID)
);

CREATE TABLE ANNOUNCEMENT(
    restaurant_ID VARCHAR(20),
    a_time DATE,
    a_details VARCHAR(300),
    PRIMARY KEY(restaurant_ID, a_details),
    FOREIGN KEY(restaurant_ID) REFERENCES RESTAURANT(restaurant_ID)
);

CREATE TABLE MENU(
    dish_ID VARCHAR(30),
    prices FLOAT(10),
    restaurant_ID VARCHAR(20),
    PRIMARY KEY(dish_ID),
    FOREIGN KEY(restaurant_ID) REFERENCES RESTAURANT(restaurant_ID)
);

CREATE TABLE CUSTOMER(
    customer_ID VARCHAR(20),
    birthday VARCHAR(10),
    passwords VARCHAR(30),
    username VARCHAR(20),
    age INTEGER(3),
    numbers VARCHAR(10),
    emails VARCHAR(40),
    PRIMARY KEY(customer_ID)
);

CREATE TABLE FAVORITERESTAURANT(
    restaurant_ID VARCHAR(20),
    customer_ID VARCHAR(20),
    PRIMARY KEY(restaurant_ID, customer_ID),
    FOREIGN KEY(restaurant_ID) REFERENCES RESTAURANT(restaurant_ID),
    FOREIGN KEY(customer_ID) REFERENCES CUSTOMER(customer_ID)
);

CREATE TABLE CRITIC(
    critic_ID VARCHAR(20),
    firstname VARCHAR(20),
    lastname VARCHAR(20),
    preference VARCHAR(40),
    age INTEGER(3),
    city VARCHAR(30),
    zip INTEGER(10),
    street VARCHAR(30),
    states VARCHAR(20),
    birthday VARCHAR(10),
    descriptions  VARCHAR(300),
    numbers VARCHAR(10),
    emails VARCHAR(40),
    PRIMARY KEY(critic_ID)
);

CREATE TABLE FAVORITECRITIC(
    customer_ID VARCHAR(20),
    critic_ID VARCHAR(20),
    PRIMARY KEY(customer_ID, critic_ID),
    FOREIGN KEY(customer_ID) REFERENCES CUSTOMER(customer_ID),
    FOREIGN KEY(critic_ID) REFERENCES CRITIC(critic_ID)
);

CREATE TABLE REVIEW(
    customer_ID VARCHAR(20),
    critic_ID VARCHAR(14),
    restaurant_ID VARCHAR(20),
    postdate DATE,
    trust_rating FLOAT(3),
    reviewdetails VARCHAR(300),
    PRIMARY KEY(customer_ID, critic_ID, restaurant_ID),
    FOREIGN KEY(customer_ID) REFERENCES CUSTOMER(customer_ID),
    FOREIGN KEY(critic_ID) REFERENCES CRITIC(critic_ID),
    FOREIGN KEY(restaurant_ID) REFERENCES RESTAURANT(restaurant_ID),
    CONSTRAINT trust_rating CHECK (trust_rating BETWEEN 1 AND 5)
);

CREATE TABLE RECOMMENDATION(
    restaurant_ID VARCHAR(20),
    critic_ID VARCHAR(20),
    PRIMARY KEY(restaurant_ID, critic_ID),
    FOREIGN KEY(restaurant_ID) REFERENCES RESTAURANT(restaurant_ID),
    FOREIGN KEY(critic_ID) REFERENCES CRITIC(critic_ID)
);

CREATE TABLE ORDERDETAILS(
    order_ID VARCHAR(20),
    ordertime DATE,
    totalprice FLOAT,
    PRIMARY KEY(order_ID)
);

CREATE TABLE ORDERS(
    order_ID VARCHAR(20),
    customer_ID VARCHAR(20),
    restaurant_ID VARCHAR(20),
    PRIMARY KEY(order_ID, customer_ID, restaurant_ID),
    FOREIGN KEY(customer_ID) REFERENCES CUSTOMER(customer_ID),
    FOREIGN KEY(order_ID) REFERENCES ORDERDETAILS(order_ID),
    FOREIGN KEY(restaurant_ID) REFERENCES RESTAURANT(restaurant_ID)
);

CREATE TABLE DISHES(
    order_ID VARCHAR(20),
    dish_name VARCHAR(30),
    price FLOAT,
    PRIMARY KEY(order_ID),
    FOREIGN KEY(order_ID) REFERENCES ORDERDETAILS(order_ID),
    FOREIGN KEY(dish_name) REFERENCES MENU(dish_ID)
);

-- Add sample data.
INSERT INTO RESTAURANT
    (restaurant_ID, city, zip, street, states, emails, numbers, cuisine, names, descriptions, openinghours)
VALUES
    ('00126782364928364729', 'boston', 02115, '480 Columbus Ave', 'MA', 'petit@gmail.com', 6178670600, 'French', 'Petit Bistro', 'great vibes and good food', '12AM-10PM'),
    ('00026374829376426358', 'los angeles', 90001, '13705 Ventura Blvd', 'CA', 'Trois@outlook.com', 8189892600, 'Spanish', 'Trois', 'incredible selection & awesome staff', '10AM-10PM'),
    ('00673946592735463729', 'new york', 10001, '167 W 74th St', 'NY', 'levain@gmail.com', 9174643769, 'Bakeries', 'Levain', 'best of the best cookies', '11AM-8PM');

INSERT INTO ANNOUNCEMENT
    (restaurant_ID, a_time, a_details)
VALUES
    ('00126782364928364729', '2020-12-05', 'our restaurant will be closed tomorrow on December 5th 2020'),
    ('00026374829376426358', '2011-10-15', 'we are back to the table'),
    ('00673946592735463729', '2008-05-23', 'we are hiring');

INSERT INTO MENU
    (dish_ID, prices, restaurant_ID)
VALUES
    ('chicken', 90, '00126782364928364729'),
    ('crab', 20, '00026374829376426358'),
    ('biscuit', 8, '00673946592735463729');

INSERT INTO CUSTOMER
    (customer_ID, birthday, passwords, username, age, numbers, emails)
VALUES
    ('16283746392013648946', '1999-10-01', 'abc123', 'bruce111', 23, 6179892739, 'bruce@gmail.com'),
    ('10496225562648399372', '1980-01-23', 'sjadkh', 'elonmask', 42, 9172839029, 'elon@outlook.com'),
    ('23527839263727361726', '2002-08-11', 'porsche', 'porsche1', 20, 8187263459, 'porsche@gmail.com');

INSERT INTO FAVORITERESTAURANT
    (restaurant_ID, customer_ID)
VALUES
    ('00126782364928364729', '16283746392013648946'),
    ('00026374829376426358', '10496225562648399372'),
    ('00673946592735463729', '23527839263727361726');

INSERT INTO CRITIC
    (critic_ID, firstname, lastname, preference, age, city, zip, street, states, birthday, descriptions, numbers, emails)
VALUES
    ('12046387322354', 'John', 'Ally', 'Asian & French', 30, 'boston', 02115, '150 Huntington Ave', 'MA', '1988-10-01', 'I love Chinese and French food', 6178259083, 'john@gmail.com'),
    ('00246473273829', 'Bruce', 'Grant', 'Sushi', 20, 'new york', 10023, '104W 71St', 'NY', '2002-09-20', 'Find the best restaurants', 8182738362, 'bruce@gmail.com'),
    ('26389297277288', 'Christina', 'Jiang', 'Asian & Spanish', 40, 'Seattle', 98108, '5930 6th Ave', 'WA', '1982-01-10', 'Taste more Chinese food', 2067623549, 'jiang@gmail.com');

INSERT INTO FAVORITECRITIC
    (customer_ID, critic_ID)
VALUES
    ('16283746392013648946', '12046387322354'),
    ('10496225562648399372', '00246473273829'),
    ('23527839263727361726', '26389297277288');

INSERT INTO REVIEW
    (customer_ID, critic_ID, restaurant_ID, postdate, trust_rating, reviewdetails)
VALUES
    ('16283746392013648946', '12046387322354', '00126782364928364729', '2020-10-01', 4.8, 'Petit Bistro has the best!!!! beef'),
    ('10496225562648399372', '00246473273829', '00026374829376426358', '2011-05-10', 3.2, 'Trois was good, you should try spaghetti with seafood'),
    ('23527839263727361726', '26389297277288', '00673946592735463729', '2001-01-20', 2.0, 'Levain cookoies does not taste good');

INSERT INTO RECOMMENDATION
    (restaurant_ID, critic_ID)
VALUES
    ('00126782364928364729', '12046387322354'),
    ('00026374829376426358', '00246473273829'),
    ('00673946592735463729', '26389297277288');

INSERT INTO ORDERDETAILS
    (order_ID, ordertime, totalprice)
VALUES
    ('1293637937362837482', '2022-11-21', 100.21),
    ('0283293748379000212', '2021-01-10', 50.68),
    ('0182643828478299370', '2019-06-01', 135.14);

INSERT INTO ORDERS
    (order_ID, customer_ID, restaurant_ID)
VALUES
    ('1293637937362837482', '16283746392013648946', '00126782364928364729'),
    ('0283293748379000212', '10496225562648399372', '00026374829376426358'),
    ('0182643828478299370', '23527839263727361726', '00673946592735463729');

INSERT INTO DISHES
    (order_ID, dish_name, price)
VALUES
    ('1293637937362837482', 'chicken', 90),
    ('0283293748379000212', 'crab', 20),
    ('0182643828478299370', 'biscuit', 8);