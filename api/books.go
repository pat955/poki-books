package api

import (
	"fmt"

	"github.com/google/uuid"
	"github.com/pat955/poki_books/api/database"
)

type Book struct {
	Title   string
	Content string
	Notes   string
	Author  string
}

func AddBook(db_path string, book Book) error {
	cfg := connect(db_path)
	if book.Title == "" {
		return &NoTitleError{"unamed book"}
	} else if book.Content == "" {
		return &NoContentError{"empty book"}
	}
	if cfg == nil || cfg.DB == nil {
		return fmt.Errorf("failed to connect to the database")
	}

	newBook, err := cfg.DB.CreateBook(
		cfg.GenericCtx,
		database.CreateBookParams{
			ID:      uuid.New(),
			Title:   book.Title,
			Content: book.Content,
		})
	if err != nil {
		return err
	}
	fmt.Println(newBook)
	return nil
}

func GetAllBooks(db_path string) []database.Book {
	cfg := connect(db_path)
	books, err := cfg.DB.GetAllBooks(cfg.GenericCtx)
	if err != nil {
		panic(err)
	}
	return books
}

func GetContentByTitle(db_path, title string) string {
	cfg := connect(db_path)
	content, err := cfg.DB.GetContentByTitle(cfg.GenericCtx, title)
	if err != nil {
		panic(err)
	}
	return content
}
