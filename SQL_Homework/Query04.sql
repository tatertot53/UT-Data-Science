USE sakila;

#4a_____________________________________________________________
SELECT 
    last_name, COUNT(last_name) AS 'num'
FROM
    actor
GROUP BY last_name;
 
 #4b_____________________________________________________________
SELECT 
    last_name, COUNT(last_name) AS 'num'
FROM
    actor
GROUP BY last_name
HAVING COUNT(last_name) >= 2;

#4c_______________________________________________________________
UPDATE actor 
SET first_name = 'HARPO'
WHERE First_name = "GROUCHO" AND last_name = "WILLIAMS";

#4d________________________________________________________________
SELECT 
    *
FROM
    actor
WHERE
    first_name = 'HARPO';

UPDATE actor 
SET 
    first_name = IF(actor_id = 172,
        'GROUCHO',
        'MUCHO GROUCHO')
WHERE
    actor_id = 172;

SELECT 
    first_name
FROM
    actor;


    
