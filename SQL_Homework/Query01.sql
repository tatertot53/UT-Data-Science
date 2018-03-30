use sakila;

#1a___________________________________________________
SELECT 
    first_name, last_name
FROM
    actor;

#1b____________________________________________________
SELECT 
    CONCAT(first_name, ' ', last_name) AS 'Actor Name'
FROM
    actor; 