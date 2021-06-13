package main

import (
	"log"
	"syscall"
)

func main() {

	err := syscall.Kill(9999, syscall.SIGKILL)
	log.Print(err)

}
