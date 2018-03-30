USE sakila;

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

