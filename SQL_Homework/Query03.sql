use sakila;

#3a____________________________________________
alter table actor
add middle_name varchar(30) not null;


SELECT 
    first_name, middle_name, last_name
FROM
    actor;

#3b____________________________________________
alter table actor
modify middle_name BLOB;

#3c_____________________________________________
alter table actor
drop column middle_name;
