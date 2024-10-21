package api

import (
	"errors"
)

type NoTitleError struct {
}

func (e NoTitleError) New(message string) error {
	return errors.New("NoTitleError: " + message)
}

// Implement the Error() method for NoTitleError to satisfy the error interface.

type NoContentError struct {
}

func (e NoContentError) New(message string) error {
	return errors.New("NoContentError: " + message)
}
