// Code generated by sqlc. DO NOT EDIT.
// versions:
//   sqlc v1.27.0
// source: books.sql

package database

import (
	"context"
)

const createBook = `-- name: CreateBook :one
INSERT INTO books (
  id, path, title, content
) VALUES (
  ?, ?, ?, ?
)
RETURNING id, path, title, content, extension, notes
`

type CreateBookParams struct {
	ID      interface{}
	Path    string
	Title   string
	Content string
}

func (q *Queries) CreateBook(ctx context.Context, arg CreateBookParams) (Book, error) {
	row := q.db.QueryRowContext(ctx, createBook,
		arg.ID,
		arg.Path,
		arg.Title,
		arg.Content,
	)
	var i Book
	err := row.Scan(
		&i.ID,
		&i.Path,
		&i.Title,
		&i.Content,
		&i.Extension,
		&i.Notes,
	)
	return i, err
}

const getAllBooks = `-- name: GetAllBooks :many
SELECT id, path, title, content, extension, notes FROM books
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
			&i.Path,
			&i.Title,
			&i.Content,
			&i.Extension,
			&i.Notes,
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
SELECT id, path, title, content, extension, notes FROM books
WHERE id = ?
`

func (q *Queries) GetBookByID(ctx context.Context, id interface{}) (Book, error) {
	row := q.db.QueryRowContext(ctx, getBookByID, id)
	var i Book
	err := row.Scan(
		&i.ID,
		&i.Path,
		&i.Title,
		&i.Content,
		&i.Extension,
		&i.Notes,
	)
	return i, err
}

const getBookByPath = `-- name: GetBookByPath :one
SELECT id, path, title, content, extension, notes FROM books
WHERE path = ?
`

func (q *Queries) GetBookByPath(ctx context.Context, path string) (Book, error) {
	row := q.db.QueryRowContext(ctx, getBookByPath, path)
	var i Book
	err := row.Scan(
		&i.ID,
		&i.Path,
		&i.Title,
		&i.Content,
		&i.Extension,
		&i.Notes,
	)
	return i, err
}

const getContentByPath = `-- name: GetContentByPath :one
SELECT content FROM books
WHERE path = ?
`

func (q *Queries) GetContentByPath(ctx context.Context, path string) (string, error) {
	row := q.db.QueryRowContext(ctx, getContentByPath, path)
	var content string
	err := row.Scan(&content)
	return content, err
}

const getContentByTitle = `-- name: GetContentByTitle :one
SELECT content FROM books
WHERE title = ?
`

func (q *Queries) GetContentByTitle(ctx context.Context, title string) (string, error) {
	row := q.db.QueryRowContext(ctx, getContentByTitle, title)
	var content string
	err := row.Scan(&content)
	return content, err
}

const removeBook = `-- name: RemoveBook :exec
DELETE FROM books 
WHERE path = ?
`

func (q *Queries) RemoveBook(ctx context.Context, path string) error {
	_, err := q.db.ExecContext(ctx, removeBook, path)
	return err
}

const resetTable = `-- name: ResetTable :exec
DELETE FROM books
`

func (q *Queries) ResetTable(ctx context.Context) error {
	_, err := q.db.ExecContext(ctx, resetTable)
	return err
}
