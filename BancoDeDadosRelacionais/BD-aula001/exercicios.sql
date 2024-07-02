PROBLEMA:2602 - Select Básico
LINGUAGEM:PostgreSQL (psql 9.4.19)
---------------------------------------
SELECT name
FROM customers WHERE state = 'RS'
--------------------------------------
PROBLEMA: 2603 - Endereço dos Clientes
LINGUAGEM: PostgreSQL (psql 9.4.19)
--------------------------------------
SELECT name,street
FROM customers WHERE city = 'Porto Alegre'

PROBLEMA:2604 - Menores que 10 ou Maiores que 100
LÍNGUA:PostgreSQL (psql 9.4.19)

SELECT id, name
FROM products
WHERE price < 10 OR price > 100;

PROBLEMA:2605 - Representantes Executivos
LÍNGUA:PostgreSQL (psql 9.4.19)

SELECT p.name AS product_name, pr.name AS provider_name
FROM products p
JOIN providers pr ON p.id_providers = pr.id
JOIN categories c ON p.id_categories = c.id
WHERE c.id = 6;

PROBLEMA:2606 - Categorias
LÍNGUA:PostgreSQL (psql 9.4.19)

SELECT p.id, p.name
FROM products p
JOIN categories c ON p.id_categories = c.id
WHERE c.name LIKE 'super%';

PROBLEMA:2613 - Filmes em Promoção
LÍNGUA:PostgreSQL (psql 9.4.19)

SELECT m.id, m.name
FROM movies m
JOIN prices p ON m.id_prices = p.id
WHERE p.value < 2.00;
