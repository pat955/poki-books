package api

import (
	"context"
	"database/sql"

	_ "github.com/mattn/go-sqlite3"

	"github.com/pat955/poki_books/internal/database"
)

// Entry point to the DB
type apiConfig struct {
	DB         *database.Queries
	GenericCtx context.Context
}

// use this to connect to the db
func connect(DBPATH string) *apiConfig {
	db, err := sql.Open("sqlite3", DBPATH)
	if err != nil {
		panic(err)
	}
	dbQueries := database.New(db)
	return &apiConfig{DB: dbQueries, GenericCtx: context.Background()}
}
