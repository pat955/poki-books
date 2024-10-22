// run ./scripts/test.sh for actual testing, it creates and resets the test database
package api

import (
	"testing"
)

// Constant of test database
var DB_PATH_TEST string = "../sql/test.db"

// Testcase struct
type Case struct {
	Nr                 int
	Book               Book
	ExpectedErr        bool
	ExpectedTotalBooks int
}

var addBookCases = []Case{
	{1, Book{Path: "books/some_book.pdf", Content: "contnetmte t,t estestetm tetet, yeah."}, false, 1},
	{2, Book{Path: "books/now_thats_a_book.txt", Content: "something something"}, false, 2},
	{3, Book{Path: ""}, true, 2}, // NoPathError
}

// Testing AddBook function, checks if the book is actually added into the db or if the expected error is presented.
func TestAddBook(t *testing.T) {
	for _, test := range addBookCases {
		if err := AddBook(DB_PATH_TEST, test.Book); (err != nil) != test.ExpectedErr {
			t.Errorf("Case nr.%v | Output %v, error expected: %v", test.Nr, err, test.ExpectedErr)
		}
		books, err := GetAllBooks(DB_PATH_TEST)
		if (err != nil) != test.ExpectedErr {
			t.Errorf("Case nr.%v | Output %v, error expected: %v", test.Nr, err, test.ExpectedErr)
		}
		i := len(books)
		if i != test.ExpectedTotalBooks {
			t.Errorf("Case nr.%v | Output %v not equal to expected %v", test.Nr, i, test.ExpectedTotalBooks)
		}
	}
}

var getContentCases = []Case{
	{1, Book{Path: "books/we_testing", Title: "we testing", Content: "some content"}, false, 0}, // expected int is not used!
	{2, Book{Path: "books/second_testcase", Title: "second testcase", Content: "weirddddddddddddddddddddddddddddd"}, false, 0},
}

// Testing GetContentTitle function, adds book to db then gets content with title.
func TestGetContentTitle(t *testing.T) {
	for _, test := range getContentCases {
		err := AddBook(DB_PATH_TEST, test.Book)
		if (err != nil) != test.ExpectedErr {
			t.Errorf("Case nr.%v | Output %v, error expected: %v", test.Nr, err, test.ExpectedErr)
		}
		title := test.Book.Title
		expectedContent := test.Book.Content
		content, err := GetContentByTitle(DB_PATH_TEST, title)

		if (err != nil) != test.ExpectedErr {
			t.Errorf("Case nr.%v | Output %v, error expected: %v", test.Nr, err, test.ExpectedErr)

		}
		if content != expectedContent {
			t.Errorf("Case nr.%v | Output %v not equal to expected %v", test.Nr, content, expectedContent)
		}
	}
}
