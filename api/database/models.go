// Code generated by sqlc. DO NOT EDIT.
// versions:
//   sqlc v1.27.0

package database

import (
	"database/sql"
)

type Book struct {
	ID        interface{}
	Path      string
	Title     string
	Content   string
	Extension sql.NullString
	Notes     sql.NullString
}
