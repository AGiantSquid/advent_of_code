package main

import (
	"testing"
)

func TestGetTotalValidPasswordCount(t *testing.T) {
	testString := "118-121"

	result := getTotalValidPasswordCount(testString)
	expected := 2 // 118, 119

	if result != expected {
		t.Errorf("Incorrect value observed! Expected %v but got %v", expected, result)
	}
}