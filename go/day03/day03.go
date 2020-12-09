package main

import (
	"fmt"

	"../aoc"
)

func main() {
	fmt.Printf("Running day02 test\n")

	var lines []string = aoc.LoadLines("../../day03input.txt")

	var treegrid [][]bool
	for _, line := range lines {
		var treeline []bool
		for _, character := range line {
			treeline = append(treeline, character == '#')
		}
		treegrid = append(treegrid, treeline)
	}

	var steps = [][]int{
		{1, 1},
		{3, 1},
		{5, 1},
		{7, 1},
		{1, 2},
	}
	fmt.Printf("%d\n", len(steps))

	total := 1
	for _, step := range steps {
		var x int = 0
		var y int = 0
		var treecount int = 0

		for y < len(treegrid) {
			var treeline []bool = treegrid[y]
			var istree bool = treeline[x%len(treeline)]
			if istree {
				treecount++
			}
			x += step[0]
			y += step[1]
		}
		total *= treecount
		fmt.Printf("%d\n", treecount)
	}
	fmt.Printf("%d\n", total)

}
