// Code generated by sqlc. DO NOT EDIT.
// versions:
//   sqlc v1.27.0
// source: books.sql

package database

import (
	"context"
	"time"
)

const createBook = `-- name: CreateBook :one
INSERT INTO books (
  id, created_at, updated_at, title
) VALUES (
  ?, ?, ?, ?
)
RETURNING id, created_at, updated_at, title
`

type CreateBookParams struct {
	ID        interface{}
	CreatedAt time.Time
	UpdatedAt time.Time
	Title     string
}

func (q *Queries) CreateBook(ctx context.Context, arg CreateBookParams) (Book, error) {
	row := q.db.QueryRowContext(ctx, createBook,
		arg.ID,
		arg.CreatedAt,
		arg.UpdatedAt,
		arg.Title,
	)
	var i Book
	err := row.Scan(
		&i.ID,
		&i.CreatedAt,
		&i.UpdatedAt,
		&i.Title,
	)
	return i, err
}

const getAllBooks = `-- name: GetAllBooks :many
SELECT id, created_at, updated_at, title FROM books
`

func (q *Queries) GetAllBooks(ctx context.Context) ([]Book, error) {
	rows, err := q.db.QueryContext(ctx, getAllBooks)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var items []Book
	for rows.Next() {
		var i Book
		if err := rows.Scan(
			&i.ID,
			&i.CreatedAt,
			&i.UpdatedAt,
			&i.Title,
		); err != nil {
			return nil, err
		}
		items = append(items, i)
	}
	if err := rows.Close(); err != nil {
		return nil, err
	}
	if err := rows.Err(); err != nil {
		return nil, err
	}
	return items, nil
}

const getBookByID = `-- name: GetBookByID :one
SELECT id, created_at, updated_at, title FROM books
WHERE id = ?
`

func (q *Queries) GetBookByID(ctx context.Context, id interface{}) (Book, error) {
	row := q.db.QueryRowContext(ctx, getBookByID, id)
	var i Book
	err := row.Scan(
		&i.ID,
		&i.CreatedAt,
		&i.UpdatedAt,
		&i.Title,
	)
	return i, err
}
