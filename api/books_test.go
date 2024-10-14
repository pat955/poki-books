package api

import (
	"testing"
)

type Case struct {
	Title              string
	ExpectedErr        error
	ExpectedTotalBooks int
}

var TotalBooksNow int = len(GetAllBooks())

var addTests = []Case{
	Case{"Title", nil, TotalBooksNow + 1},
	Case{"ANOTHER TITLE", nil, TotalBooksNow + 2},
	Case{"", NoTitleError{}, TotalBooksNow + 2},
}

func TestAddBook(t *testing.T) {
	for _, test := range addTests {
		if err := AddBook(test.Title); err != test.ExpectedErr {
			t.Errorf("Output %v not equal to expected %v", err, test.ExpectedErr)
		}
		if i := len(GetAllBooks()); i != test.ExpectedTotalBooks {
			t.Errorf("Output %v not equal to expected %v", i, test.ExpectedTotalBooks)
		}
	}
}
