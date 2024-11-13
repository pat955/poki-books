-- name: AddNotesByPath :exec
UPDATE books SET notes = ? 
WHERE path LIKE ?;


-- name: GetNotesByPath :one
SELECT notes FROM books
WHERE path = ?;

-- name: ResetNotes :exec
UPDATE books SET notes = "";