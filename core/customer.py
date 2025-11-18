import threading
import time
import random
from typing import Any


# ===== Customer Mood Enum Equivalent =====
class CustomerMood:
    Happy = "happy"
    Fine = "fine"
    Impatient = "impatient"


# ===== Customer Interface Equivalent =====
class Customer:
    def StartHelping(self):
        raise NotImplementedError

    def FinishHelping(self):
        raise NotImplementedError

    def Mood(self) -> str:
        raise NotImplementedError

    def StillHere(self) -> bool:
        raise NotImplementedError


def NewCustomer():
    return _Customer()


class _Customer(Customer):
    def __init__(self):
        # Random wait: 5–8 seconds
        randomSeconds = random.randint(5, 8)
        self.maxWaitTime = randomSeconds

        self.happy = False
        self.beingHelped = False
        self.left = False

        # Mimic Go goroutine: "go cust.leave()"
        thread = threading.Thread(target=self._leave_after_wait, daemon=True)
        thread.start()

    # ---------- Customer Actions ----------
    def StartHelping(self):
        self.beingHelped = True

    def FinishHelping(self):
        if not self.beingHelped:
            return

        self.happy = True
        self.left = True
        print("A customer left happy!!")

    def _leave_after_wait(self):
        time.sleep(self.maxWaitTime)

        if self.left or self.beingHelped:
            return

        self.left = True
        print("A customer left unhappy....")

    def Mood(self):
        if self.happy:
            return CustomerMood.Happy
        return CustomerMood.Fine

    def StillHere(self):
        return not self.left