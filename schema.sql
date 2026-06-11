CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    note TEXT,
    date DATE NOT NULL
);

INSERT INTO expenses (category, amount, note, date) VALUES 
('Food', 15.50, 'Banku + Soup', '2026-04-10'),
('Transport', 8.00, 'Trotro to town', '2026-04-10'),
('Data', 20.00, 'MTN bundle', '2026-04-11');
