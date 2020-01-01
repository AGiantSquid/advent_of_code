package main

import (
	"fmt"
	"strings"
	"strconv"
)

func main() {
	input := "168630-718098"

	total := getTotalValidPasswordCount(input)
	fmt.Println(total)
}

func getTotalValidPasswordCount(rangeString string) int {
	ranges := strings.Split(rangeString, "-")[:2]

	low, _ := strconv.Atoi(ranges[0])
	high, _ := strconv.Atoi(ranges[1])

	validPasswordCount := 0

	for i := low; i <= high; i++ {
		if validPassword(i) {
			validPasswordCount++
		}
	}

	return validPasswordCount
}

func validPassword(input int) bool {
	s := strconv.Itoa(input)
	twoAdjDigitsAreTheSame := false
	digitsIncrease := true

	var priorDigit rune

	for i, c := range(s) {
		if i > 0 {
			if c == priorDigit {
				twoAdjDigitsAreTheSame = true
			}
			if c < priorDigit {
				digitsIncrease = false
			}
		}
		priorDigit = c
	}

	return twoAdjDigitsAreTheSame && digitsIncrease
}