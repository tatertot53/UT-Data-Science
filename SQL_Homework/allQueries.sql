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

#5a____________________________________________
SELECT 
    *
FROM
    address;

CREATE TABLE address (
    address_id INTEGER NOT NULL AUTO_INCREMENT,
    address VARCHAR(250) NOT NULL,
    address2 VARCHAR(250),
    district VARCHAR(100),
    city_id INTEGER(4) UNIQUE,
    postal_code INT(5),
    phone INTEGER(12),
    location BLOB,
    last_update DATETIME NOT NULL,
    PRIMARY KEY (address_id)
);

#6a________________________________________________
SELECT 
    *
FROM
    staff;
    
SELECT 
    s.first_name, s.last_name, a.address
FROM
    staff s
        LEFT JOIN
    address a ON s.address_id = a.address_id;

#6b_________________________________________________
SELECT 
    *
FROM
    payment;
    
SELECT 
    SUM(p.amount) AS Total_Rung_Up,
    p.payment_date AS August_2005,
    s.first_name,
    s.last_name
FROM
    staff s
        LEFT JOIN
    payment p ON s.staff_id = p.staff_id
WHERE
    p.payment_date LIKE '2005-08%';
    
#6c_________________________________________________
SELECT 
    f.title AS Film_Title, COUNT(a.actor_id) AS Number_of_Actors
FROM
    film_actor a
        INNER JOIN
    film f ON f.film_id = a.film_id
GROUP BY f.title;

#6d_________________________________________________
SELECT 
    f.title AS Film_Title,
    (SELECT 
            COUNT(*)
        FROM
            inventory i
        WHERE
            f.film_id = i.film_id) AS Number_of_Copies
FROM
    film f
WHERE
    title = 'HUNCHBACK IMPOSSIBLE';
    
#6e_________________________________________________
SELECT 
    SUM(p.amount) AS Sum_of_PMT_by_Customer,
    c.first_name,
    c.last_name
FROM
    customer c
        LEFT JOIN
    payment p ON c.customer_id = p.customer_id
GROUP BY c.last_name;
    
#7a___________________________________________________
SELECT 
    f.title AS Film_Title
FROM
    film f
WHERE
    f.title LIKE 'K%'
        OR f.title LIKE 'Q%'
        AND (SELECT 
            language_id
        FROM
            sakila.language
        WHERE
            language_id = 1);

 #7b___________________________________________________   
SELECT 
    a.first_name, a.last_name
FROM
    actor a
WHERE
    a.actor_id IN (SELECT 
            fa.actor_id
        FROM
            film_actor fa
        WHERE
            fa.film_id IN (SELECT 
                    f.film_id
                FROM
                    film f
                WHERE
                    f.title = 'Alone Trip'));

#7c_____________________________________________________
SELECT 
    c.first_name, c.last_name, c.email
FROM
    customer c
        LEFT JOIN
    address a ON c.address_id = a.address_id
        LEFT JOIN
    city ON a.city_id = city.city_id
        LEFT JOIN
    country ON city.country_id = country.country_id
WHERE
    country.country = 'Canada';

#7d______________________________________________________
SELECT 
    f.title AS Family_Movies
FROM
    film f
WHERE
    f.film_id IN (SELECT 
            fc.film_id
        FROM
            film_category fc
        WHERE
            fc.category_id IN (SELECT 
                    c.category_id
                FROM
                    category c
                WHERE
                    c.name = 'FAMILY'));

#7e_______________________________________________________
SELECT 
    f.title AS Most_Rented_Title,
    COUNT(r.rental_date) AS Number_of_Rentals
FROM
    film f
        JOIN
    inventory i ON f.film_id = i.film_id
        JOIN
    rental r ON i.inventory_id = r.inventory_id
GROUP BY Most_Rented_Title
ORDER BY Number_of_Rentals DESC;
    
#7f_______________________________________________________
SELECT 
    s.store_id,
    CONCAT('$', FORMAT(SUM(amount), 2)) AS Total_Revenue
FROM
    store s,
    staff,
    payment p
WHERE
    s.store_id = staff.store_id
        AND staff.staff_id = p.staff_id
GROUP BY s.store_id;

#7g________________________________________________________
SELECT 
    s.store_id, city, country
FROM
    store s,
    address a,
    city,
    country c
WHERE
    s.address_id = a.address_id
        AND a.city_id = city.city_id
        AND city.country_id = c.country_id;

#7h_________________________________________________________
SELECT 
    c.name AS Genre, SUM(p.amount) AS Total_Revenue
FROM
    category c
        JOIN
    film_category fc ON c.category_id = fc.category_id
        JOIN
    inventory i ON fc.film_id = i.film_id
        JOIN
    rental r ON i.inventory_id = r.inventory_id
        JOIN
    payment p ON r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY SUM(p.amount) DESC;

#8a_________________________________________________________
CREATE VIEW top_five_genres AS
    SELECT 
        category.name AS 'Genre',
        SUM(payment.amount) AS 'Gross Revenue'
    FROM
        category
            JOIN
        film_category ON category.category_id = film_category.category_id
            JOIN
        inventory ON film_category.film_id = inventory.film_id
            JOIN
        rental ON inventory.inventory_id = rental.inventory_id
            JOIN
        payment ON rental.rental_id = payment.rental_id
    GROUP BY category.name
    ORDER BY SUM(payment.amount) DESC
    LIMIT 5
;

#8b__________________________________________________________
SELECT 
    *
FROM
    top_five_genres;

#8c__________________________________________________________
drop view top_five_genres;