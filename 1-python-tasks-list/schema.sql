CREATE TABLE the_tasks_table (
    issue_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    status VARCHAR(50) DEFAULT 'Pending',
    created_date DATE DEFAULT CURRENT_DATE
);
