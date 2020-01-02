package main

import (
	"testing"
)

func TestGetTotalValidPasswordCount(t *testing.T) {
	testString := "118-121"

	result := getTotalValidPasswordCount(testString, validPassword1)
	expected := 2 // 118, 119

	if result != expected {
		t.Errorf("Incorrect value observed! Expected %v but got %v", expected, result)
	}
}

func TestGetTotalValidPasswordCount2(t *testing.T) {
	testString := "1118-1122"

	result := getTotalValidPasswordCount(testString, validPassword2)
	expected := 1 // 1122

	if result != expected {
		t.Errorf("Incorrect value observed! Expected %v but got %v", expected, result)
	}
}


func TestGetTotalValidPasswordCount2b(t *testing.T) {
	testString := "11120-11223"

	result := getTotalValidPasswordCount(testString, validPassword2)
	expected := 10
	// 11122
	// 11133
	// 11144
	// 11155
	// 11166
	// 11177
	// 11188
	// 11199
	// 11222
	// 11223

	if result != expected {
		t.Errorf("Incorrect value observed! Expected %v but got %v", expected, result)
	}
}

func TestValidPassword2Count(t *testing.T) {
	testInt := 348888

	result := validPassword2(testInt)
	expected := false

	if result != expected {
		t.Errorf("Incorrect value observed! Expected %v but got %v", expected, result)
	}
}


func TestValidPassword2Countb(t *testing.T) {
	testInt := 333344

	result := validPassword2(testInt)
	expected := true

	if result != expected {
		t.Errorf("Incorrect value observed! Expected %v but got %v", expected, result)
	}
}

func TestValidPassword2Countc(t *testing.T) {
	testInt := 3333444

	result := validPassword2(testInt)
	expected := false

	if result != expected {
		t.Errorf("Incorrect value observed! Expected %v but got %v", expected, result)
	}
}

func TestValidPassword2Countd(t *testing.T) {
	testInt := 223334

	result := validPassword2(testInt)
	expected := true

	if result != expected {
		t.Errorf("Incorrect value observed! Expected %v but got %v", expected, result)
	}
}