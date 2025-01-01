from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}
    GRANTED_LOANS = 0

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def find_client(self, current_client_id):
        try:
            client = [c for c in self.clients if c.client_id == current_client_id][0]
            return client
        except IndexError:
            return None

    def find_loan(self, loan_type):
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                return loan

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS.keys():
            raise Exception("Invalid loan type!")

        new_loan = self.VALID_LOANS[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS.keys():
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        new_client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    # TODO check method
    def grant_loan(self, loan_type: str, client_id: str):
        client = self.find_client(client_id)
        loan = self.find_loan(loan_type)

        if client.__class__.__name__ == "Adult" and loan_type == "StudentLoan":
            raise Exception("Inappropriate loan type!")
        if client.__class__.__name__ == "Student" and loan_type == "MortgageLoan":
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        self.GRANTED_LOANS += 1
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.find_client(client_id)

        if not client:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                changed_loans += 1
                loan.increase_interest_rate()

        return f"Successfully changed {changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_interest = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_interest += 1

        return f"Number of clients affected: {changed_interest}."

    def get_statistics(self):
        clients_income = sum(c.income for c in self.clients)
        all_granted_sum = sum([sum([l.amount for l in c.loans]) for c in self.clients])
        not_granted_sum = sum([l.amount for l in self.loans])

        try:
            clients_interest_rates = sum([c.interest for c in self.clients])
            average_interest = clients_interest_rates / len(self.clients)
        except ZeroDivisionError:
            average_interest = 0

        result = f"Active Clients: {len(self.clients)}\n" \
                 f"Total Income: {clients_income:.2f}\n" \
                 f"Granted Loans: {self.GRANTED_LOANS}, Total Sum: {all_granted_sum:.2f}\n" \
                 f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n" \
                 f"Average Client Interest Rate: {average_interest:.2f}"

        return result





