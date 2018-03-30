use sakila;

#2a_________________________________________________
SELECT 
    actor_id, first_name, last_name
FROM
    actor
WHERE
    first_name = 'Joe';

#2b__________________________________________________
SELECT 
    *
FROM
    actor
WHERE
    last_name LIKE '%gen%';

#2c__________________________________________________
SELECT 
    last_name, first_name
FROM
    actor
WHERE
    last_name LIKE '%li%'
ORDER BY last_name , first_name;

#2d____________________________________________________
SELECT 
    country_id, country
FROM
    country
WHERE
    country IN ('Afghanistan' , 'Bangladesh', 'China');
