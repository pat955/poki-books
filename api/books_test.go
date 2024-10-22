package api

import (
	"testing"
)

// Constant of test database
var DB_PATH_TEST string = "../sql/test.db"

// Testcase struct
type Case struct {
	Book               Book
	ExpectedErr        bool
	ExpectedTotalBooks int
}

var addBookCases = []Case{
	{Book{Title: "Title", Content: "contnetmte t,t estestetm tetet, yeah."}, false, 1},
	{Book{Title: "ANOTHER TITLE", Content: "something something"}, false, 2},
	{Book{Title: ""}, true, 2},                // NoTitleError
	{Book{Title: "No content test"}, true, 2}, // NoContentError
}

// Testing AddBook function, checks if the book is actually added into the db or if the expected error is presented.
func TestAddBook(t *testing.T) {
	for _, test := range addBookCases {
		if err := AddBook(DB_PATH_TEST, test.Book); (err != nil) != test.ExpectedErr {
			t.Errorf("Output %v not equal to expected %v", err, test.ExpectedErr)
		}
		if i := len(GetAllBooks(DB_PATH_TEST)); i != test.ExpectedTotalBooks {
			t.Errorf("Output %v not equal to expected %v", i, test.ExpectedTotalBooks)
		}
	}
}

var getContentCases = []Book{
	{Title: "we testing", Content: "some content"},
	{Title: "second testcase", Content: "weirddddddddddddddddddddddddddddd"},
}

// Testing GetContentTitle function, adds book to db then gets content with title.
func TestGetContentTitle(t *testing.T) {
	for _, book := range getContentCases {
		err := AddBook(DB_PATH_TEST, book)
		if err != nil {
			panic(err)
		}
		title := book.Title
		expectedContent := book.Content
		if content := GetContentByTitle(DB_PATH_TEST, title); content != expectedContent {
			t.Errorf("Output %v not equal to expected %v", content, expectedContent)
		}
	}
}
