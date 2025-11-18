package main

import "fmt"

type BankSecurity struct {
	MyBank Bank
}

func NewBankSecurity(bankRef Bank) BankSecurity {
	return BankSecurity{
		MyBank: bankRef,
	}
}

// Called every time a new customer arrives at the bank
func (s *BankSecurity) HandleNewCustomerArrival(newCustomer Customer) {
	fmt.Println("Customer arrived!")
	s.MyBank.GetCurrentClerks()[0].AssignCustomer(newCustomer)
	return
}

// If you've "greeted" a clerk, they will call this method when they are free to help another customer
func (s *BankSecurity) ReadyToHelpWhosNext(clerk Clerk) {
	fmt.Println("Clerk ready!")
	return
}
