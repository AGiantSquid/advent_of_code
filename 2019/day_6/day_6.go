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
