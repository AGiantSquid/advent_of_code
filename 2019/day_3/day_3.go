package main

import (
	"fmt"
	"strings"
	"strconv"
	"io/ioutil"
	"log"
)

func main () {
	filePath := "test.txt"
	testString := readData(filePath)
	partOne := DistanceOfNearestIntersection(testString)
	fmt.Println(partOne)
}

type Coords struct {
	X int
	Y int
}

func (c *Coords) mahattanDistance() int {
	return Abs(c.X) + Abs(c.Y)
}


func DistanceOfNearestIntersection (instructionsString string) int {
	// first line is wire one instructions, second line is wire two instructions
	instructionsSlice := strings.Split(instructionsString, "\n")[:2]

	wireOneCoords := getTraversedCoords(instructionsSlice[0])
	wireTwoCoords := getTraversedCoords(instructionsSlice[1])

	overlaps := getOverlappingCoords(wireOneCoords, wireTwoCoords)

	closestOverlap := overlaps[0]

	for _, overlap := range overlaps {
		if closestOverlap.mahattanDistance() > overlap.mahattanDistance() {
			closestOverlap = overlap
		}
	}

	result := closestOverlap.mahattanDistance()

	return result
}

// Convert string of comma separated instructions into list of coordinates
// instructions comes in the form of a letter, then a number, eg. "R8,U5,L5,D3"
func getTraversedCoords(instructionString string) []Coords {
	s := strings.Split(instructionString, ",")
	// cursor holds the last known position of our wire
	cursorCoords := Coords{0,0}

	var resultCoords []Coords

	for _, instruction := range s {
		direction := instruction[:1]
		amount, _ := strconv.Atoi(instruction[1:])
		for i := 0; i < amount; i++ {
			if direction == "R" {
				cursorCoords.X++
			}
			if direction == "U" {
				cursorCoords.Y++
			}
			if direction == "L" {
				cursorCoords.X--
			}
			if direction == "D" {
				cursorCoords.Y--
			}
			resultCoords = append(resultCoords, cursorCoords)
		}
	}

	return resultCoords

}

// return all the coordinates that are overlapping
func getOverlappingCoords(one, two []Coords) []Coords {
	var overlappingCoords []Coords

	for _, coords1 := range one {
		for _, coords2 := range two {
			if coords1 == coords2 {
				overlappingCoords = append(overlappingCoords, coords1)
			}
		}
	}

	return overlappingCoords
}



// Abs returns the absolute value of x.
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// Read all the contents of a file
func readData(filePath string) string {
	data, err := ioutil.ReadFile(filePath)
	if err != nil {
		log.Fatal(err)
	}
	return string(data)
}