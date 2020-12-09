package main

import (
	"fmt"
	"regexp"
	"strconv"

	"../aoc"
)

//password info loaded from file
type Password struct {
	Min    int
	Max    int
	Letter byte
	Text   string
}

//loads inputs line by line and uses reg ex to convert to array of Password structs
func loadmatches() []Password {
	var results []Password

	//load lines and build reg ex
	lines := aoc.LoadLines("../../day02input.txt")
	re := regexp.MustCompile(`(\d+)\-(\d+) (\w)\: (\w+)`)
	for _, line := range lines {

		//parse line and convert substrings
		var matches []string = re.FindStringSubmatch(line)
		min, _ := strconv.Atoi(matches[1])
		max, _ := strconv.Atoi(matches[2])
		letter := matches[3][0]
		text := matches[4]
		pw := Password{min, max, letter, text}

		//print
		//fmt.Printf("min=%d, max=%d, letter=%c, text=%s\n", pw.Min, pw.Max, pw.Letter, pw.Text)

		//append to results array
		results = append(results, pw)
	}

	return results
}

//challenge1 (min/max correspond to number of times letter can exist)
func challenge1() {
	validcount := 0
	passwords := loadmatches()

	for _, pw := range passwords {

		count := 0
		for _, char := range pw.Text {
			if byte(char) == pw.Letter {
				count++
			}
		}

		if count >= pw.Min && count <= pw.Max {
			validcount++
		}
	}

	fmt.Printf("Challenge 1 valid count: %d\n", validcount)
}

//challenge 2 (min/max are positions, exactly 1 at position must be letter)
func challenge2() {
	validcount := 0
	passwords := loadmatches()

	for _, pw := range passwords {

		firstchar := pw.Text[pw.Min-1]
		lastchar := pw.Text[pw.Max-1]

		firstmatch := firstchar == pw.Letter
		lastmatch := lastchar == pw.Letter

		if (firstmatch || lastmatch) && !(firstmatch && lastmatch) {
			validcount++
		}

	}

	fmt.Printf("Challenge 2 valid count: %d\n", validcount)
}

func main() {
	fmt.Printf("Running day02 test\n")
	challenge1()
	challenge2()
}
