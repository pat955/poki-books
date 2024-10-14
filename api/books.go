package api

import (
	"context"
	"fmt"
	"time"

	"github.com/google/uuid"
	"github.com/pat955/poki_books/internal/database"
)

func AddBook() {
	ctx := context.Background()
	cfg := connect("/sql/poki_books.db")

	newBook, err := cfg.DB.CreateBook(
		ctx,
		database.CreateBookParams{
			ID:        uuid.New(),
			CreatedAt: time.Now().UTC(),
			UpdatedAt: time.Now().UTC(),
			Title:     "title",
		})
	if err != nil {
		panic(err)
	}
	fmt.Println(newBook)

}
