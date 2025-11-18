package main

import "fmt"

// Load balancer!
// Goal: Leverage a collection/queue

// Request comes in
// It needs to be "processed" node
// Node exposes a process function to do this, but it take time to complete
//

//

// WorkRequest
// isCompleted? <- should only be able to be
// timeout <- Most used for checking if request are actually being completed

// TODO:
// * Port it all to python
// * Add some README and comment then share with Matt

func main() {
	fmt.Println("here we go")
	someBank := InitBank()
	theBank := someBank.(*bank)
	theBank.startSpawningCustomers(3)
}
