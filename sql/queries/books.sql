-- name: CreateBook :one
INSERT INTO books (
  id, title, content
) VALUES (
  ?, ?, ?
)
RETURNING *;

-- name: GetBookByID :one
SELECT * FROM books
WHERE id = ?;

-- name: GetAllBooks :many
SELECT * FROM books;

-- name: GetContentByID :one
SELECT content FROM books
WHERE id = ?;

-- name: GetContentByTitle :one
SELECT content FROM books
WHERE title = ?;