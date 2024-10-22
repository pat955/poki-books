package api

import (
	"testing"
)

var DB_PATH_TEST string = "../sql/test.db"

type Case struct {
	Book               Book
	ExpectedErr        bool
	ExpectedTotalBooks int
}

var addTests = []Case{
	{Book{Title: "Title", Content: "contnetmte t,t estestetm tetet, yeah."}, false, 1},
	{Book{Title: "ANOTHER TITLE", Content: "something something"}, false, 2},
	{Book{Title: ""}, true, 2},                // NoTitleError
	{Book{Title: "No content test"}, true, 2}, // NoContentError
}

func TestAddBook(t *testing.T) {
	for _, test := range addTests {
		if err := AddBook(DB_PATH_TEST, test.Book); (err != nil) != test.ExpectedErr {
			t.Errorf("Output %v not equal to expected %v", err, test.ExpectedErr)
		}
		if i := len(GetAllBooks(DB_PATH_TEST)); i != test.ExpectedTotalBooks {
			t.Errorf("Output %v not equal to expected %v", i, test.ExpectedTotalBooks)
		}
	}
}

var contentCases = []Book{
	{Title: "we testing", Content: "some content"},
	{Title: "second testcase", Content: "weirddddddddddddddddddddddddddddd"},
}

func TestGetContentTitle(t *testing.T) {
	for _, book := range contentCases {
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
