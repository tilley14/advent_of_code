// Advent of Code 2023, Day 1, Puzzle 1 & 2

package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"unicode"
)

func check(e error) {
	if e != nil {
		log.Fatal(e)
		panic(e)
	}
}

func part1(file io.Reader) int {
	scanner := bufio.NewScanner(file)
	sum := 0
	for scanner.Scan() {
		line := []rune(scanner.Text())
		first, last := "0", "0"
		size := len(line)
		i := 0
		for ; i < size; i++ {
			r := line[i]
			if unicode.IsNumber(r) {
				first = string(r)
				last = string(r)
				break
			}
		}
		for j := size - 1; j > i; j-- {
			r := line[j]
			if unicode.IsNumber(r) {
				last = string(r)
				break
			}
		}

		calStr := string(first) + string(last)
		cal, _ := strconv.Atoi(calStr)

		sum += cal
	}

	check(scanner.Err())

	return sum
}

func part2(file io.Reader) int {
	numbers := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	scanner := bufio.NewScanner(file)
	sum := 0

	// process files
	for scanner.Scan() {
		line := []rune(scanner.Text())
		first, last := "0", "0"
		size := len(line)
		i := 0
		ffound := false
		lfound := false
		for ; i < size; i++ {
			for k := range numbers {
				klen := len(k)
				if klen <= i+1 {
					lookBehind := string(line[i+1-klen : i+1])
					if lookBehind == k {
						first = numbers[k]
						last = numbers[k]
						ffound = true
						break
					}
				}
			}

			if ffound != true {
				r := line[i]
				if unicode.IsNumber(r) {
					first = string(r)
					last = string(r)
					ffound = true
				}
			}

			if ffound == true {
				break
			}
		}

		for j := size - 1; j >= i; j-- {
			for k := range numbers {
				klen := len(k)
				if klen <= size-j {
					lookBehind := string(line[j : j+klen])
					if lookBehind == k {
						last = numbers[k]
						lfound = true
						break
					}
				}
			}

			if lfound != true {
				r := line[j]
				if unicode.IsNumber(r) {
					last = string(r)
					lfound = true
				}
			}

			if lfound == true {
				break
			}
		}

		calStr := string(first) + string(last)
		cal, _ := strconv.Atoi(calStr)
		sum += cal
	}

	check(scanner.Err())

	return sum
}

func main() {
	t1()
	t2()
	solve()
}

func t1() {
	file, err := os.Open("test1.txt")

	check(err)
	defer file.Close()

	answer := 142
	if part1(file) == answer {
		fmt.Println("Part 1 Test: PASS")
	} else {
		fmt.Println("Part 1 Test: FAIL")
	}
}

func t2() {
	file, err := os.Open("test2.txt")

	check(err)
	defer file.Close()
	answer := 281
	if part2(file) == answer {
		fmt.Println("Part 2 Test: PASS")
	} else {
		fmt.Println("Part 2 Test: FAIL")
	}
}

func solve() {
	file, err := os.Open("input.txt")

	check(err)
	defer file.Close()

	// 55172
	fmt.Println("Part 1 Answer:", part1(file))
	file.Seek(0, 0)
	// 54925
	fmt.Println("Part 2 Answer:", part2(file))
}
