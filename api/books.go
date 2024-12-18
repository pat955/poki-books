package api

import (
	"fmt"

	"github.com/google/uuid"
	"github.com/pat955/poki_books/api/database"
)

type Book struct {
	Path      string
	Title     string
	Content   string
	Extension string
	Notes     string
	Author    string
}

// Connects to db and adds book to database
func AddBook(db_path string, book Book) error {
	cfg := connect(db_path)
	if cfg == nil || cfg.DB == nil {
		return fmt.Errorf("failed to connect to the database")
	}
	if book.Path == "" {
		return &NoPathError{"no path!"}
	}
	_, err := cfg.DB.CreateBook(
		cfg.GenericCtx,
		database.CreateBookParams{
			ID:      uuid.New(),   // uuid
			Path:    book.Path,    // string
			Title:   book.Title,   // string
			Content: book.Content, // string
		})
	if err != nil {
		return err
	}
	// TODO make a unable to make book custom error
	return nil
}

// Gets all books from db in a slice with books structs
func GetAllBooks(db_path string) ([]Book, error) {
	cfg := connect(db_path)
	if cfg == nil || cfg.DB == nil {
		return []Book{}, fmt.Errorf("failed to connect to the database")
	}
	books, err := cfg.DB.GetAllBooks(cfg.GenericCtx)
	if err != nil {
		panic(err)
	}
	convertedBook := []Book{}
	for _, book := range books {
		convertedBook = append(convertedBook, convertToPyBook(book))
	}
	return convertedBook, nil
}

// From database gets content with title as argument
func GetContentByTitle(db_path, title string) (string, error) {
	cfg := connect(db_path)
	if cfg == nil || cfg.DB == nil {
		return "", fmt.Errorf("failed to connect to the database")
	}
	content, err := cfg.DB.GetContentByTitle(cfg.GenericCtx, title)
	if err != nil {
		panic(err)
	}
	return content, nil
}

func convertToPyBook(book database.Book) Book {
	return Book{
		Path:      book.Path,
		Title:     book.Title,
		Content:   book.Content,
		Extension: book.Extension.String,
	}
}

// Returns book from db with path as argument
func GetBookByPath(db_path, path string) (Book, error) {
	cfg := connect(db_path)
	if cfg == nil || cfg.DB == nil {
		return Book{}, fmt.Errorf("failed to connect to the database")
	}
	book, err := cfg.DB.GetBookByPath(cfg.GenericCtx, path)
	if err != nil {
		return Book{}, err
	}
	return convertToPyBook(book), nil
}

// Removes book from database
func RemoveBook(db_path, path string) error {
	cfg := connect(db_path)
	if cfg == nil || cfg.DB == nil {
		return fmt.Errorf("failed to connect to the database")
	}
	err := cfg.DB.RemoveBook(cfg.GenericCtx, path)
	if err != nil {
		return err
	}
	return nil
}

// Removes all rows from table
func ResetTable(dp_path string) error {
	cfg := connect(dp_path)
	if cfg == nil || cfg.DB == nil {
		return fmt.Errorf("failed to connect to the database")
	}
	err := cfg.DB.ResetTable(cfg.GenericCtx)
	if err != nil {
		return err
	}
	return nil
}
