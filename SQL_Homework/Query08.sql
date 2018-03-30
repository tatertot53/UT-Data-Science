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