-- +goose Up
ALTER TABLE books
ADD notes TEXT;

-- +goose Down
ALTER TABLE books
DROP COLUMN notes;
