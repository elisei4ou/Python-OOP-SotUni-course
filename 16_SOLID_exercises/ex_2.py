from abc import ABC, abstractmethod
import time


class AbstractWorker(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass


class Worker(AbstractWorker, Eatable):

    def work(self):
        print("I am normal worker. I am working.")

    def eat(self):
        print("Lunch break....(5sec)")
        time.sleep(5)


class SuperWorker(AbstractWorker, Eatable):

    def work(self):
        print("I am super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3sec)")
        time.sleep(3)


class BaseManager(ABC):
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        pass


class WorkManager(BaseManager):

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), f"`worker` must be of type {AbstractWorker}"
        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(BaseManager):

    def set_worker(self, worker):
        assert isinstance(worker, Eatable), f"`worker` must be of type {Eatable}"
        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


class Robot(AbstractWorker):
    def work(self):
        print("I am robot. I am working....")


class LazyPerson(Eatable):
    def eat(self):
        print("I only eat...")


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()


work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass