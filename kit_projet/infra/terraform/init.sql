-- Script SQL pour créer la table et insérer des données
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(100)
);

INSERT INTO employees (name, role) VALUES
('Alice', 'Engineer'),
('Bob', 'Manager')
ON CONFLICT DO NOTHING;
