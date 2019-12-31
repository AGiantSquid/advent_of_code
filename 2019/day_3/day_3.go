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

	partTwo := DistanceOfFirstIntersection(testString)
	fmt.Println(partTwo)
}

type Coords struct {
	X int
	Y int
}

func (c *Coords) mahattanDistance() int {
	return Abs(c.X) + Abs(c.Y)
}

type IndexedCoords map [int]Coords

type OverlappingCoordsWithIndexes struct {
	Distance int
	OverlappingCoords Coords
}


func DistanceOfNearestIntersection (instructionsString string) int {
	overlaps := getOverlappingCoordsForTwoWires(instructionsString)

	closestOverlapManhattanDistance := overlaps[0].OverlappingCoords.mahattanDistance()

	for _, overlap := range overlaps {
		currentCoordsManhattanDistance := overlap.OverlappingCoords.mahattanDistance()
		if currentCoordsManhattanDistance < closestOverlapManhattanDistance  {
			closestOverlapManhattanDistance = currentCoordsManhattanDistance
		}
	}

	return closestOverlapManhattanDistance
}

func DistanceOfFirstIntersection(instructionsString string) int {
	overlaps := getOverlappingCoordsForTwoWires(instructionsString)

	minManhattanDistance := overlaps[0].Distance

	for _, el := range overlaps {
		if el.Distance < minManhattanDistance {
			minManhattanDistance = el.Distance
		}
	}

	return minManhattanDistance
}

func getOverlappingCoordsForTwoWires(instructionsString string) []OverlappingCoordsWithIndexes {
	// first line is wire one instructions, second line is wire two instructions
	instructionsSlice := strings.Split(instructionsString, "\n")[:2]

	wireOneCoords := getTraversedCoordsWithIndex(instructionsSlice[0])
	wireTwoCoords := getTraversedCoordsWithIndex(instructionsSlice[1])

	overlaps := getOverlappingCoordsWithDistance(wireOneCoords, wireTwoCoords)

	return overlaps
}

// Convert string of comma separated instructions into list of coordinates with distance travelled
// instructions comes in the form of a letter, then a number, eg. "R8,U5,L5,D3"
func getTraversedCoordsWithIndex(instructionString string) IndexedCoords {
	s := strings.Split(instructionString, ",")

	cursorCoords := Coords{0,0}
	resultCoords := IndexedCoords{}
	runningTotal := 0

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
			runningTotal++
			resultCoords[runningTotal] = cursorCoords
		}
	}

	return resultCoords
}

// return all the coordinates that are overlapping
func getOverlappingCoordsWithDistance(one, two IndexedCoords) []OverlappingCoordsWithIndexes {
	var overlappingCoords []OverlappingCoordsWithIndexes

	for i, coords1 := range one {
		for j, coords2 := range two {
			if coords1 == coords2 {
				intersection := OverlappingCoordsWithIndexes{
					i + j,
					coords1,
				}
				overlappingCoords = append(overlappingCoords, intersection)
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