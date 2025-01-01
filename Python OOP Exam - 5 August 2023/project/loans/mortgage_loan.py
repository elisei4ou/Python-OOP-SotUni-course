from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST_RATE: float = 3.5
    AMOUNT: float = 50000.0

    def __init__(self):
        super().__init__(self.INTEREST_RATE, self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5
