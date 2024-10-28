package api

import (
	"context"
	"database/sql"

	_ "github.com/mattn/go-sqlite3"

	"github.com/pat955/poki_books/api/database"
)

var DB_PATH string = "../sql/poki_books.db"

// Entry point to the DB
type apiConfig struct {
	DB         *database.Queries
	GenericCtx context.Context
}

// Connects to database with a database path string.
func connect(DBPATH string) *apiConfig {
	db, err := sql.Open("sqlite3", DBPATH)
	if err != nil {
		panic(err)
	}
	dbQueries := database.New(db)
	return &apiConfig{DB: dbQueries, GenericCtx: context.Background()}
}

func Connect() *apiConfig {
	return connect(DB_PATH)
}
