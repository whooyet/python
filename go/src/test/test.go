package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

func RandomString(ss string) string {
	check := strings.Contains(ss, "!단어")
	if check {
		bb := strings.Replace(ss, "!단어 ", "", 1)
		s := strings.Split(bb, " ")

		rand.Seed(time.Now().UnixNano())
		randIdx := rand.Intn(len(s))
		return s[randIdx]
	}
	return "d"
}


func main() { // 영어 암기 봇 만들기 전 테스트 할 것
	a := "!단어 monkey bus apple fun good resibk yache naver channel message"

	ticker := time.NewTicker(time.Millisecond * 500)

	i := 1
	for range ticker.C {
		if i < 10 {

			random := RandomString(a)
			fmt.Println(random)
			i += 1
		} else {
			ticker.Stop()
			break
		}
	}
}
