package main

import (
	"testing"
)

func TestProcessOrbitMap(t *testing.T) {
	filePath := "test_data.txt"
	result := processOrbitMap(filePath)
	expectedResult := 42

	if result != expectedResult {
		t.Errorf("Error: processOrbitMap should have produced a result of %v. Observed %v", expectedResult, result)
	}
}

func TestProcessOrbitMapRealData(t *testing.T) {
	filePath := "data.txt"
	result := processOrbitMap(filePath)
	expectedResult := 261306

	if result != expectedResult {
		t.Errorf("Error: processOrbitMap should have produced a result of %v. Observed %v", expectedResult, result)
	}
}

func TestNavigateOrbitMap(t *testing.T) {
	filePath := "test_data_2.txt"
	result := navigateOrbitMap(filePath)
	expectedResult := 4

	if result != expectedResult {
		t.Errorf("Error: processOrbitMap should have produced a result of %v. Observed %v", expectedResult, result)
	}
}

func TestNavigateOrbitMapRealData(t *testing.T) {
	filePath := "data.txt"
	result := navigateOrbitMap(filePath)
	expectedResult := 382

	if result != expectedResult {
		t.Errorf("Error: processOrbitMap should have produced a result of %v. Observed %v", expectedResult, result)
	}
}
