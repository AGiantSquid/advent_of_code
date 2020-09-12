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

	partOne := getRequiredFuelTotal(masses, getRequiredFuel)
	fmt.Print(partOne)

	partTwo := getRequiredFuelTotal(masses, getRequiredFuelCompounding)
	fmt.Println(partTwo)

	// Same thing as above, just with recursive strategy
	partTwoRecursive := getRequiredFuelTotal(masses, getRequiredFuelCompoundingRecursive)
	fmt.Println(partTwoRecursive)
}

// getRequiredFuelTotal accepts file location of module masses
// it reads the contents of the file and returns the
// total fuel required to launch them
func getRequiredFuelTotal(filePath string, fuelCalculationFunc func(int) int) int {
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
		result += fuelCalculationFunc(mass)
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

// getRequiredFuelCompounding calculates the required fuel to launch a module
// from its mass with fuel costs compounded
func getRequiredFuelCompounding(moduleMass int) int {
	valueIsPositive := true
	totalFuelNeeded := 0

	amountToCalculate := moduleMass

	for valueIsPositive {
		fuelNeeded := (amountToCalculate / 3) - 2
		if fuelNeeded < 0 {
			return totalFuelNeeded
		}
		totalFuelNeeded += fuelNeeded
		amountToCalculate = fuelNeeded
	}

	return totalFuelNeeded
}

// getRequiredFuelCompoundingRecursive calculates the required fuel to launch a module
// from its mass with fuel costs compounded, using recursive strategy
func getRequiredFuelCompoundingRecursive(mass int) (totalFuel int) {
	_, totalFuel = recursivelyGetRequiredFuel(mass, 0)
	return
}

func recursivelyGetRequiredFuel(moduleMass int, totalFuelNeeded int) (int, int) {
	fuelNeeded := (moduleMass / 3) - 2
	if fuelNeeded < 0 {
		return 0, totalFuelNeeded
	}

	return recursivelyGetRequiredFuel(fuelNeeded, totalFuelNeeded+fuelNeeded)
}
