from typing import Any

from core.clerk import Clerk
from core.customer import Customer

# NOTE: Feel free to change this class however needed, just keep the initial two method signatures intact!

class BankSecurity:
    def __init__(self, bank: Any):
        self.bank = bank
    
    # HandleNewCustomerArrival is called any time a new customer arrives at the bank
    def HandleNewCustomerArrival(self, customer: Customer):
        # TODO: Implement
        pass

    # ReadyToHelpWhosNext is called by any clerk who has been "Greeted" and is ready to handle new customers
    def ReadyToHelpWhosNext(self, clerk: Clerk):
        # TODO: Implement
        pass