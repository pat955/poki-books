package api

import "fmt"

// NoTitleError is a custom error type for missing title errors.
type NoTitleError struct {
	Message string
}

// Implement the Error() method for NoTitleError to satisfy the error interface.
func (e *NoTitleError) Error() string {
	return fmt.Sprintf("NoTitleError: %s", e.Message)
}

// NoContentError is a custom error type for missing content errors.
type NoContentError struct {
	Message string
}

// Implement the Error() method for NoContentError to satisfy the error interface.
func (e *NoContentError) Error() string {
	return fmt.Sprintf("NoContentError: %s", e.Message)
}
