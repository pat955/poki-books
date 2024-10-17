package api

import (
	"fmt"

	"github.com/google/uuid"
	"github.com/pat955/poki_books/internal/database"
)

var DB_PATH string = "../sql/poki_books.db"

type Book struct {
	Title   string
	Content string
	Notes   string
	Author  string
}

func AddBook(book Book) error {
	if book.Title == "" {
		return NoTitleError{}
	} else if book.Content == "" {
		return NoContentError{}
	}
	cfg := connect(DB_PATH)

	newBook, err := cfg.DB.CreateBook(
		cfg.GenericCtx,
		database.CreateBookParams{
			ID:      uuid.New(),
			Title:   book.Title,
			Content: book.Content,
		})
	if err != nil {
		return (err)
	}
	fmt.Println(newBook)
	return nil
}

func GetAllBooks() []database.Book {
	cfg := connect(DB_PATH)
	books, err := cfg.DB.GetAllBooks(cfg.GenericCtx)
	if err != nil {
		panic(err)
	}
	return books
}

func GetContentByTitle(title string) string {
	cfg := connect(DB_PATH)
	content, err := cfg.DB.GetContentByTitle(cfg.GenericCtx, title)
	if err != nil {
		panic(err)
	}
	return content
}
