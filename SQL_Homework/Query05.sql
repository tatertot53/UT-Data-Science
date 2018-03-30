USE sakila;

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
