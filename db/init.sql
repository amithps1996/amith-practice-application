CREATE TABLE test (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL
);

INSERT INTO test (message) VALUES ('Hello from PostgreSQL!');
