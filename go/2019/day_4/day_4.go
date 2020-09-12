package main

import (
	"fmt"
	"strings"
	"strconv"
)

func main() {
	input := "168630-718098"

	partOne := getTotalValidPasswordCount(input, validPassword1)
	fmt.Println(partOne)

	partTwo := getTotalValidPasswordCount(input, validPassword2)
	fmt.Println(partTwo)
}

type fn func(int) bool

func getTotalValidPasswordCount(rangeString string, validPassword fn) int {
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

func validPassword1(input int) bool {
	s := strconv.Itoa(input)
	twoAdjDigitsAreTheSame := false

	var priorDigit rune

	for i, c := range(s) {
		if i > 0 {
			if c == priorDigit {
				twoAdjDigitsAreTheSame = true
			}
			if c < priorDigit {
				return false
			}
		}
		priorDigit = c
	}

	return twoAdjDigitsAreTheSame
}

func validPassword2(input int) bool {
	s := strconv.Itoa(input)
	twoAdjDigitsFound := false
	twoAdjDigitsAreTheSame := false

	var priorDigit rune
	adjDigit := '0'

	for i, c := range(s) {
		if i > 0 {
			if c == priorDigit {
				// this will happen with 3 or more in a row
				if c == adjDigit {
					twoAdjDigitsAreTheSame = false
				}
				if c != adjDigit {
					twoAdjDigitsAreTheSame = true
					adjDigit = c
				}
			}
			if c != priorDigit && twoAdjDigitsAreTheSame {
				twoAdjDigitsFound = true
			}
			if c != priorDigit {
				// reset adjDigit
				adjDigit = '0'
			}

			if c < priorDigit {
				return false
			}
		}
		priorDigit = c
	}

	if twoAdjDigitsFound || twoAdjDigitsAreTheSame {
		return true
	}

	return false
}
