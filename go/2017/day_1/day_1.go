package main

import "fmt"
import "strconv"

func main() {
        integerSequence := 1122
        var res int
        res = captchaSequenceSolver(integerSequence)
        fmt.Printf("%v", res)
}

func captchaSequenceSolver(integerSequence int) int {
        stringified := strconv.Itoa(integerSequence)
        firstChar := string(stringified[0])
        extended := stringified + firstChar

        var priorEl int
        var sumOfSequences int
        for i := 0; i < len(extended); i++ {
                el, _ := strconv.Atoi(string(extended[i]))
                if el == priorEl {
                        sumOfSequences += el
                }
                priorEl = el
        }
        return sumOfSequences

}
