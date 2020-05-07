-- CREATE DATABASE socialmeadia;
-- use socialmeadia;

create table User(
	user_id integer NOT NULL AUTO_INCREMENT, 
	firstname varchar(100),
	lastname varchar(100),
	email varchar(100),
	password_digest varchar(255),
	primary key(user_id)

);

create table Phone(
	user_id integer NOT NULL,
	telephone_no varchar(50),
	area_code varchar(10),
	
	primary key(user_id,telephone_no),

	foreign key(user_id)
	references User(user_id) on delete cascade on update cascade
);


create table Address(
	user_id integer NOT NULL,
	street_name varchar(100),
	city varchar(100),
	country varchar(50),

	primary key(user_id),

	foreign key(user_id)
	references User(user_id) on delete cascade on update cascade

);