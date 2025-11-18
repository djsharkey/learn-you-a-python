import threading
import random
import time

from typing import Optional
from core.customer import Customer

class Clerk:
    """
    Python equivalent to the Go Clerk interface.
    """
    def Greet(self, sec) -> bool:
        raise NotImplementedError

    def AssignCustomer(self, cus: Customer) -> bool:
        raise NotImplementedError

    def IsFree(self) -> bool:
        raise NotImplementedError

    def Dismiss(self):
        raise NotImplementedError


def NewClerk():
    return _Clerk()


class _Clerk(Clerk):
    def __init__(self):
        self.assignedCustomer: Optional[Customer] = None
        self.security = None
        self.isWorking = False
        self.isDismissed = False

    def AssignCustomer(self, cus: Customer) -> bool:
        if self.isDismissed or self.assignedCustomer is not None:
            return False

        self.assignedCustomer = cus

        # Start background work similar to Go goroutine
        thread = threading.Thread(target=self.handleAssignedCustomer)
        thread.daemon = True
        thread.start()

        return True

    def Greet(self, sec) -> bool:
        if self.isDismissed:
            return False
        self.security = sec
        return True

    def IsFree(self) -> bool:
        if self.isDismissed:
            return False
        return self.assignedCustomer is None

    def Dismiss(self):
        self.isDismissed = True

    # ========== Internal work simulation ==========
    def handleAssignedCustomer(self):
        if self.assignedCustomer is None:
            return

        self.isWorking = True
        self.assignedCustomer.StartHelping()

        randomSeconds = random.randint(1, 4)
        time.sleep(randomSeconds)

        self.assignedCustomer.FinishHelping()

        self.assignedCustomer = None
        self.isWorking = False

        # Tell security “I’m ready for next customer”
        if self.security is not None:
            # Placeholder callback (may not exist in current placeholder)
            if hasattr(self.security, "ReadyToHelpWhosNext"):
                self.security.ReadyToHelpWhosNext(self)