package main

import (
	"math/rand"
	"time"
)

type Clerk interface {
	Greet(sec *BankSecurity) bool
	AssignCustomer(cus Customer) bool
	IsFree() bool
	Dismiss()
}

func NewClerk() Clerk {
	return &clerk{}
}

type clerk struct {
	assignedCustomer Customer
	security         *BankSecurity
	isWorking        bool
	isDismissed      bool
}

// AssignCustomer attempts to assign a new customer to the Clerk, returns bool based on success
func (c *clerk) AssignCustomer(cus Customer) bool {
	if c.isDismissed || c.assignedCustomer != nil {
		return false
	}
	c.assignedCustomer = cus
	go c.handleAssignedCustomer()
	return true
}

func (c *clerk) Greet(sec *BankSecurity) bool {
	if c.isDismissed {
		return false
	}
	c.security = sec
	return true
}

func (c *clerk) IsFree() bool {
	if c.isDismissed {
		return false
	}
	return c.assignedCustomer == nil
}

func (c *clerk) Dismiss() {
	c.isDismissed = true
}

func (c *clerk) handleAssignedCustomer() {
	if c.assignedCustomer == nil {
		return
	}
	c.isWorking = true
	c.assignedCustomer.StartHelping()

	randomSeconds := rand.Intn(4) + 1
	time.Sleep(time.Duration(randomSeconds) * time.Second)

	c.assignedCustomer.FinishHelping()

	c.assignedCustomer = nil
	c.isWorking = false
	if c.security != nil {
		c.security.ReadyToHelpWhosNext(c)
	}
}
