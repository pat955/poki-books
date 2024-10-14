-- name: CreateBook :one
INSERT INTO books (
  id, created_at, updated_at, title
) VALUES (
  ?, ?, ?, ?
)
RETURNING *;

-- name: GetBookByID :one
SELECT * FROM books
WHERE id = ?;

-- name: GetAllBooks :many
SELECT * FROM books;