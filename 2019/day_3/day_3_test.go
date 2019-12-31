package main

import (
	"testing"
	// "fmt"
)

func TestDistanceOfNearestIntersection1(t *testing.T) {
	str := `R8,U5,L5,D3
U7,R6,D4,L4`
	result:= DistanceOfNearestIntersection(str)
	expected := 6
	if result!= expected {
		t.Errorf("Incorrect value observed! Expected %v but got %v", expected, result)
	}
}

func TestDistanceOfNearestIntersection2(t *testing.T) {
	str := `R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83`
	result:= DistanceOfNearestIntersection(str)
	expected := 159
	if result!= expected {
		t.Errorf("Incorrect value observed! Expected %v but got %v", expected, result)
	}
}

func TestDistanceOfNearestIntersection3(t *testing.T) {
	str := `R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7`
	result:= DistanceOfNearestIntersection(str)
	expected := 135
	if result!= expected {
		t.Errorf("Incorrect value observed! Expected %v but got %v", expected, result)
	}
}

