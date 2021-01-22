package main

import (
	"errors"
	"fmt"
)

type UserProfile map[string]string

var (
	errSearch = errors.New("검색 결과: 없습니다.")
	errCantUp = errors.New("업뎃불능")
)

func (d UserProfile) Update(word, def string) error {
	_, err := d.Search(word) // 첫번째 인자를 검색
	switch err {
	case nil: // 리턴된 nil 그러니까 검색결과 있다면 채워넣기
		d[word] = def // map 안에 값을 집어넣음
	case errSearch:
		return errCantUp
	}
	return nil
}

func (d UserProfile) Search(word string) (string, error) {
	value, exists := d[word]
	if exists { // 만약에 두번째 인자값이 있다면
		return value, nil // value 또는 nil로 리턴
	}
	return "", errSearch
}

func iu(a string, b int) {
	u_name := "이름"
	u_age := "나이"
	u_game := "게임"

	u := UserProfile{u_name: "x", u_age: "x", u_game: "x"}

	switch b {
	case 1:
		err := u.Update(u_name, a)
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println("이름:", a)
	case 2:
		err := u.Update(u_age, a)
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println("나이:", a)
	case 3:
		err := u.Update(u_game, a)
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println("게임:", a)
	}
}

func main() {

	var a, b, c string

	fmt.Println("이름, 나이, 게임 순으로 적으세요")
	fmt.Println("ex) fucca치고 엔터 15 치고 엔터")
	fmt.Scan(&a, &b, &c)
	iu(a, 1)
	iu(b, 2)
	iu(c, 3)

}