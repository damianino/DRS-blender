package utils

import (
	"log"
	"math/rand"
	"time"
)

var letters = []rune("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

func RandSeq(n int) string {
	rand.Seed(time.Now().UnixNano())
	b := make([]rune, n)
	for i := range b {
		b[i] = letters[rand.Intn(len(letters))]
	}
	return string(b)
}

func Check(err error, msg string) {
	if err != nil {
		log.Fatalf("%s: %s", msg, err)
	}
}
