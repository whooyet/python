package main

import (
	"fmt"
	"test/dict"
)

func main() {
	dictionary := dict.Dictionary{"first":"First word"}
	beaseWord := "미로"

	dictionary.Add(beaseWord, "First")

	err := dictionary.Update(beaseWord, "Second")
	if err != nil {
		fmt.Println(err)
	}
	word, _ := dictionary.Search(beaseWord)
	fmt.Println(word)
}