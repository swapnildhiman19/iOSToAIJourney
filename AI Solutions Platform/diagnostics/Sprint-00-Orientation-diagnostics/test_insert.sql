BEGIN;

-- Fixture identity is synthetic on purpose: the `.invalid` TLD is IANA-reserved
-- and can never resolve to a real mailbox. Closes the orientation carry-forward
-- "replace the real email in test_insert.sql with a synthetic identity"
-- (recorded July 25, 2026).
INSERT INTO customers (email, full_name)
VALUES ('learner@example.invalid', 'Learner One'); -- <-- Added missing single quote here

INSERT INTO orders (customer_id, amount_cents, status)
VALUES (currval(pg_get_serial_sequence('customers', 'customer_id')), 9900000, 'will receive');

COMMIT;

-- Verify the results
SELECT * FROM customers;
SELECT * FROM orders;