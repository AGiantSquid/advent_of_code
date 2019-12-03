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
	result := processIntCode("intcode_file.txt")
	fmt.Println(result)
}

// processIntCode reads a file and returns the updated code values
func processIntCode(filePath string) int {
	intCode := readIntCode(filePath)
	solvedIntCode := processIntCodeString(intCode)
	return solvedIntCode
}

func resetState(intCode *[]int) {
	(*intCode)[1] = 12
	(*intCode)[2] = 2
}

// formats the input from a string to ints to a string again
func processIntCodeString(intCodeString string) int {
	intCodeStringSlice := strings.Split(intCodeString, ",")
	intCodeSlice := convertStringSliceToIntSlice(intCodeStringSlice)
	resetState(&intCodeSlice)
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
