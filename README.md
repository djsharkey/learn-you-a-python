# Learning python with Matt and Dill

## Project 1: The bank simulator!
The goal of this project is to take a predefined interface and implement it to serve a "real world" need. We need to operate a bank that handles customers coming in at random times and try to get them assigned to a clerk in a timely fashion


NOTE: In this project there is a bit of functionality already created, but its all nested under the "core" directory
**Its highly encouraged to just use the readme and avoid looking at the code under core unless you really get stuck**
(Though of course feel free to look afterwards if curious)

**You should only need to edit code in projects/security.go this time around**
---
Anyways, the main classes that already exist are...

## Bank
Represents the bank itself, useful for understanding staffing states and changing number of clerks

Methods
* `GetCurrentClerks() -> List[Clerk]` - returns the list of active clerks assigned to a desk at the bank
* `OpenNewClerkDesk() -> Tuple[Optional[Clerk], bool]` - "hires" a new clerk, assigns them a desk, and returns two values to the caller: 1) the Clerk reference itself and 2) a boolean of if a clerk was successfully hired or not. The second value boolean should only ever return false if the bank is already at max capacity
* `DismissClerk(clerk: Clerk) -> bool` - "fires" a clerk and returns a boolean for success. Useful for reducing overall operation costs when as many clerks aren't needed!

## Customer
A class for the customers visiting the bank

Methods
* `Mood() -> str` - Returns a string representing what kind of mood a customer is in?
* `StillHere() -> bool` - Returns a bool representing if a customer is still present at the bank or not

yes yes there are technically two more methods on this class, but don't use them its cheating! ;D

## Clerk
A class for the clerks that handle customer requests.
There is a good amount going on in this class, so spend some time familarizing yourself with the methods. (You will most likely need them at some point)

Methods
* `IsFree() -> bool` - Returns a bool representing if a clerk is currently free to assist a new customer
* `AssignCustomer(cus: Customer) -> bool` - This is the good stuff! The method you want to call to actually make a customer happy. The boolean return value indicates if a clerk was actually free to help the customer or not (they may already be busy with another)
* `Greet(sec: Security) -> bool` - Its very important to greet any newly hired Clerks. If you do so they will start calling the `ReadyToHelpWhosNext` whenever they free up making your security job a little easier. Remember the reference you should pass in this call is your-`self`

## Security
This is the class you will be working in and updating. Imagine it like you are taking on the role of bank security!

As security you are given access to a reference for the bank and can use this to invoke the Bank functions listed above. Beyond that you are expected to be able to acknowledge customers as they arrive, get them assigned to a clerk to help them, and manage the number of clerks on the floor at any given time. Once you've assigned a customer to an open clerk, your job is done (but maybe we'll add more later?)

To complete this task our focus is going to be on implementing the stubbed methods in the BankSecurity class
* `HandleNewCustomerArrival` is called any time a new customer arrives
* `ReadyToHelpWhosNext` is called by any clerk that has been "greeted" and is free to help another customer

HINT: You should feel empowered to change the Security class around however you need, you may find thing are much easier if you store additional data or add more methods to this class. Maybe something like a list of customers that are showing up??


# How to run and test
This program is pretty barebones and mostly just operates from the terminal
For the initial go, navigate to the code directory in any terminal and try:
```
python main.py
```
This will run the program with just one customer arriving. After that you can rerun with more customers by passing an additional argument like the following example for 5 total customer
```
python main.py -n 5
```

Try making the total customer amount longer and see how you do!

## How to share work?? (stretch goal)
Make a branch of this using git on local then open a new PR via a remote push!! (wow such git wow)

**Good luck!**
