// Advent of Code 2023, Day 2, Puzzle 1 & 2
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		log.Fatal(e)
		panic(e)
	}
}

func ParseInt(str string, trim string) int {
	id, err := strconv.Atoi(strings.Trim(str, trim))
	check(err)
	return id
}

func p1(fname string, r int, g int, b int) int {
	f, err := os.Open(fname)
	check(err)
	defer f.Close()

	scanner := bufio.NewScanner(f)
	sum := 0

	for scanner.Scan() {
		line := scanner.Text()
		set := strings.Split(line, ":")
		id := ParseInt(set[0], "Game ")
		games := strings.Split(set[1], "; ")

		valid := true
		for _, game := range games {
			gr := 0
			gb := 0
			gg := 0

			turns := strings.Split(game, ", ")

			for _, turn := range turns {
				if strings.Contains(turn, "red") {
					gr = ParseInt(turn, " red")
				}
				if strings.Contains(turn, "blue") {
					gb = ParseInt(turn, " blue")
				}
				if strings.Contains(turn, "green") {
					gg = ParseInt(turn, " green")
				}
			}

			valid = gr <= r && gb <= b && gg <= g

			if valid != true {
				break
			}
		}

		if valid {
			sum += id
		}
	}

	return sum
}

func p2(fname string) int {
	f, err := os.Open(fname)
	check(err)
	defer f.Close()

	scanner := bufio.NewScanner(f)
	sum := 0

	for scanner.Scan() {
		line := scanner.Text()
		set := strings.Split(line, ":")
		games := strings.Split(set[1], "; ")

		rmax := 0
		bmax := 0
		gmax := 0

		for _, game := range games {

			turns := strings.Split(game, ", ")

			for _, turn := range turns {
				if strings.Contains(turn, "red") {
					r := ParseInt(turn, " red")
					if r >= rmax {
						rmax = r
					}
				}
				if strings.Contains(turn, "blue") {
					b := ParseInt(turn, " blue")
					if b >= bmax {
						bmax = b
					}

				}
				if strings.Contains(turn, "green") {
					g := ParseInt(turn, " green")
					if g >= gmax {
						gmax = g
					}
				}
			}
		}

		if rmax == 0 || bmax == 0 || gmax == 0 {
			panic(0)
		}

		sum += (rmax * bmax * gmax)
	}

	return sum
}

func main() {
	if p1("test1.txt", 12, 13, 14) == 8 {
		fmt.Println("Test 1: Pass")
	} else {
		fmt.Println("Test 1: Fail")
	}

	if p2("test2.txt") == 2286 {
		fmt.Println("Test 2: Pass")
	} else {
		fmt.Println("Test 2: Fail")
	}

	// 2406
	fmt.Println("The answer to Part 1 is", p1("input.txt", 12, 13, 14))

	// 78375
	fmt.Println("The answer to Part 2 is", p2("input.txt"))
}
