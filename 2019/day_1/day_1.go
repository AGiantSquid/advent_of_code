package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	masses := "masses.txt"

	result := getRequiredFuelTotal(masses)
	fmt.Print(result)
}

// getRequiredFuelTotal accepts file location of module masses
// it reads the contents of the file and returns the
// total fuel required to launch them
func getRequiredFuelTotal(filePath string) int {
	result := 0

	file, err := os.Open(filePath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		mass, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		result += getRequiredFuel(mass)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return result
}

// getRequiredFuel calculates the required fuel to launch a module from its mass
func getRequiredFuel(mass int) int {
	// divide by 3, round down, subtract 2
	// since we use ints, we already have a rounded down number
	return (mass / 3) - 2
}
