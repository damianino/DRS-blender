package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strconv"
	"strings"

	//"strings"
	"bytes"
	"io"
)

const (
	BUFFER_SIZE      = 4 * 1024
	BUFFER_SIZE_FILE = 16 * 1024
)

func main() {
	arguments := os.Args
	if len(arguments) == 1 {
		fmt.Println("Please provide a port number!")
		return
	}

	PORT := ":" + arguments[1] 
	l, err := net.Listen("tcp4", PORT)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer l.Close()

	for {
		c, err := l.Accept()
		if err != nil {
			fmt.Println(err)
			return
		}
		go handleConnection(c)

	}
}

// func NetCommandHandler(c net.Conn){
// 	for{

// 	}
// }

func handleConnection(c net.Conn) {
	fmt.Printf("Serving %s\n", c.RemoteAddr().String())
	
	LOOP:
	for {
		netData, err := bufio.NewReader(c).ReadString('\n')
		//buff, err := io.ReadAll(c) 
		if err != nil {
			fmt.Println(err)
			return
		}


		temp := strings.TrimSpace(netData)
		commands := strings.Split(temp, " ")
		fmt.Printf("[%s] %s\n", c.RemoteAddr(), temp)

		switch commands[0] {
		case "STOP":
			break LOOP

		case "FILE":
			size, err := strconv.ParseInt(commands[2], 10, 64)
			check(err)
			reciveFile(c, commands[1], size)
		}
	}

	c.Close()
}

func reciveFile(c net.Conn, filename string, size int64) {	
	f, err := os.Create(filename)
	check(err)
	defer f.Close()

	io.Copy(f, io.LimitReader(c, size))
}

func sendFile(c net.Conn, filename string) {	
	f, err := os.Open(filename)
	check(err)
	defer f.Close()

	info, err := os.Stat(filename)
	check(err)
	size := info.Size()
	str := strconv.FormatInt(size, 10)

	c.Write([]byte(str))
	io.Copy(c, f)
}

func reciveFile_(c net.Conn, filename string, size int64) {

	var currentByte int64 = 0
	
	
	f, err := os.Create(filename)
	check(err)
	defer f.Close()

	for currentByte < size {
		fileBuffer := make([]byte, BUFFER_SIZE_FILE)
		c.Read(fileBuffer)
		cleanedFileBuffer := bytes.Trim(fileBuffer, "\x00")
		_, err = f.WriteAt(cleanedFileBuffer, currentByte)
        if len(string(fileBuffer)) != len(string(cleanedFileBuffer)) {
            break
        }
        currentByte += BUFFER_SIZE_FILE
	}
	fmt.Printf("Done reciving file(EOF)\n")
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}
