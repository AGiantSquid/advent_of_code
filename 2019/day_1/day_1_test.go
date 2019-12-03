package main

import (
	"testing"
)

func TestGetRequiredFuelOne(t *testing.T) {
	mass := map[int]int{
		12:     2,
		14:     2,
		1969:   654,
		100756: 33583,
	}
	for k, v := range mass {
		res := getRequiredFuel(k)

		if res != v {
			t.Errorf("Error: Mass of %v should have produced a fuel value of %v", k, v)
		}
	}
}

func TestGetRequiredFuelTotal(t *testing.T) {
	masses := "test_data.txt"
	res := getRequiredFuelTotal(masses)

	if res != 34241 {
		t.Errorf("Error: Masses of %v should have produced a fuel value of %v", masses, res)
	}
}
