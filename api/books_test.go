package api

import (
	"os/exec"
	"testing"
)

type Case struct {
	Book               Book
	ExpectedErr        bool
	ExpectedTotalBooks int
}

var TotalBooksNow int = len(GetAllBooks())

var addTests = []Case{
	{Book{Title: "Title", Content: "contnetmte t,t estestetm tetet, yeah."}, false, TotalBooksNow + 1},
	{Book{Title: "ANOTHER TITLE", Content: "something something"}, false, TotalBooksNow + 2},
	{Book{Title: ""}, true, TotalBooksNow + 2},                // NoTitleError
	{Book{Title: "No content test"}, true, TotalBooksNow + 2}, // NoContentError
}

func setupTestDB() {
	exec.Command("/bin/sh", "./scripts/test.sh")
}

func TestAddBook(t *testing.T) {
	setupTestDB()
	for _, test := range addTests {
		if err := AddBook(test.Book); (err != nil) != test.ExpectedErr {
			t.Errorf("Output %v not equal to expected %v", err, test.ExpectedErr)
		}
		if i := len(GetAllBooks()); i != test.ExpectedTotalBooks {
			t.Errorf("Output %v not equal to expected %v", i, test.ExpectedTotalBooks)
		}
	}
}

var contentCases = []Book{
	{Title: "we testing", Content: "some content"},
	{Title: "second testcase", Content: "weirddddddddddddddddddddddddddddd"},
}

func TestGetContentTitle(t *testing.T) {
	setupTestDB()
	for _, book := range contentCases {
		err := AddBook(book)
		if err != nil {
			panic(err)
		}
		title := book.Title
		expectedContent := book.Content
		if content := GetContentByTitle(title); content != expectedContent {
			t.Errorf("Output %v not equal to expected %v", content, expectedContent)
		}
	}
}
