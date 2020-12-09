package main

import (
	"fmt"

	"../aoc"
)

func main() {
	fmt.Printf("Running day01 test\n")

	//load integer values
	values := aoc.LoadIntList("../../day01input.txt")

	//look for pairs that sum to 2020
	for idx0 := 0; idx0 < len(values); idx0++ {
		for idx1 := idx0 + 1; idx1 < len(values); idx1++ {
			val0 := values[idx0]
			val1 := values[idx1]
			if (val0 + val1) == 2020 {
				fmt.Printf("%d\n", val0*val1)
			}
		}
	}

	//look for tuples that sum to 2020
	for idx0 := 0; idx0 < len(values); idx0++ {
		for idx1 := idx0 + 1; idx1 < len(values); idx1++ {
			for idx2 := idx1 + 1; idx2 < len(values); idx2++ {
				val0 := values[idx0]
				val1 := values[idx1]
				val2 := values[idx2]
				if (val0 + val1 + val2) == 2020 {
					fmt.Printf("%d\n", val0*val1*val2)
				}
			}
		}
	}

}
