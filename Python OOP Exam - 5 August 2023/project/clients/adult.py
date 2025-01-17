from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INITIAL_INTEREST: float = 4.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += 2.0
