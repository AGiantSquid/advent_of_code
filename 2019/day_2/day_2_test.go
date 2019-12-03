package main

import (
	"testing"
)

func TestSolveIntCode(t *testing.T) {
	mass := [][][]int{
		[][]int{[]int{1, 0, 0, 0, 99}, []int{2, 0, 0, 0, 99}},
		[][]int{[]int{2, 3, 0, 3, 99}, []int{2, 3, 0, 6, 99}},
		[][]int{[]int{2, 4, 4, 5, 99, 0}, []int{2, 4, 4, 5, 99, 9801}},
		[][]int{[]int{1, 1, 1, 4, 99, 5, 6, 0, 99}, []int{30, 1, 1, 4, 2, 5, 6, 0, 99}},
	}
	for _, v := range mass {
		cachedStartingValues := v[0]
		solveIntCode(&v[0])

		if !Equal(v[0], v[1]) {
			t.Errorf("Error: IntCode of %v should have produced a result of %v. Expecting %v", v[0], v[1], cachedStartingValues)
		}
	}
}

// Equal tells whether a and b contain the same elements.
// A nil argument is equivalent to an empty slice.
func Equal(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i, v := range a {
		if v != b[i] {
			return false
		}
	}
	return true
}
