-- ============ TABLE 1: customers ============
CREATE TABLE customers (
    customer_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    email       TEXT        NOT NULL UNIQUE,
    full_name   TEXT        NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
-- ============ TABLE 2: orders ============
CREATE TABLE orders (
    order_id     BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id  BIGINT  NOT NULL
                 REFERENCES customers(customer_id),
    amount_cents INTEGER NOT NULL
                 CHECK (amount_cents >= 0),
    status       TEXT    NOT NULL DEFAULT 'pending',
    created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);
-- ============ INDEX on the FK column ============
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
