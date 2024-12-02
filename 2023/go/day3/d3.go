// Advent of Code 2023, Day 3, Puzzle 1 & 2
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"unicode"
)

func check(e error) {
	if e != nil {
		log.Fatal(e)
		panic(e)
	}
}

func ParseLine(line string) []string {
	lineView := make([]string, 0)

	// token builder
	lineTokens := []rune(line)

	eot := true
	ct := make([]rune, 0)
	for _, r := range lineTokens {
		if unicode.IsNumber(r) {
			eot = false
			ct = append(ct, r)

		} else {
			if eot == false {
				// add complex token
				lineView = append(lineView, string(ct))
				ct = nil // is this an empty slice
				eot = true
			}

			lineView = append(lineView, string(r))
		}
	}

	if eot == false {
		lineView = append(lineView, string(ct))
	}

	return lineView
}

func p1(fname string) int {
	ret := 0

	f, e := os.Open(fname)
	check(e)

	scanner := bufio.NewScanner(f)

	first := true
	view := make([][]string, 3)

	for scanner.Scan() {
		line := scanner.Text()

		if first {

		} else {

		}

	}
	// Handle last

	return ret
}

func p2(fname string) int {
	ret := 0

	return ret
}

func main() {
	if p1("test1.txt") == 4361 {
		fmt.Println("Test 1: Pass")
	} else {
		fmt.Println("Test 1: Fail")
	}

	if p2("test2.txt") == 1 {
		fmt.Println("Test 2: Pass")
	} else {
		fmt.Println("Test 2: Fail")
	}

	// fmt.Println("The answer to Part 1 is", p1("input.txt"))
	// fmt.Println("The answer to Part 2 is", p2("input.txt"))
}
