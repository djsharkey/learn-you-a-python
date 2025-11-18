package main

import (
	"fmt"
	"time"
)

const (
	MAX_CLERKS_FOR_BRANCH = 10
)

type Bank interface {
	GetCurrentClerks() []Clerk
	OpenNewClerkDesk() (Clerk, bool)
	DismissClerk(clerk Clerk) bool
}

type bank struct {
	activeClerks []Clerk
	allCustomers []Customer
	security     *BankSecurity
	hiredClerks  int
}

func InitBank() Bank {
	bank := &bank{}
	security := NewBankSecurity(bank)
	bank.security = &security

	newClerk, _ := bank.OpenNewClerkDesk()
	newClerk.Greet(&security)
	return bank
}

func (b *bank) GetCurrentClerks() []Clerk {
	return b.activeClerks
}

func (b *bank) OpenNewClerkDesk() (Clerk, bool) {
	if len(b.activeClerks) >= MAX_CLERKS_FOR_BRANCH {
		return nil, false
	}
	newClerk := NewClerk()
	b.hiredClerks++
	b.activeClerks = append(b.activeClerks, newClerk)
	return newClerk, true
}

func (b *bank) DismissClerk(clerk Clerk) bool {
	if clerk != nil {
		clerk.Dismiss()
		updatedClerks := []Clerk{}
		for _, c := range b.activeClerks {
			if c != clerk {
				updatedClerks = append(updatedClerks, c)
			}
		}
		b.activeClerks = updatedClerks
		return true
	}
	return false
}

func (b *bank) startSpawningCustomers(amount int) {
	fmt.Println("The bank is open!")
	for i := 0; i < amount; i++ {
		fmt.Println("A new customer just arrived")
		cust := NewCustomer()
		b.allCustomers = append(b.allCustomers, cust)
		b.security.HandleNewCustomerArrival(cust)

		// Wait some amount of time (TODO: make it somewhat random)
		time.Sleep(time.Duration(1) * time.Second)
	}

	fmt.Println("The bank is closing~ Waiting for final customer(s) to leave")
	for !b.checkIfAllCustomersDone() {
		fmt.Println("waiting...")
		time.Sleep(time.Duration(1) * time.Second)
	}
	fmt.Println("The bank is closed!")

	happyCustomers := 0
	for _, cus := range b.allCustomers {
		if cus.Mood() == Happy {
			happyCustomers++
		}
	}
	if happyCustomers == amount {
		fmt.Println("Good job handling all customers before they got too upset")
	} else {
		fmt.Printf("Of %d total customers, %d left unhappy. Try improving your clerk assigment some!\n", amount, amount-happyCustomers)
	}
	fmt.Printf("During operating hours you had %d clerks working and ended the day with %d still active\n", b.hiredClerks, len(b.activeClerks))

}

func (b *bank) checkIfAllCustomersDone() bool {
	for _, cus := range b.allCustomers {
		if cus.StillHere() {
			return false
		}
	}
	return true
}
