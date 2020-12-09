package aoc

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

//Read lines from file
func LoadLines(filename string) []string {
	var results []string

	//open file and close at end of func
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	//read all lines
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		results = append(results, scanner.Text())
	}

	//check for error then return
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return results
}

//Read lines from file and convert them all to integers
func LoadIntList(filename string) []int {
	var results []int

	//open file and close at end of func
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	//use scanner to read each line and add ints to list
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		txt := scanner.Text()

		intval, err := strconv.Atoi(txt)
		if err != nil {
			log.Fatal(err)
		}

		results = append(results, intval)
	}

	//check for error then return
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return results
}
