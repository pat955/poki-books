package api

import (
	"database/sql"

	"github.com/pat955/poki_books/internal/database"
)

// Entry point to the DB
type apiConfig struct {
	DB *database.Queries
}

// use this to connect to the db
func connect(DBPATH string) *apiConfig {
	db, err := sql.Open("sqlite3", DBPATH)
	if err != nil {
		panic(err)
	}
	dbQueries := database.New(db)
	return &apiConfig{DB: dbQueries}
}
