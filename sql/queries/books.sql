-- name: CreateBook :one
INSERT INTO books (id, created_at, updated_at, title, content, author)
(id, title, content, author) VALUES ($1, $4, $5, $6)
RETURNING *;

-- name: GetBookByID :one
SELECT * FROM books
WHERE id = $1;

-- name: GetAllBooks :many
SELECT * FROM books;