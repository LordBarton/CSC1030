#!/usr/bin/env
import sys

# Task 1
class Horse:

    def __init__(self, rank):
        self._rank = rank
        self._value = 1000 * (1.1 ** (100 - rank))

    def get_rank(self):
        return self._rank

    def get_value(self):
        return self._value

    def display(self):
        print(f"Horse with rank {self._rank} has a value of €{self._value:.2f}")


horses = [Horse(rank) for rank in range(1, 101)]


def horse_menu():
    while True:
        rank_input = int(
            input("\nEnter the rank of the horse (1-100) to display details, or enter -1 to display all horses: "))

        if rank_input == -1:
            print("\nDisplaying all horses by rank:")
            for horse in horses:
                horse.display()
            break
        elif 1 <= rank_input <= 100:
            horses[rank_input - 1].display()
        else:
            print(f"A horse with rank {rank_input} was not found!")

# Task 2

def sqr(ls):
    return [int(n)**2 for n in ls]

# Task 3

def revupp(ls):
    return [s[::-1].upper() for s in ls]

# Task 4

class BankAccount(object):

    def __init__(self, holder, ppsnum, accnum, balance=0.0):
        self._balance = float(balance)
        self.__holder = holder
        self.__accnum = accnum
        self.__ppsnum = ppsnum

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount >= 0:
            self._balance -= amount
        else:
            print("Insufficient balance")

    # Task 5
    def get_balance(self):
        type = (self.__class__.__name__).replace("Account", "")
        return f"Balance: {self._balance:.2f}\nAccount type: {type}"

    def get_holder(self):
        return self.__holder

    def get_pps(self):
        return self.__ppsnum

    def get_AccountType(self):
        return self.__class__.__name__

    def get_accountnumber(self):
        return self.__accnum
class SavingsAccount(BankAccount):

    def add_interest(self, rate):
        self._balance *= rate

    #Task 6
    def apply_interest(self):
        interest = 1.02
        self._balance *= interest

class CurrentAccount(BankAccount):
    max_overdraft = 100
    def withdraw(self, amount):
        if self._balance - amount >= self._balance - self.max_overdraft:
            self._balance -= amount
        else:
            print("Sorry, the maximum overdraft amount is", self.max_overdraft)

    def apply_interest(self):
        interest = 1.01
        self._balance *= interest