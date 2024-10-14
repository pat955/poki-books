package api

import (
	"context"
	"fmt"
	"time"

	"github.com/google/uuid"
	"github.com/pat955/poki_books/internal/database"
)

func AddBook(title string) error {
	if title == "" {
		return NoTitleError{}
	}
	ctx := context.Background()
	cfg := connect("../sql/poki_books.db")

	newBook, err := cfg.DB.CreateBook(
		ctx,
		database.CreateBookParams{
			ID:        uuid.New(),
			CreatedAt: time.Now().UTC(),
			UpdatedAt: time.Now().UTC(),
			Title:     title,
		})
	if err != nil {
		return (err)
	}
	fmt.Println(newBook)
	return nil
}

func GetAllBooks() []database.Book {
	ctx := context.Background()
	cfg := connect("../sql/poki_books.db")
	books, err := cfg.DB.GetAllBooks(ctx)
	if err != nil {
		panic(err)
	}
	return books
}
