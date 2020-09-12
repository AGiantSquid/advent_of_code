package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	filePath := "data.txt"
	result := processOrbitMap(filePath)
	fmt.Println(result) // 261306

	partTwo := navigateOrbitMap(filePath)
	fmt.Println(partTwo) // 382
}

func navigateOrbitMap(filePath string) int {
	orbitMap := readOrbitMap(filePath)
	orbitEdges := map[string][]string{}

	for k, v := range orbitMap {
		if _, ok := orbitMap[k]; ok {
			//do something here
			orbitEdges[k] = append(orbitEdges[k], v)
		} else {
			orbitEdges[k] = []string{v}
		}

		if _, ok := orbitMap[v]; ok {
			//do something here
			orbitEdges[v] = append(orbitEdges[v], k)
		} else {
			orbitEdges[v] = []string{k}
		}
	}

	orbitMoves := recursivelyCountNavigations(
		orbitEdges,
		orbitEdges["YOU"],
		orbitEdges["SAN"],
		[]string{"YOU"},
		[]string{"SAN"},
		0,
	)

	return orbitMoves
}

// recursivelyCountNavigations does a breath first search from each of the two element, taking turns for each element
// each element collects all the bordering elements, and compares them to the other elements neighbors
// once a common neigbor is found, the shortest route is satisfied.
func recursivelyCountNavigations(
	edgeMap map[string][]string,
	objectListOne []string,
	objectListTwo []string,
	seenObjectsOne []string,
	seenObjectsTwo []string,
	count int,
) int {
	commonElement := getCommonElement(objectListOne, objectListTwo)

	if commonElement != "" {
		return count
	}

	count++

	// alternate between each object, so only one object gets new neighboring objects each function call
	if count%2 != 0 {
		objectListOne, seenObjectsOne = getNextObjectList(edgeMap, objectListOne, seenObjectsOne)
	} else {
		objectListTwo, seenObjectsTwo = getNextObjectList(edgeMap, objectListTwo, seenObjectsTwo)
	}

	return recursivelyCountNavigations(edgeMap, objectListOne, objectListTwo, seenObjectsOne, seenObjectsTwo, count)
}

// getNextObjectList gets all the neighboring objects that have not already been seen
func getNextObjectList(edgeMap map[string][]string, objectList []string, seenObjects []string) ([]string, []string) {
	var nextNodes []string

	// add objects in objectList to seenObjects
	for _, el := range objectList {
		if !stringInSlice(el, seenObjects) {
			seenObjects = append(seenObjects, el)
		}
	}

	// add all neighbors of objects that have not already been seen to next nodes
	for _, key := range objectList {
		for _, el := range edgeMap[key] {
			if !stringInSlice(el, seenObjects) {
				nextNodes = append(nextNodes, el)
			}
		}
	}

	return nextNodes, seenObjects
}

func stringInSlice(a string, list []string) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}

	return false
}

func getCommonElement(one, two []string) string {
	for _, el := range one {
		for _, el2 := range two {
			if el == el2 {
				return el
			}
		}
	}

	return ""
}

// processOrbitMap reads an orbit map file and returns the number of orbits
func processOrbitMap(filePath string) int {
	orbitMap := readOrbitMap(filePath)

	runningTotal := 0
	for k := range orbitMap {
		runningTotal += recursivelyCountOrbits(orbitMap, k, 0)
	}

	return runningTotal
}

// read the input data line by line, and create a graph of the edges (orbits)
func readOrbitMap(filePath string) map[string]string {
	orbitMap := map[string]string{}

	file, err := os.Open(filePath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		orbitPairText := scanner.Text()
		orbitPair := strings.Split(orbitPairText, ")")
		orbitMap[orbitPair[1]] = orbitPair[0]
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return orbitMap
}

// recursivelyCountOrbits walks through the graph and counts the edges until "COM"
func recursivelyCountOrbits(orbitMap map[string]string, key string, runningTotal int) int {
	target := orbitMap[key]

	runningTotal++

	if target == "COM" {
		return runningTotal
	}

	return recursivelyCountOrbits(orbitMap, target, runningTotal)
}
