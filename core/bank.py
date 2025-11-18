import time
import random
from typing import List, Tuple, Optional

from core.clerk import Clerk, NewClerk
from core.customer import Customer, NewCustomer
from project.security import BankSecurity

MAX_CLERKS_FOR_BRANCH = 6

class Bank:
    def GetCurrentClerks(self) -> List[Clerk]:
        raise NotImplementedError

    def OpenNewClerkDesk(self) -> Tuple[Optional[Clerk], bool]:
        raise NotImplementedError

    def DismissClerk(self, clerk: Clerk) -> bool:
        raise NotImplementedError


# ===== Concrete Bank Implementation =====
class bank(Bank):
    def __init__(self):
        self.activeClerks: List[Clerk] = []
        self.allCustomers: List[Customer] = []
        self.security: Optional[BankSecurity] = None
        self.hiredClerks = 0

    @staticmethod
    def InitBank():
        b = bank()
        security = BankSecurity(b)
        b.security = security

        newClerk = b.OpenNewClerkDesk()
        newClerk.Greet(security)
        return b

    # ---- Interface Methods ----
    def GetCurrentClerks(self) -> List[Clerk]:
        return self.activeClerks

    def OpenNewClerkDesk(self) -> Optional[Clerk]:
        if len(self.activeClerks) >= MAX_CLERKS_FOR_BRANCH:
            return None

        newClerk = NewClerk()
        self.hiredClerks += 1
        self.activeClerks.append(newClerk)
        return newClerk

    def DismissClerk(self, clerk: Clerk) -> bool:
        if clerk is None:
            return False

        clerk.Dismiss()
        self.activeClerks = [c for c in self.activeClerks if c is not clerk]
        return True

    # ---- Main Behavior Methods ----
    def startSpawningCustomers(self, amount: int):
        print("The bank is open!")
        for _ in range(amount):
            print("A new customer just arrived")
            bankCustomer = NewCustomer()
            self.allCustomers.append(bankCustomer)

            self.security.HandleNewCustomerArrival(bankCustomer)

            time.sleep(random.uniform(0.2, 2.0))

        print("The bank is closing~ Waiting for final customer(s) to leave")
        while not self.__checkIfAllCustomersDone():
            print("waiting...")
            time.sleep(1)

        print("The bank is closed!")

        happyCustomers = sum(1 for cus in self.allCustomers if cus.Mood() == "Happy")

        if happyCustomers == amount:
            print("Good job handling all customers before they got too upset")
        else:
            print(
                f"Of {amount} total customers, {amount - happyCustomers} left unhappy. "
                "Try improving your clerk assignment some!"
            )

        print(
            f"During operating hours you had {self.hiredClerks} clerks working and ended "
            f"the day with {len(self.activeClerks)} still active"
        )

    def __checkIfAllCustomersDone(self) -> bool:
        return all(not cus.StillHere() for cus in self.allCustomers)