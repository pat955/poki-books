// Code generated by sqlc. DO NOT EDIT.
// versions:
//   sqlc v1.27.0
// source: notes.sql

package database

import (
	"context"
	"database/sql"
)

const addNotesByPath = `-- name: AddNotesByPath :exec
UPDATE books SET notes = ? 
WHERE path LIKE ?
`

type AddNotesByPathParams struct {
	Notes sql.NullString
	Path  string
}

func (q *Queries) AddNotesByPath(ctx context.Context, arg AddNotesByPathParams) error {
	_, err := q.db.ExecContext(ctx, addNotesByPath, arg.Notes, arg.Path)
	return err
}

const getNotesByPath = `-- name: GetNotesByPath :one
SELECT notes FROM books
WHERE path = ?
`

func (q *Queries) GetNotesByPath(ctx context.Context, path string) (sql.NullString, error) {
	row := q.db.QueryRowContext(ctx, getNotesByPath, path)
	var notes sql.NullString
	err := row.Scan(&notes)
	return notes, err
}

const resetNotes = `-- name: ResetNotes :exec
UPDATE books SET notes = ""
`

func (q *Queries) ResetNotes(ctx context.Context) error {
	_, err := q.db.ExecContext(ctx, resetNotes)
	return err
}
