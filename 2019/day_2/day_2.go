package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	filePath := "intcode_file.txt"
	result := processIntCode(filePath, 12, 2)
	fmt.Println(result)

	partTwo := bruteForce(filePath)
	fmt.Println(partTwo)
}

func bruteForce(filePath string) int {
	intCode := readIntCode(filePath)
	for i := 0; i < 99; i++ {
		for j := 0; j < 99; j++ {
			result := processIntCodeString(intCode, i, j)
			if result == 19690720 {
				return i*100 + j
			}
		}
	}
	return 0
}

// processIntCode reads a file and returns the updated code values
func processIntCode(filePath string, noun int, verb int) int {
	intCode := readIntCode(filePath)
	solvedIntCode := processIntCodeString(intCode, noun, verb)
	return solvedIntCode
}

func resetState(intCode *[]int, noun int, verb int) {
	(*intCode)[1] = noun
	(*intCode)[2] = verb
}

// formats the input from a string to ints to a string again
func processIntCodeString(intCodeString string, noun int, verb int) int {
	intCodeStringSlice := strings.Split(intCodeString, ",")
	intCodeSlice := convertStringSliceToIntSlice(intCodeStringSlice)
	resetState(&intCodeSlice, noun, verb)
	solveIntCode(&intCodeSlice)
	return intCodeSlice[0]
}

// solveIntCode contains the intCode business logic for solving the puzzle
func solveIntCode(intCode *[]int) {
	for i, val := range *intCode {
		if i%4 == 0 && val == 99 {
			return
		}
		if i%4 != 0 {
			continue
		}
		valOne := (*intCode)[i+1]
		valTwo := (*intCode)[i+2]
		target := (*intCode)[i+3]
		if val == 1 {
			(*intCode)[target] = (*intCode)[valOne] + (*intCode)[valTwo]
		}
		if val == 2 {
			(*intCode)[target] = (*intCode)[valOne] * (*intCode)[valTwo]
		}
	}
}

func convertStringSliceToIntSlice(stringSlice []string) (result []int) {
	for _, str := range stringSlice {
		convertedInt, err := strconv.Atoi(str)
		if err != nil {
			panic(err)
		}
		result = append(result, convertedInt)
	}
	return
}

func convertIntSliceToStringSlice(intSlice []int) (result []string) {
	for _, i := range intSlice {
		convertedString := strconv.Itoa(i)
		result = append(result, convertedString)
	}
	return
}

func readIntCode(filePath string) string {
	intCode := ""

	file, err := os.Open(filePath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		intCode = scanner.Text()
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return intCode
}
