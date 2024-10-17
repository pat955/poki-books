-- +goose Up
CREATE TABLE books (
    id UUID PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

-- +goose Down
DROP TABLE books;
