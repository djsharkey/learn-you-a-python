package main

import (
	"fmt"
	"math/rand"
	"time"
)

type CustomerMood string

const (
	Happy     CustomerMood = "happy"
	Fine      CustomerMood = "fine"
	Impatient CustomerMood = "impatient"
)

type Customer interface {
	StartHelping()
	FinishHelping()
	Mood() CustomerMood
	StillHere() bool
}

type customer struct {
	maxWaitTime int
	happy       bool
	beingHelped bool
	left        bool
}

func NewCustomer() Customer {
	randomSeconds := rand.Intn(4) + 5
	cust := &customer{
		maxWaitTime: randomSeconds,
	}
	go cust.leave()
	return cust
}

func (c *customer) StartHelping() {
	c.beingHelped = true
}

func (c *customer) FinishHelping() {
	if !c.beingHelped {
		return
	}
	c.happy = true
	c.left = true
	fmt.Println("A customer left happy!! :)")
}

func (c *customer) leave() {
	time.Sleep(time.Duration(c.maxWaitTime) * time.Second)
	if c.left == true || c.beingHelped {
		return
	}
	c.left = true
	fmt.Println("A customer left unhappy.... :(")
}

func (c *customer) Mood() CustomerMood {
	if c.happy {
		return Happy
	}
	return Fine
}

func (c *customer) StillHere() bool {
	return !c.left
}
