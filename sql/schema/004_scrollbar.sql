-- +goose Up
ALTER TABLE books
ADD scrollbar_position TEXT;

-- +goose Down
ALTER TABLE books
DROP COLUMN scrollbar_position;
