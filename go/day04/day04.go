package main

import (
	"fmt"
	"strings"

	"../aoc"
)

/*
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
*/

type Passport struct {
	BirthYear      int
	IssueYear      int
	ExpirationYear int
	Height         int
	HairColor      int
	EyeColor       int
	PassportID     int
	CountryID      int
}

re := regexp.MustCompile(`(\w\w\w)`)

func addfield(passport *Passport, field string) {

}

func main() {
	fmt.Printf("Running day02 test\n")

	lines := aoc.LoadLines("../../day04input.txt")
	for _, line := range lines {
		fields := strings.Split(line, " ")
	}
}
