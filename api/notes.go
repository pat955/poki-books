package api

import (
	"database/sql"
	"fmt"

	"github.com/pat955/poki_books/api/database"
)

// Add notes using path as identifier
func AddNotesByPath(db_path, notes, path string) error {
	cfg := connect(db_path)
	if cfg == nil || cfg.DB == nil {
		return fmt.Errorf("failed to connect to the database")
	}
	err := cfg.DB.AddNotesByPath(
		cfg.GenericCtx,
		database.AddNotesByPathParams{
			Notes: sql.NullString{String: notes, Valid: true},
			Path:  path,
		})
	if err != nil {
		return err
	}
	return nil
}

// Get notes with path as the identifier
func GetNotesByPath(db_path, path string) (string, error) {
	cfg := connect(db_path)
	if cfg == nil || cfg.DB == nil {
		return "", fmt.Errorf("failed to connect to the database")
	}
	notes, err := cfg.DB.GetNotesByPath(
		cfg.GenericCtx,
		path,
	)
	if err != nil {
		return "", err
	}
	return notes.String, nil
}
