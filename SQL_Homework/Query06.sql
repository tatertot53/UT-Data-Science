USE sakila;

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
    


    