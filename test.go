package main

import "fmt"

var Arr []int{1,2,3,4,5}
var PtrArr []*int

func main() {
	for i, n := range Arr {
		PtrArr[i] = &n
	}
	fmt.Print(PtrArr)
}
