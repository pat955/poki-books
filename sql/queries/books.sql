-- name: AddBook :exec
INSERT INTO books(id, title, description, created_at, updated_at)
VALUES($1, $2, $3, $4, $5, $6, $7, $8)
RETURNING *;

-- name: RetrieveBooks :many
SELECT * FROM books;

-- name: DeleteBook :exec
DELETE FROM books
WHERE id = $1;

-- name: GetFeed :one
SELECT * FROM books
WHERE id = $1;
