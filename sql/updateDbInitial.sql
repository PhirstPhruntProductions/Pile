--The initial DB setup file------------------------------------------

--Create User Table
create table users
(
id integer,  --TODO: Make these uuid()s
name varchar(255) not null,
email varchar(255) not null unique,
college_id integer not null,
primary key (id),
foreign key (college_id) referneces colleges(id)
)


--Create College Table
create table colleges
(
id integer,
name varchar(255) not null unique,
primary key (id)
)


--Create Item Table
create table items
(
id integer,
user_id integer not null,
college_id integer not null,
title varchar(255) not null,
price decimal,
description varchar(255),
image_path varchar(255) unique,
primary key (id),
foriegn key (user_id) references users(id),
foreign key (college_id) references colleges(id)
)
