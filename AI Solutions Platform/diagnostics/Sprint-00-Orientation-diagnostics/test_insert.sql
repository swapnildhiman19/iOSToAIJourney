BEGIN;

INSERT INTO customers (email, full_name)
VALUES ('swapnildhiman1999@gmail.com', 'Swapnil'); -- <-- Added missing single quote here

INSERT INTO orders (customer_id, amount_cents, status)
VALUES (currval(pg_get_serial_sequence('customers', 'customer_id')), 9900000, 'will receive');

COMMIT;

-- Verify the results
SELECT * FROM customers;
SELECT * FROM orders;