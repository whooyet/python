package dict

import (
	"errors"
)

type Dictionary map[string]string

var (
	errDamit = errors.New("오우 마이갓!! 뎀잇!!!!!")
	errCantUp = errors.New("업뎃불능")
	errYes = errors.New("그 단어는 있어 ㅇㅇ")
	)

func (d Dictionary) Search(word string) (string, error) {
	value, exists := d[word]
	if exists {
		return value, nil
	}
	return "", errDamit
}
func (d Dictionary) Add(word, def string) error {
	_, err := d.Search(word)

	switch err {
	case errDamit:
		d[word] = def
	case nil:
		return errYes
	}
	return nil
}

func (d Dictionary) Update(word, def string) error{
	_, err := d.Search(word)
	switch err {
	case nil:
		d[word] = def
	case errDamit:
		return errCantUp
	}
	return nil
}