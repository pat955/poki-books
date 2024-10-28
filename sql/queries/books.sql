-- name: CreateBook :one
INSERT INTO books (
  id, path, title, content
) VALUES (
  ?, ?, ?, ?
)
RETURNING *;

-- name: RemoveBook :exec
DELETE FROM books 
WHERE path = ?;


-- name: GetAllBooks :many
SELECT * FROM books;


-- name: GetContentByTitle :one
SELECT content FROM books
WHERE title = ?;

-- name: GetContentByPath :one
SELECT content FROM books
WHERE path = ?;


-- name: GetBookByPath :one
SELECT * FROM books
WHERE path = ?;

-- name: GetBookByID :one
SELECT * FROM books
WHERE id = ?;


-- name: ResetTable :exec
DELETE FROM books;