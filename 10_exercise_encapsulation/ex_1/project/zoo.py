from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def is_space(self, list_with_obj: List[object], capacity: int):
        return capacity > len(list_with_obj)

    def search_by_name(self, list_with_obj: List[object], name: str):
        try:
            return next(filter(lambda x: x.name == name, list_with_obj))
        except StopIteration:
            return None

    def add_animal(self, animal: Animal, price: int):
        if not self.is_space(self.animals, self.__animal_capacity):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if not self.is_space(self.workers, self.__workers_capacity):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        searched_worker = self.search_by_name(self.workers, worker_name)
        if searched_worker:
            self.workers.remove(searched_worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salaries = sum([w.salary for w in self.workers])

        if self.__budget >= workers_salaries:
            self.__budget -= workers_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_care = sum([a.money_for_care for a in self.animals])

        if self.__budget >= animals_care:
            self.__budget -= animals_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions_info = []
        tigers_info = []
        cheetahs_info = []

        for every_animal in self.animals:
            if every_animal.__class__.__name__ == "Lion":
                lions_info.append(every_animal.__repr__())
            elif every_animal.__class__.__name__ == "Tiger":
                tigers_info.append(every_animal.__repr__())
            elif every_animal.__class__.__name__ == "Cheetah":
                cheetahs_info.append(every_animal.__repr__())

        result += f"----- {len(lions_info)} Lions:\n"
        for info in lions_info:
            result += f"{info}\n"

        result += f"----- {len(tigers_info)} Tigers:\n"
        for info in tigers_info:
            result += f"{info}\n"

        result += f"----- {len(cheetahs_info)} Cheetahs:\n"
        for info in cheetahs_info:
            result += f"{info}\n"

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers_info = []
        caretakers_info = []
        vets_info = []

        for every_worker in self.workers:
            if every_worker.__class__.__name__ == "Keeper":
                keepers_info.append(every_worker.__repr__())
            elif every_worker.__class__.__name__ == "Caretaker":
                caretakers_info.append(every_worker.__repr__())
            elif every_worker.__class__.__name__ == "Vet":
                vets_info.append(every_worker.__repr__())

        result += f"----- {len(keepers_info)} Keepers:\n"
        for info in keepers_info:
            result += f"{info}\n"

        result += f"----- {len(caretakers_info)} Caretakers:\n"
        for info in caretakers_info:
            result += f"{info}\n"

        result += f"----- {len(vets_info)} Vets:\n"
        for info in vets_info:
            result += f"{info}\n"

        return result.strip()
