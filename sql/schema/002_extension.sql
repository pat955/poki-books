-- +goose Up
ALTER TABLE books
ADD extension TEXT;

-- +goose Down
ALTER TABLE books
DROP COLUMN extension;
