package main

import (
	"log"
	"syscall"

)

func main() {
	err := syscall.Kill(427271, syscall.SIGKILL)
	log.Print(err)


}
